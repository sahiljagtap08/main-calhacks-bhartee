from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from clerk_backend_api import Clerk
import os

clerk_secret_key = os.getenv('CLERK_SECRET_KEY')
clerk = Clerk(secret_key=clerk_secret_key)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        claims = clerk.verify_token(token)
        return claims
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def get_current_client(current_user: dict = Depends(get_current_user)):
    if "client" not in current_user.get("public_metadata", {}).get("roles", []):
        raise HTTPException(status_code=403, detail="Not authorized as a client")
    return current_user

async def get_current_candidate(current_user: dict = Depends(get_current_user)):
    if "candidate" not in current_user.get("public_metadata", {}).get("roles", []):
        raise HTTPException(status_code=403, detail="Not authorized as a candidate")
    return current_user