from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    auth0_domain: str
    auth0_client_id: str
    auth0_client_secret: str
    auth0_identifier: str
    auth0_algorithms: str
    auth0_issuer: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()