from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from configs.db import get_db
from controllers.categotyController import getCategories, getOneCategory, addCategory, deleteCategory, modifyCategory

from models.Categorias import CategoriaPy

categoryRoutes = APIRouter(tags=['Categorías'], prefix='/category')

@categoryRoutes.get('/all', status_code=status.HTTP_200_OK, response_model=list[CategoriaPy])
def sow_Categories(db: Session = Depends(get_db)) :
    return getCategories(db)

@categoryRoutes.get('/{id}', status_code=status.HTTP_200_OK, response_model=CategoriaPy)
def sow_One_Category(id: int, db: Session = Depends(get_db)) :
    category = getOneCategory(id, db)
    if category:
        return category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra la categoría')

# TODO validar que los campos unique no esten ya en la bd
@categoryRoutes.post('/add', status_code=status.HTTP_201_CREATED, response_model=list[CategoriaPy])
def add_New_Category(category: CategoriaPy, db: Session = Depends(get_db)) :
    addCategory(category, db)
    return getCategories(db)

@categoryRoutes.delete('/delete/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=dict[str, str])
def del_Category(id: int, db: Session = Depends(get_db)) :
    if deleteCategory(id, db) :
        return {'detail': 'Categoría eliminada'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se ha encontrado la categoría')

@categoryRoutes.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=dict[str, str])
def update_Category(id: int, category: CategoriaPy, db: Session = Depends(get_db)) :
    if modifyCategory(id, db, category) :
        return {'detail': 'Categoría actualizada'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra la categoría')