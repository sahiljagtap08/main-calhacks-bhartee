from database.chroma import add_resume, search_resumes
from ai.groq_integration import generate_groq_response
import json

def screen_resume(resume_text: str, job_description: str, candidate_id: str):
    # Add resume to Chroma DB
    add_resume(resume_text, candidate_id)

    # Use Groq to analyze resume
    prompt = f"""
    Compare the following resume to the job description. 
    Provide a detailed analysis including:
    1. Relevant skills match (score out of 10)
    2. Experience match (score out of 10)
    3. Overall suitability (score out of 10)
    4. Key strengths
    5. Potential areas for improvement

    Resume: {resume_text}

    Job Description: {job_description}

    Provide the response as a JSON object.
    """

    analysis = generate_groq_response(prompt)
    analysis_json = json.loads(analysis)

    # Perform semantic search
    search_results = search_resumes(job_description, n_results=1)
    semantic_score = 1 - min(search_results['distances'][0][0], 1) if search_results['distances'] else 0

    # Combine scores
    overall_score = (analysis_json['skills_match'] + analysis_json['experience_match'] + analysis_json['overall_suitability'] + semantic_score * 10) / 4

    return {
        "overall_score": overall_score,
        "analysis": analysis_json,
        "semantic_score": semantic_score
    }

def is_resume_suitable(screening_result, threshold=7.0):
    return screening_result["overall_score"] > threshold