import os
import json
import pandas as pd
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from .utils import file_name_generator, save_file


def analysis(dframe_path: str) -> list[str]:
    dframe = pd.read_csv(dframe_path)
    return dframe.columns.tolist()

def build_text(df, columns):
    subset = df[columns].astype(str).fillna("")
    texts = []

    for _, row in subset.iterrows():
        values = sorted(v.strip() for v in row if v.strip())
        text = " | ".join(values)
        texts.append(text)

    return texts


def index(request):
    return render(request, "smart_join/index.html")


@csrf_exempt
def upload(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST is allowed"}, status=405)

    file1 = request.FILES.get("df1")
    file2 = request.FILES.get("df2")

    if not file1 or not file2:
        return JsonResponse({"error": "Both df1 and df2 files are required"}, status=400)

    name1 = file_name_generator(file1)
    name2 = file_name_generator(file2)
    path1 = save_file(file1, name1, subdirectory="smart_join")
    path2 = save_file(file2, name2, subdirectory="smart_join")

    cols1 = analysis(path1)
    cols2 = analysis(path2)

    return JsonResponse(
        {
            "df1_name": name1,
            "df2_name": name2,
            "df1_columns": cols1,
            "df2_columns": cols2,
        }
    )


@csrf_exempt
def run_join(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST is allowed"}, status=405)

    try:
        request_data = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    df1_name = request_data.get("df1_name")
    df2_name = request_data.get("df2_name")
    df1_selected_columns = request_data.get("df1_columns") or []
    df2_selected_columns = request_data.get("df2_columns") or []
    threshold = float(request_data.get("threshold", 0.75))
    join_type = request_data.get("join_type", "inner")

    if not df1_name or not df2_name:
        return JsonResponse({"error": "df1_name and df2_name are required"}, status=400)

    if join_type not in {"inner", "left", "right", "outer"}:
        join_type = "inner"

    base_dir = os.path.join(settings.MEDIA_ROOT, "smart_join")
    df1_path = os.path.join(base_dir, df1_name)
    df2_path = os.path.join(base_dir, df2_name)

    if not os.path.exists(df1_path) or not os.path.exists(df2_path):
        return JsonResponse({"error": "Uploaded files not found on server"}, status=404)

    df1 = pd.read_csv(df1_path)
    df2 = pd.read_csv(df2_path)

    if not isinstance(df1_selected_columns, list) or not df1_selected_columns:
        df1_selected_columns = df1.columns.tolist()
    if not isinstance(df2_selected_columns, list) or not df2_selected_columns:
        df2_selected_columns = df2.columns.tolist()

    df1_text = build_text(df1, df1_selected_columns)
    df2_text = build_text(df2, df2_selected_columns)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    emb1 = model.encode(df1_text)
    emb2 = model.encode(df2_text)

    similarity_matrix = cosine_similarity(emb1, emb2)
    matches = []

    for i, row in enumerate(similarity_matrix):
        best_match = row.argmax()
        score = row[best_match]

        if score >= threshold:
            matches.append({
                "df1_index": i,
                "df2_index": best_match,
                "similarity": score,
            })

    match_df = pd.DataFrame(matches)

    if match_df.empty:
        result = pd.DataFrame()
    else:
        result = (
            df1
            .merge(match_df, left_index=True, right_on="df1_index", how=join_type)
            .merge(df2, left_on="df2_index", right_index=True, suffixes=("_df1", "_df2"), how=join_type)
        )

    preview_limit = 50
    preview_df = result.head(preview_limit)
    columns = preview_df.columns.tolist()
    rows = preview_df.astype(str).values.tolist()

    output_dir = os.path.join(settings.MEDIA_ROOT, "smart_join")
    os.makedirs(output_dir, exist_ok=True)
    output_name = f"smart_join_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.csv"
    output_path = os.path.join(output_dir, output_name)
    result.to_csv(output_path, index=False)

    return JsonResponse({"columns": columns, "rows": rows, "csv_name": output_name})


