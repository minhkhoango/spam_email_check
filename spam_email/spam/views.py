from django.shortcuts import render

# Create your views here.
import pandas as pd
import joblib
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

model_name = 'model.joblib'
vectorizer_name = 'vectorizer.joblib'

def main():
    model, vectorizer = load_models()

    X_pred = get_input(vectorizer)
    y_pred = model.predict(X_pred)
    
    if y_pred[0] == 1:
        print('This email is classified as Spam')
    else:
        print('This email is classified as Not Spam')

def analyzer_function(x):
    return x

def load_models():
    model = joblib.load(model_name)
    vectorizer = joblib.load(vectorizer_name)
    return model, vectorizer

def get_input(vectorizer):
    inp = input('Email to check: ')
    tokenized_input = sentence_tokenizer(inp)
    X_pred = vectorizer.transform([tokenized_input])
    return X_pred

def sentence_tokenizer(sentence):
    return set(word for word in word_tokenize(sentence)
               if any(c.isalpha() for c in word))

if __name__ == '__main__':
    main()