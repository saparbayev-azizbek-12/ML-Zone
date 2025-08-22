from django.shortcuts import render
from tasks.services.spam_classifier import predict

def index(request):
    context = {}
    if request.method == 'POST':
        message = request.POST.get('message', '')
        context['user_input'] = message

        if message:
            try:
                pred = predict(message)
                if pred['status']:
                    is_spam = pred['is_spam']
                    context['prediction'] = 'Spam' if is_spam == 1 else 'Not Spam'
                else:
                    context['prediction'] = None

            except Exception as e:
                context['error'] = f"An error occurred: {str(e)}"

    return render(request, 'spam_classifier/index.html', context)