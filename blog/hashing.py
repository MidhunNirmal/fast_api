from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated = "auto")

class hash():
    def hashing(password):
        return pwd_cxt.hash(password)
    def verify(hashed_pass,plain_pass):
        return pwd_cxt.verify(plain_pass,hashed_pass)