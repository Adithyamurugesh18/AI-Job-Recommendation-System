import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("data/jobs.csv")

# Convert text into vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(data["job_description"])

# Recommendation function
def recommend_jobs(resume_text):
    resume_vec = vectorizer.transform([resume_text])
    similarity = cosine_similarity(resume_vec, tfidf_matrix)
    top_indexes = similarity.argsort()[0][-3:][::-1]
    return data.iloc[top_indexes][["job_title", "company"]]
