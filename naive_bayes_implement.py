import pandas as pd
import numpy as np
from nltk import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

def main():
    X,y = load_data()
    vectorizer = CountVectorizer(analyzer=lambda x:x)
    # Transform email into context machine can understand, word into row with values
    X_counts = vectorizer.fit_transform(X)
    # Train the Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X_counts, y)

    X_pred = get_input(vectorizer)
    y_pred = model.predict(X_pred)
    print(y_pred)
    # Predict the label for test set

def get_input(vectorizer):
    inp = input('Email to check: ')
    tokenized_input = sentence_tokenizer(inp)
    X_pred = vectorizer.transform([tokenized_input])
    return X_pred

def sentence_tokenizer(sentence):
    return set(word for word in word_tokenize(sentence)
               if any(c.isalpha() for c in word))

def load_data():
    df = pd.read_csv('emails.csv')
    # Use regex to remove the Subject: part of the text column
    df['text'] = df['text'].str.replace(r'^Subject: ', '', regex=True)

    emails = df['text'].to_numpy(dtype='U')
    X = [sentence_tokenizer(email) for email in emails]
    y = df['spam'].to_numpy(dtype='int16')
    return X,y

if __name__ == '__main__':
    main()



