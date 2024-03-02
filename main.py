from datetime import timedelta
from typing import Annotated

from fastapi import FastAPI, Depends, Security, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import requests

from settings import get_settings
from models import Token, TokenData
# from utils import *
from auth0.utils import VerifyToken
# from fake_user_db import fake_users_db

app = FastAPI(
    title="FastAPI - OAuth2 with Resource Owner Password Credentials Flow (Password Grant)",
    description="This is a test project to test OAuth2 with password grant flow using Auth0 as the OAuth2 provider.",
    version="1.0.2"
)

auth0 = VerifyToken()


@app.post("/auth0/token")
async def login_for_auth0_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    setting = get_settings()
    auth0_domain = setting.auth0_domain
    payload = {
        'grant_type': 'password',
        'username': form_data.username,
        'password': form_data.password,
        'audience': setting.auth0_identifier,
        'scope': '',
        'client_id': setting.auth0_client_id,
        'client_secret': setting.auth0_client_secret
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(f'https://{auth0_domain}/oauth/token', data=payload, headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json()
        )
    
    token = response.json()
    print(token)
    return Token(**token)

@app.get("/v1/protected")
async def read_protected(token: TokenData = Security(auth0.verify)):

    return token

# @app.get("/users/me/", response_model=User)
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_active_user)]
# ):
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)]
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]