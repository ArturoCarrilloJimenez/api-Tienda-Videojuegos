from passlib.context import CryptContext 

# Configuro la función de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# encripto texto
def hashing (text: str) -> str :
    return pwd_context.hash(text)

# valido el texto, plain_password es la contraseña sin hash y hashed_password es ya hecho el hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)