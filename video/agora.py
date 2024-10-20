import os
from agora_token_builder import RtcTokenBuilder
import time

app_id = os.getenv("AGORA_APP_ID")
app_certificate = os.getenv("AGORA_APP_CERTIFICATE")

def generate_agora_token(channel_name: str, uid: str, role_num: int = 1, expire_time_seconds: int = 3600):
    current_timestamp = int(time.time())
    expire_time = current_timestamp + expire_time_seconds
    
    token = RtcTokenBuilder.buildTokenWithUid(app_id, app_certificate, channel_name, uid, role_num, expire_time)
    return token

def create_agora_channel(interview_id: str):
    channel_name = f"interview_{interview_id}"
    return channel_name

def get_agora_credentials(interview_id: str, user_id: str):
    channel_name = create_agora_channel(interview_id)
    token = generate_agora_token(channel_name, user_id)
    
    return {
        "app_id": app_id,
        "channel_name": channel_name,
        "token": token
    }