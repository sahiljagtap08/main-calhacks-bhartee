import reflex as rx
from bharteeai.components.interview import interview
from bharteeai.state import State

def interview_page():
    return rx.vstack(
        rx.cond(
            State.is_authenticated,
            rx.vstack(
                rx.heading("Technical Interview"),
                interview(),
            ),
            rx.redirect("/")
        )
    )