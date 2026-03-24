import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
text = input("Enter your text: ")
sentences = sent_tokenize(text)
words = word_tokenize(text)
characters = list(text)
print("Sentence Tokenization: ",sentences)
print("Word Tokenization: ",words)
print("Character Tokenization : ",characters)
