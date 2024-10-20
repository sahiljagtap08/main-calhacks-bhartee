import pytest
from bharteeai.server import auth
from bharteeai.utils import jdoodle
from database import singlestore, chroma
from ai import groq_integration, interview_assistant, resume_screening
from voice import vapi
from video import agora
from storage import s3

@pytest.mark.asyncio
async def test_auth():
    with pytest.raises(Exception):
        await auth.get_current_user("invalid_token")

def test_jdoodle():
    result = jdoodle.execute_code("print('Hello, World!')", "python3")
    assert "Hello, World!" in result["output"]

def test_singlestore():
    session = singlestore.get_session()
    assert session is not None

def test_chroma():
    result = chroma.search_resumes("Python developer")
    assert isinstance(result, dict)

def test_groq_integration():
    response = groq_integration.generate_groq_response("What is 2+2?")
    assert response is not None

def test_interview_assistant():
    questions = interview_assistant.get_interview_questions("Python Developer")
    assert len(questions) > 0

def test_resume_screening():
    result = resume_screening.screen_resume("Python developer with 5 years experience", "Looking for a Python developer", "candidate1")
    assert "overall_score" in result

def test_vapi():
    assistant_id = vapi.create_vapi_assistant("Test Assistant", "You are a test assistant")
    assert assistant_id is not None

def test_agora():
    credentials = agora.get_agora_credentials("test_interview", "user1")
    assert "app_id" in credentials

def test_s3():
    result = s3.upload_file("test.txt", "test_object")
    assert result is True
    s3.delete_file("test_object")