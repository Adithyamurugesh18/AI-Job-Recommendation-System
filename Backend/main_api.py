from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recommender import recommend_jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Job Recommendation API Running"}

@app.post("/recommend")
def recommend(resume_text: str):
    jobs = recommend_jobs(resume_text)
    return jobs.to_dict(orient="records")