import reflex as rx
from bharteeai.components.auth import clerk_sign_in, clerk_sign_up

def sign_in():
    return rx.vstack(
        rx.heading("Candidate Sign In"),
        clerk_sign_in("/candidate/sign-in")
    )

def sign_up():
    return rx.vstack(
        rx.heading("Candidate Sign Up"),
        clerk_sign_up("/candidate/sign-up")
    )