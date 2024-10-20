import pytest
from bharteeai.pages import home, client, candidate, interview
from bharteeai.components import navbar, job_form, consent_form, interview_results

def test_home_page():
    home_component = home.index()
    assert "Welcome to BharteeAI" in str(home_component)

def test_client_sign_in():
    sign_in_component = client.sign_in()
    assert "Client Sign In" in str(sign_in_component)

def test_candidate_sign_up():
    sign_up_component = candidate.sign_up()
    assert "Candidate Sign Up" in str(sign_up_component)

def test_interview_page():
    interview_component = interview.interview_page()
    assert "Technical Interview" in str(interview_component)

def test_navbar():
    navbar_component = navbar.navbar()
    assert "BharteeAI" in str(navbar_component)

def test_job_form():
    form_component = job_form.job_form()
    assert "Post a Job" in str(form_component)

def test_consent_form():
    consent_component = consent_form.consent_form()
    assert "I agree" in str(consent_component)

def test_interview_results():
    mock_results = {
        "overall_score": 8,
        "technical_skills": 7,
        "communication_skills": 9,
        "problem_solving": 8,
        "cultural_fit": 8,
        "strengths": ["Python", "Problem Solving"],
        "areas_for_improvement": ["SQL"],
        "recommendation": "Hire"
    }
    results_component = interview_results.interview_results(mock_results)
    assert "Interview Results" in str(results_component)