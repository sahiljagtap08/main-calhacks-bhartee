import reflex as rx
from bharteeai.components.auth import user_button
from bharteeai.state import State

def index():
    return rx.vstack(
        user_button(),
        rx.heading("Welcome to BharteeAI"),
        rx.cond(
            State.is_authenticated,
            rx.vstack(
                rx.text(f"Welcome, {State.user_role}!"),
                rx.cond(
                    State.is_client,
                    rx.link("Start Interview", href="/interview"),
                    rx.link("View Jobs", href="/jobs")
                )
            ),
            rx.vstack(
                rx.link("Client Sign In", href="/client/sign-in"),
                rx.link("Candidate Sign In", href="/candidate/sign-in"),
                rx.link("Client Sign Up", href="/client/sign-up"),
                rx.link("Candidate Sign Up", href="/candidate/sign-up")
            )
        )
    )