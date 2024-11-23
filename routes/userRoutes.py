from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from configs.db import get_db

from models.Usuarios import UsuarioPy
from controllers.userController import getUsuario, getOneUsuario, addUsuario, deleteUsuario, modifyUsuario
from utils.fuction_jwt import get_current_user

userRouter = APIRouter(tags=['Usuarios'], prefix='/users')

# Admin
@userRouter.get('/all', status_code=status.HTTP_200_OK, response_model=list[UsuarioPy])
def sow_Users(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access forbidden')
    return getUsuario(db)

# Login
@userRouter.get('/{id}', status_code=status.HTTP_200_OK, response_model=UsuarioPy)
def sow_One_Usuario(id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    category = getOneUsuario(id, db)
    if category:
        return category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra el usuario')


# TODO validar que los campos unique no estén ya en la bd
# Invitado
@userRouter.post('/add', status_code=status.HTTP_201_CREATED, response_model=list[UsuarioPy])
def add_New_Usuario(usuario: UsuarioPy, db: Session = Depends(get_db)) :
    addUsuario(usuario, db)
    return getUsuario(db)

# Admin
@userRouter.delete('/delete/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=dict[str, str])
def del_Usuario(id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access forbidden')
    if deleteUsuario(id, db) :
        return {'detail': 'Usuario eliminada'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se ha encontrado el usuario')


# Login
@userRouter.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=dict[str, str])
def update_User(id: int, user: UsuarioPy, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if modifyUsuario(id, db, user) :
        return {'detail': 'Usuario actualizada'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra el usuario')