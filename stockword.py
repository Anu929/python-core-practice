import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
stock_words = [
    "stock", "market", "shares", "price", "profit", "loss",
    "rise", "fall", "gain", "drop", "invest", "trading"
]
text = input("Enter stock news: ")
tokens = word_tokenize(text.lower())
result = [word for word in tokens if word in stock_words]
print("Output")
print("All Words:", tokens)
print("Stock Related Words:", result)