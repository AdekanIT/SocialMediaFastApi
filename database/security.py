import jwt
from datetime import datetime, timedelta


SECRET_KEY = '9yBB9vn0jb82ib5sf9tf7C5UIvc67FF'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({'expire': expire.isoformat()})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
