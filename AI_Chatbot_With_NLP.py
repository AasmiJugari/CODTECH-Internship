# AI Chatbot using Natural Language Processing (NLTK)
# CODTECH Internship - AI Chatbot with NLP

import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer

# Run only once if needed
# nltk.download('punkt')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    return [lemmatizer.lemmatize(token) for token in tokens]

# Knowledge base
knowledge_base = [
    "I am an AI chatbot created using natural language processing.",
    "Natural language processing helps computers understand human language.",
    "Python is widely used for artificial intelligence applications.",
    "Chatbots are used in customer support, education and healthcare.",
    "CODTECH internship provides practical exposure to students.",
    "Machine learning is a subset of artificial intelligence."
]

def chatbot(query):
    knowledge_base.append(query)

    vectorizer = TfidfVectorizer(tokenizer=preprocess, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(knowledge_base)

    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    index = similarity.argsort()[0][-2]
    score = similarity.flatten()[-2]

    knowledge_base.pop()

    if score == 0:
        return "Sorry, I don't have an answer to that."
    else:
        return knowledge_base[index]

# -------------------------------
# Chatbot Interaction (IDLE)
# -------------------------------
print("AI Chatbot (Type 'exit' to stop)")

while True:
    user_query = input("You: ")
    
    if user_query.lower() == "exit":
        print("AI Chatbot: Thank you! Goodbye.")
        break

    response = chatbot(user_query)
    print("AI Chatbot:", response)
