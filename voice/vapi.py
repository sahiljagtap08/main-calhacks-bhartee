import os
import requests

VAPI_API_URL = "https://api.vapi.ai"
VAPI_API_KEY = os.getenv("VAPI_API_KEY")

headers = {
    "Authorization": f"Bearer {VAPI_API_KEY}",
    "Content-Type": "application/json"
}

def create_vapi_assistant(name: str, instructions: str) -> str:
    payload = {
        "name": name,
        "instructions": instructions,
        "model": {
            "provider": "openai",
            "model": "gpt-3.5-turbo",
            "temperature": 0.7
        },
        "voice": {
            "provider": "eleven_labs",
            "voice_id": "21m00Tcm4TlvDq8ikWAM"
        },
        "asr": {
            "provider": "deepgram",
            "language": "en-US"
        }
    }
    
    response = requests.post(f"{VAPI_API_URL}/assistants", headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["assistant_id"]

def start_vapi_call(assistant_id: str) -> dict:
    payload = {
        "assistant_id": assistant_id,
        "caller_id": "+11234567890"  # Replace with actual caller ID if needed
    }
    
    response = requests.post(f"{VAPI_API_URL}/calls", headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def send_message_to_call(call_id: str, message: str) -> dict:
    payload = {
        "message": message
    }
    
    response = requests.post(f"{VAPI_API_URL}/calls/{call_id}/message", headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def get_call_transcript(call_id: str) -> str:
    response = requests.get(f"{VAPI_API_URL}/calls/{call_id}/transcript", headers=headers)
    response.raise_for_status()
    return response.json()["transcript"]

def end_vapi_call(call_id: str) -> dict:
    response = requests.post(f"{VAPI_API_URL}/calls/{call_id}/end", headers=headers)
    response.raise_for_status()
    return response.json()

def conduct_interview(job_description: str, questions: list) -> dict:
    assistant_id = create_vapi_assistant(
        name="BharteeAI Interviewer",
        instructions=f"You are an AI interviewer for a tech position. Job Description: {job_description}"
    )
    
    call = start_vapi_call(assistant_id)
    call_id = call["call_id"]
    
    for question in questions:
        send_message_to_call(call_id, question)
        # In a real scenario, you'd wait for the candidate's response here
        # This could involve webhooks or polling the call status
    
    transcript = get_call_transcript(call_id)
    end_vapi_call(call_id)
    
    return {
        "assistant_id": assistant_id,
        "call_id": call_id,
        "transcript": transcript
    }