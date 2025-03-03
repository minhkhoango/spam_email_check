from django.shortcuts import render
from django.conf import settings
import os
# Create your views here.
import joblib
from nltk import word_tokenize


class Classify:
    def __init__(self, inp=None):
        self.model = joblib.load(self.get_path('model.joblib'))
        self.vectorizer = joblib.load(self.get_path('vectorizer.joblib'))
        self.inp = inp
    
    def get_path(self, name):
        return os.path.join(settings.BASE_DIR, 'spam', 'ml_models', name)
    
    def get_input(self):
        if self.inp is None:
            return None
        tokenized_input = set(word for word in word_tokenize(self.inp)
                if any(c.isalpha() for c in word))
        return self.vectorizer.transform([tokenized_input])

    def check_spam(self):
        X_pred = self.get_input()
        y_pred = self.model.predict(X_pred)

        if y_pred[0] == 1:
            return 'spam'
        else:
            return 'notspam'
        
def analyzer_function(x):
    return x

def index(request):
    if request.method == 'POST':
        email_content = request.POST['email'].strip()
        if not email_content:
            return render(request, 'spam/index.html', {'spam_result': 'No input provded'})
        
        classifier = Classify(email_content)
        spam_result = classifier.check_spam()
        return render(request, 'spam/index.html', {
            'spam_result': spam_result,
        })
        
    return render(request, 'spam/index.html')


    