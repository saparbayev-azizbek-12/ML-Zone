# ML-Zone 🤖
Site link: https://mlzone.pythonanywhere.com

A modern Django web application showcasing interactive machine learning projects with a beautiful, responsive interface.

## 🌟 Features

- **Interactive ML Models**: Three different machine learning projects with real-time predictions
- **Modern UI**: Clean, responsive design with dark/light theme support
- **Real-time Processing**: AJAX-powered predictions without page refreshes
- **Mobile Friendly**: Fully responsive design that works on all devices

## 🚀 Projects Included

### 1. 🔢 Digit Recognition
- **Description**: Interactive handwritten digit classifier
- **Technology**: Computer Vision with scikit-learn
- **Interface**: Canvas drawing with real-time prediction
- **Model**: Pre-trained digit classification model

### 2. 🏠 House Price Prediction
- **Description**: Real estate price prediction based on property features
- **Technology**: Regression analysis with scikit-learn
- **Interface**: Form-based input for house characteristics
- **Features**: Predicts market price based on area, bedrooms, location, etc.

### 3. 📧 Spam Classifier
- **Description**: Email spam detection system
- **Technology**: Text classification with NLP
- **Interface**: Text input for email content analysis
- **Model**: Uses Count Vectorizer and classification algorithms

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Machine Learning**: scikit-learn 1.7.0
- **Data Processing**: NumPy 2.3.1, Pillow 11.3.0
- **Frontend**: Tailwind CSS, Font Awesome
- **Database**: SQLite
- **Model Storage**: Joblib for serialized ML models

## 📁 Project Structure

```
ML-Zone/
├── config/                 # Django configuration
│   ├── settings.py        # Main settings
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI configuration
├── pages/                 # Home page application
│   ├── views/            # Page views
│   └── urls.py           # Page URL patterns
├── tasks/                 # ML task implementations
│   ├── views/            # Task-specific views
│   │   ├── digit_recognition.py
│   │   ├── house_price.py
│   │   └── spam_classifier.py
│   └── urls.py           # Task URL patterns
├── models/               # Pre-trained ML models
│   ├── digit_recognition/
│   │   └── digit_clf.joblib
│   └── spam_classifier/
│       ├── spam_classifier_model.joblib
│       └── count_vectorizer.joblib
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── pages/           # Page templates
│   ├── partials/        # Reusable components
│   └── [task_templates] # Task-specific templates
├── static/              # Static assets (CSS, JS, images)
├── requirements.txt     # Python dependencies
└── manage.py           # Django management script
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ML-Zone
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   Navigate to `http://127.0.0.1:8000/` to view the application

## 📱 Usage

### Home Page
- Browse available ML projects
- Navigate to individual project pages
- Toggle between light and dark themes

### Digit Recognition
- Draw digits on the interactive canvas
- Get real-time predictions as you draw
- Clear canvas to try new digits

### House Price Prediction
- Enter house characteristics (area, bedrooms, etc.)
- Submit form to get price prediction
- View detailed prediction results

### Spam Classifier
- Enter email text content
- Analyze text for spam probability
- Get classification results with confidence scores

## 🎨 UI Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Dark/Light Theme**: Automatic theme detection with manual toggle
- **Modern Animations**: Smooth transitions and hover effects
- **Interactive Elements**: Real-time feedback and loading states
- **Accessibility**: ARIA labels and keyboard navigation support

## 🔧 Development

### Adding New ML Projects

1. Create model files in `/models/[project_name]/`
2. Add view logic in `/tasks/views/[project_name].py`
3. Create templates in `/templates/[project_name]/`
4. Update URL patterns in `/tasks/urls.py`
5. Add project card to home page template

### Model Requirements
- Models should be saved using `joblib.dump()`
- Include error handling for missing model files
- Implement proper input validation and preprocessing

## 📦 Dependencies

```
asgiref==3.9.1
datadispatch==1.0.0
Django==5.2.4
joblib==1.5.1
numpy==2.3.1
pillow==11.3.0
scikit-learn==1.7.0
scipy==1.16.0
sqlparse==0.5.3
threadpoolctl==3.6.0
tzdata==2025.2
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Django and scikit-learn
- UI powered by Tailwind CSS
- Icons from Font Awesome
- Machine learning models trained on standard datasets

---

**Made with ❤️ for the ML community**
