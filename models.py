from typing import Union
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    scope: Union[str, None] = None
    expires_in: Union[int, None] = None

class TokenData(BaseModel):
    iss: str
    sub: str
    aud: str
    iat: int
    exp: int
    azp: str
    gty: str