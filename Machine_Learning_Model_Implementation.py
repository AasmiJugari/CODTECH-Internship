# Spam Email Detection using Machine Learning
# CODTECH Internship – ML Model Implementation

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------
# Step 1: Create Dataset
# -----------------------------
data = {
    "label": ["ham", "spam", "ham", "spam", "ham", "spam", "ham", "spam", "ham", "spam"],
    "message": [
        "Hey are we still meeting today?",
        "Win a free iPhone now click here",
        "Please call me when you reach home",
        "You have won a cash prize of 100000",
        "Let's have lunch tomorrow",
        "Exclusive offer limited time deal",
        "Can you send the report by evening?",
        "Congratulations you are selected for lottery",
        "Are you coming to class today?",
        "Claim your free reward now"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Preprocessing
# -----------------------------
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['message']
y = df['label']

# -----------------------------
# Step 3: Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Step 4: Text Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# -----------------------------
# Step 5: Train Model
# -----------------------------
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# -----------------------------
# Step 6: Model Evaluation
# -----------------------------
y_pred = model.predict(X_test_tfidf)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# -----------------------------
# Step 7: Predict New Email
# -----------------------------
new_email = ["Congratulations! You won a free gift"]
new_email_vector = vectorizer.transform(new_email)
result = model.predict(new_email_vector)

print("\nNew Email Prediction:")
if result[0] == 1:
    print("Spam Email")
else:
    print("Not Spam Email")
