import re
from datetime import datetime

def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def format_date(date: datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M:%S")

def truncate_text(text: str, max_length: int = 100) -> str:
    return text[:max_length] + '...' if len(text) > max_length else text

def generate_interview_id(candidate_id: str, job_id: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"INT-{candidate_id}-{job_id}-{timestamp}"