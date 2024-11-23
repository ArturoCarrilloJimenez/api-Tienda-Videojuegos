from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from configs.db import get_db
from controllers.categotyController import getCategories, getOneCategory, addCategory, deleteCategory, modifyCategory

from models.Categorias import CategoriaPy
from utils.fuction_jwt import get_current_user

categoryRoutes = APIRouter(tags=['Categorías'], prefix='/category')


# Todos
@categoryRoutes.get('/all', status_code=status.HTTP_200_OK, response_model=list[CategoriaPy])
def sow_Categories(db: Session = Depends(get_db)) :
    return getCategories(db)


# Todos
@categoryRoutes.get('/{id}', status_code=status.HTTP_200_OK, response_model=CategoriaPy)
def sow_One_Category(id: int, db: Session = Depends(get_db)) :
    category = getOneCategory(id, db)
    if category:
        return category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra la categoría')


# TODO validar que los campos unique no esten ya en la bd
# Admin
@categoryRoutes.post('/add', status_code=status.HTTP_201_CREATED, response_model=list[CategoriaPy])
def add_New_Category(category: CategoriaPy, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access forbidden')
    addCategory(category, db)
    return getCategories(db)

# Admin
@categoryRoutes.delete('/delete/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=dict[str, str])
def del_Category(id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access forbidden')
    if deleteCategory(id, db) :
        return {'detail': 'Categoría eliminada'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se ha encontrado la categoría')

# Admin
@categoryRoutes.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=dict[str, str])
def update_Category(id: int, category: CategoriaPy, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access forbidden')
    if modifyCategory(id, db, category) :
        return {'detail': 'Categoría actualizada'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra la categoría')