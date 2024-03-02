
from typing import Annotated, Optional
import requests

from models import Token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from settings import get_settings
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth0/token")

class UnauthorizedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        """Returns HTTP 403"""
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)

class UnauthenticatedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
        )

class VerifyToken:
    """Does all the token verification using PyJWT"""

    def __init__(self):
        self.config = get_settings()

    def verify(self, token: Annotated[str, Depends(oauth2_scheme)]):
        print('access_token:', token)
        url = f'https://{self.config.auth0_domain}/.well-known/jwks.json'
        jwks_response = requests.get(url)
        jwks = jwks_response.json()

        if token is None:
            raise UnauthenticatedException

        rsa_key = {}
        for key in jwks['keys']:
            if key['kid'] == jwt.get_unverified_header(token)['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }

        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=[self.config.auth0_algorithms],
                audience=self.config.auth0_identifier,
                issuer=self.config.auth0_issuer
            )
            
            return payload
        except jwt.ExpiredSignatureError:
            raise UnauthorizedException("Token has expired")
        except jwt.JWTClaimsError:
            raise UnauthorizedException("Invalid claims")
        except Exception as e:
            raise UnauthorizedException("Unable to parse authentication token")
