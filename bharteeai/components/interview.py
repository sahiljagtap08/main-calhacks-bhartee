import reflex as rx
from bharteeai.utils.jdoodle import execute_code

class InterviewState(rx.State):
    code: str = ""
    language: str = "python3"
    output: str = ""

    def execute_code(self):
        result = execute_code(self.code, self.language)
        self.output = result.get("output", "Error executing code")

def interview():
    return rx.vstack(
        rx.heading("Coding Interview"),
        rx.select(
            ["python3", "java", "cpp", "javascript"],
            placeholder="Select language",
            on_change=InterviewState.set_language
        ),
        rx.text_area(
            placeholder="Write your code here",
            on_change=InterviewState.set_code,
            height="200px"
        ),
        rx.button("Run Code", on_click=InterviewState.execute_code),
        rx.text_area(
            InterviewState.output,
            placeholder="Output will appear here",
            is_read_only=True,
            height="100px"
        ),
        width="100%",
        padding="20px",
    )