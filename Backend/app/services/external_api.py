import requests as rq
from stytch import B2BClient

from app.core.config import settings


environment = (
    "live"
    if settings.PRODUCTION == "1"
    and settings.STAGING != "1"
    and settings.PYCHARM_HOSTED != "1"
    else "test"
)


class ExternalAPI:
    def __init__(self):
        self.client = B2BClient(
            project_id=settings.TRIPLOGIC_STYTCH_PROJECTID,
            secret=settings.TRIPLOGIC_STYTCH_SECRET,
            environment=environment,
        )
        self.token = None
        self.url = "https://triplogicapi-test-7c6a378ff18c.herokuapp.com/"

    def access_token(self):
        try:
            self.client.m2m.authenticate_token(self.token)
            return self.token
        except:
            auth = self.client.m2m.token(
                client_id=settings.TRIPLOGIC_STYTCH_CLIENTID,
                client_secret=settings.TRIPLOGIC_STYTCH_CLIENTSECRET,
            )
            self.token = auth.access_token
            return self.token

    def headers(self):
        return {
            "Authorization": f"Bearer {self.access_token()}",
            "Content-Type": "application/json",
        }

    def get(self, endpoint: str):
        r = rq.get(self.url + endpoint, headers=self.headers())
        r.raise_for_status()
        return r.json()

    def post(self, endpoint: str, data: dict):
        r = rq.post(self.url + endpoint, headers=self.headers(), json=data)
        r.raise_for_status()
        return r.json()
