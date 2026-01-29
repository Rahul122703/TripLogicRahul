from fastapi import APIRouter, HTTPException, Request, status
from app.schemas.user import MagicLinkRequest, VerifyRequest, TokenResponse
from app.services.stytch_service import send_magic_link, authenticate_magic_token
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/magic-link")
def post_magic_link(payload: MagicLinkRequest):
    try:
        send_magic_link(
            email=payload.email,
            expiration_minutes=20
        )

        # Always return generic success to avoid user enumeration
        return {"message": "Magic link sent (if email exists)."}

    except Exception as e:
        print("Stytch error:", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to send magic link"
        )


@router.post("/verify", response_model=TokenResponse)
def verify_magic_link(request: Request, payload: VerifyRequest):
    ip = request.client.host if request.client else None
    ua = request.headers.get("user-agent")

    try:
        resp = authenticate_magic_token(
            token=payload.token,
            ip_address=ip,
            user_agent=ua
        )

        # Safely extract user_id from Stytch response
        user_id = None

        if hasattr(resp, "user_id") and resp.user_id:
            user_id = resp.user_id
        elif hasattr(resp, "user") and hasattr(resp.user, "user_id"):
            user_id = resp.user.user_id

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        # Issue your own JWT for the app
        access_token = create_access_token(subject=user_id)

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except Exception as e:
        print("Verify error:", e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalid or expired"
        )
