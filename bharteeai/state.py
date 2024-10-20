import reflex as rx
import httpx

class State(rx.State):
    user_token: str = ""
    user_role: str = ""

    def login(self, token: str):
        self.user_token = token
        self.verify_token()

    def logout(self):
        self.user_token = ""
        self.user_role = ""

    def verify_token(self):
        headers = {"Authorization": f"Bearer {self.user_token}"}
        response = httpx.get("https://api.clerk.dev/v1/me", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            self.user_role = "client" if "client" in user_data.get("public_metadata", {}).get("roles", []) else "candidate"
        else:
            self.logout()

    @rx.var
    def is_authenticated(self) -> bool:
        return bool(self.user_token)

    @rx.var
    def is_client(self) -> bool:
        return self.user_role == "client"

    @rx.var
    def is_candidate(self) -> bool:
        return self.user_role == "candidate"