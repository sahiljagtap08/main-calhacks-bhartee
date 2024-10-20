from ai.groq_integration import generate_groq_response
import json

def get_interview_questions(job_description: str, num_questions: int = 5):
    prompt = f"""
    Based on this job description: {job_description}
    Generate {num_questions} relevant technical interview questions.
    Return the questions as a Python list.
    """
    response = generate_groq_response(prompt)
    return json.loads(response) if response else []

def analyze_interview(transcript: str, job_description: str):
    prompt = f"""
    Given this job description: {job_description}
    And this interview transcript: {transcript}
    Provide a detailed analysis of the candidate's performance. Include:
    1. Overall impression
    2. Technical skills assessment (rate out of 10 for each major skill mentioned in the job description)
    3. Communication skills (rate out of 10)
    4. Problem-solving ability (rate out of 10)
    5. Cultural fit (rate out of 10)
    6. Strengths
    7. Areas for improvement
    8. Specific examples from the interview supporting your analysis
    9. Recommendation (Strongly Hire / Hire / Maybe / Do Not Hire)
    10. Justification for your recommendation
    
    Format your response as a JSON object.
    """
    response = generate_groq_response(prompt)
    return json.loads(response) if response else {}

def generate_final_report(analysis: dict):
    prompt = f"""
    Based on the following interview analysis, generate a comprehensive final report:
    {json.dumps(analysis, indent=2)}
    
    The report should include:
    1. Executive summary
    2. Detailed breakdown of the candidate's performance
    3. Comparison to job requirements
    4. Final recommendation
    5. Next steps
    
    Format the report in Markdown.
    """
    return generate_groq_response(prompt)