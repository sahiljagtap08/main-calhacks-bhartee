import reflex as rx

def clerk_script():
    return rx.script(src="https://cdn.jsdelivr.net/npm/@clerk/clerk-js@latest/dist/clerk.browser.js")

def clerk_sign_in(routing="/sign-in"):
    return rx.vstack(
        clerk_script(),
        rx.script(f"""
        const clerk = window.Clerk;
        clerk.load().then(() => {{
            const signInDiv = document.getElementById('sign-in');
            clerk.mountSignIn(signInDiv, {{routing: "{routing}"}});
        }});
        """),
        rx.div(id="sign-in")
    )

def clerk_sign_up(routing="/sign-up"):
    return rx.vstack(
        clerk_script(),
        rx.script(f"""
        const clerk = window.Clerk;
        clerk.load().then(() => {{
            const signUpDiv = document.getElementById('sign-up');
            clerk.mountSignUp(signUpDiv, {{routing: "{routing}"}});
        }});
        """),
        rx.div(id="sign-up")
    )

def user_button():
    return rx.vstack(
        clerk_script(),
        rx.script("""
        const clerk = window.Clerk;
        clerk.load().then(() => {
            const userButtonDiv = document.getElementById('user-button');
            clerk.mountUserButton(userButtonDiv);
        });
        """),
        rx.div(id="user-button")
    )