import reflex as rx

config = rx.Config(
    app_name="bharteeai",
    api_url="https://prototype.bhartee.ai",
    db_url="sqlite:///production.db",
    env=rx.Env.PROD,
)