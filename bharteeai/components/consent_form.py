import reflex as rx

class ConsentFormState(rx.State):
    consented: bool = False

    def toggle_consent(self, value: bool):
        self.consented = value

def consent_form():
    return rx.vstack(
        rx.text("By proceeding, you agree to our terms and conditions."),
        rx.checkbox("I agree", on_change=ConsentFormState.toggle_consent),
        rx.button(
            "Continue",
            on_click=rx.console_log("Consent given"),
            is_disabled=~ConsentFormState.consented
        ),
        width="100%",
        max_width="500px",
        spacing="1rem",
    )