import os
import requests

JDOODLE_API_URL = "https://api.jdoodle.com/v1/execute"
CLIENT_ID = os.getenv("JDOODLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("JDOODLE_CLIENT_SECRET")

def execute_code(script, language, stdin=""):
    payload = {
        "script": script,
        "language": language,
        "versionIndex": "0",
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET,
        "stdin": stdin
    }
    
    response = requests.post(JDOODLE_API_URL, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        return {
            "output": result.get("output"),
            "statusCode": result.get("statusCode"),
            "memory": result.get("memory"),
            "cpuTime": result.get("cpuTime")
        }
    else:
        return {"error": "Failed to execute code", "status_code": response.status_code}