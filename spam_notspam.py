import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
nltk.download('punkt')
df = pd.read_csv("D:/Python/spam_or_not_spam.csv", encoding='latin-1')
df.columns = ["message", "label"]
df = df.dropna(subset=["message"])
df["message"] = df["message"].astype(str)
df["tokens"] = df["message"].apply(word_tokenize)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = MultinomialNB()
model.fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
user_input = input("Enter message: ")
input_vector = vectorizer.transform([user_input])
prediction = model.predict(input_vector)
print("Spam" if prediction[0] == 1 else "Not Spam")