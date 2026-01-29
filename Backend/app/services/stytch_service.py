import stytch
from stytch.core.response_base import StytchError
from app.core.config import settings

# Use Client for B2C flows; B2B vs B2C depends on your Stytch product.
client = stytch.Client(
    project_id=settings.STYTCH_PROJECT_ID,
    secret=settings.STYTCH_SECRET,
    environment=settings.ENVIRONMENT  # 'test' or 'live'
)

def send_magic_link(email: str, redirect_url: str | None = None, expiration_minutes: int = 20):
    """
    Sends a login_or_create magic link to email. Expires in expiration_minutes.
    """
    try:
        resp = client.magic_links.email.login_or_create(
            email=email,
            login_magic_link_url=redirect_url or settings.FRONTEND_CALLBACK_URL,
            signup_magic_link_url=redirect_url or settings.FRONTEND_CALLBACK_URL,
            login_expiration_minutes=expiration_minutes
        )
        return resp
    except StytchError as e:
        raise

def authenticate_magic_token(token: str, ip_address: str | None = None, user_agent: str | None = None):
    """
    Authenticates the magic link token returned by Stytch (one-time token).
    Returns the Stytch response (user_id, session info if requested).
    """
    try:
        resp = client.magic_links.authenticate(
            token=token,
            attributes={
                "ip_address": ip_address,
                "user_agent": user_agent
            }
        )
        return resp
    except StytchError as e:
        raise
