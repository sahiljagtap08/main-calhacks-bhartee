import reflex as rx
from bharteeai import styles
from bharteeai.state import State
from bharteeai.pages import home, client, candidate, interview

class BharteeAI(rx.App):
    def __init__(self):
        super().__init__(style=styles.base_style)
        self.add_page(home.index, route="/")
        self.add_page(client.sign_in, route="/client/sign-in")
        self.add_page(client.sign_up, route="/client/sign-up")
        self.add_page(candidate.sign_in, route="/candidate/sign-in")
        self.add_page(candidate.sign_up, route="/candidate/sign-up")
        self.add_page(interview.interview_page, route="/interview")

app = BharteeAI()