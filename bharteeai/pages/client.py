import reflex as rx
from bharteeai.components.auth import clerk_sign_in, clerk_sign_up

def sign_in():
    return rx.vstack(
        rx.heading("Client Sign In"),
        clerk_sign_in("/client/sign-in")
    )

def sign_up():
    return rx.vstack(
        rx.heading("Client Sign Up"),
        clerk_sign_up("/client/sign-up")
    )