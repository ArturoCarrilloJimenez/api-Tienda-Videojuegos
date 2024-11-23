from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from configs.db import get_db

from models.Articulos import ArticulosPy
from controllers.articlesController import getArticles, getOneArticles, getArticleByCategory, addArticle, deleteArticle, modifyArticles
from utils.fuction_jwt import get_current_user

articlesRoutes = APIRouter(tags=['Artículos'], prefix='/articles')

# Todos
@articlesRoutes.get('/all', status_code=status.HTTP_200_OK, response_model=list[ArticulosPy])
def sow_Articles(db: Session = Depends(get_db)) :
    return getArticles(db)


# Todos
@articlesRoutes.get('/{id}', status_code=status.HTTP_200_OK, response_model=ArticulosPy)
def sow_One_Article(id: int, db: Session = Depends(get_db)) :
    category = getOneArticles(id, db)
    if category:
        return category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra el articulo')


# Todos
@articlesRoutes.get('/categoria/{name}', status_code=status.HTTP_200_OK, response_model=list[ArticulosPy])
def sow_articles_by_category(name: str, db: Session = Depends(get_db)) :
    return getArticleByCategory(name, db)

# TODO validar que los campos unique no esten ya en la bd
# Admin
@articlesRoutes.post('/add', status_code=status.HTTP_201_CREATED, response_model=list[ArticulosPy])
def add_New_Article(article: ArticulosPy, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access forbidden')
    addArticle(article, db)
    return getArticles(db)


# Admin
@articlesRoutes.delete('/delete/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=dict[str, str])
def del_Article(id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access forbidden')
    if deleteArticle(id, db) :
        return {'detail': 'Articulo eliminada'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se ha encontrado la categoría')

# Admin
@articlesRoutes.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=dict[str, str])
def update_Article(id: int, article: ArticulosPy, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access forbidden')
    if modifyArticles(id, db, article) :
        return {'detail': 'Articulo actualizada'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra el articulo')