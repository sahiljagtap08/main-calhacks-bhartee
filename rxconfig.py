import reflex as rx

config = rx.Config(
    app_name="bharteeai",
    db_url="sahil-93cc5:fEzPgK4gGQqG2CbPP8PxtvBNbIgRoR9A@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333",
    api_url="https://prototype.bhartee.ai",  # Update this with your actual domain
    env=rx.Env.PROD,
)