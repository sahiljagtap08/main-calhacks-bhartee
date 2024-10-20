import reflex as rx
from bharteeai.state import State

def navbar():
    return rx.hstack(
        rx.heading("BharteeAI"),
        rx.spacer(),
        rx.hstack(
            rx.cond(
                State.is_authenticated,
                rx.hstack(
                    rx.link("Home", href="/"),
                    rx.cond(
                        State.is_client,
                        rx.link("Start Interview", href="/interview"),
                        rx.link("View Jobs", href="/jobs")
                    ),
                    rx.button("Logout", on_click=State.logout)
                ),
                rx.hstack(
                    rx.link("Sign In", href="/sign-in"),
                    rx.link("Sign Up", href="/sign-up")
                )
            )
        ),
        width="100%",
        padding="1rem",
        bg="rgb(240, 240, 240)",
    )