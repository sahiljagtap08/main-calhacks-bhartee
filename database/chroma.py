import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

collection = client.create_collection("resumes")

def add_resume(resume_text: str, candidate_id: str):
    collection.add(
        documents=[resume_text],
        metadatas=[{"source": "candidate"}],
        ids=[f"resume_{candidate_id}"]
    )

def search_resumes(job_description: str, n_results: int = 5):
    results = collection.query(
        query_texts=[job_description],
        n_results=n_results
    )
    return results