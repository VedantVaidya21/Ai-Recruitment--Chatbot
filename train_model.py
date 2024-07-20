import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load the dataset
data = pd.read_csv('Datasets.csv')

# Ensure the dataset has the correct columns
assert 'questions' in data.columns, "Dataset must have a 'questions' column."
assert 'answers' in data.columns, "Dataset must have an 'answers' column."

# Split the dataset into features and labels
X = data['questions']
y = data['answers']

# Vectorize the text data
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save the trained model
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Save the vectorizer
with open('cmodel.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model and vectorizer have been saved.")
