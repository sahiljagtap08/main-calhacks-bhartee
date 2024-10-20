import reflex as rx
from bharteeai.state import State

class JobFormState(rx.State):
    title: str = ""
    description: str = ""
    company: str = ""

    def submit_job(self):
        # Here you would typically call an API to submit the job
        print(f"Submitting job: {self.title} at {self.company}")
        return rx.window_alert("Job submitted successfully!")

def job_form():
    return rx.vstack(
        rx.heading("Post a Job"),
        rx.input(placeholder="Job Title", on_change=JobFormState.set_title),
        rx.input(placeholder="Company", on_change=JobFormState.set_company),
        rx.text_area(placeholder="Job Description", on_change=JobFormState.set_description),
        rx.button("Submit Job", on_click=JobFormState.submit_job),
        width="100%",
        max_width="500px",
        spacing="1rem",
    )