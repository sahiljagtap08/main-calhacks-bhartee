import reflex as rx

def interview_results(results: dict):
    return rx.vstack(
        rx.heading("Interview Results"),
        rx.text(f"Overall Score: {results.get('overall_score', 'N/A')}"),
        rx.text(f"Technical Skills: {results.get('technical_skills', 'N/A')}"),
        rx.text(f"Communication Skills: {results.get('communication_skills', 'N/A')}"),
        rx.text(f"Problem Solving: {results.get('problem_solving', 'N/A')}"),
        rx.text(f"Cultural Fit: {results.get('cultural_fit', 'N/A')}"),
        rx.heading("Strengths", size="md"),
        rx.unordered_list([rx.list_item(s) for s in results.get('strengths', [])]),
        rx.heading("Areas for Improvement", size="md"),
        rx.unordered_list([rx.list_item(a) for a in results.get('areas_for_improvement', [])]),
        rx.text(f"Recommendation: {results.get('recommendation', 'N/A')}"),
        width="100%",
        max_width="800px",
        spacing="1rem",
        padding="2rem",
        border="1px solid #E2E8F0",
        border_radius="md",
    )