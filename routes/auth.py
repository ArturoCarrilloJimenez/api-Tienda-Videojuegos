from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from utils.fuction_jwt import get_current_user, validate_token, write_token
from fastapi.responses import JSONResponse
from starlette import status

from models.Usuarios import UsuarioPy, UsuarioDB
from configs.db import get_db
from utils.hash import verify_password

auth_routes = APIRouter(tags=['Autenticación'])


# Generate jwt 
@auth_routes.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(user: UsuarioPy, db: Session = Depends(get_db)):
    result: UsuarioDB = db.query(UsuarioDB).filter(UsuarioDB.username == user.username).first()
    if result and verify_password(user.password,result.password):
        userPy: UsuarioPy = UsuarioPy(id = result.id, username = result.username)

        if result.admin:
            role = 'admin'
        else:
            role = 'user'
            
        return write_token(userPy.dict(), role)
    else:
        return JSONResponse(content={"detail": "User not found"}, status_code=404)


# Verifico el token creado anteriormente
@auth_routes.post("/verify/token", status_code=status.HTTP_202_ACCEPTED)
def verify_token(Authorization: str = Header(None)) :
    if Authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='No has pasado el token')
    token = Authorization.split(" ")[1]
    return validate_token(token)
    