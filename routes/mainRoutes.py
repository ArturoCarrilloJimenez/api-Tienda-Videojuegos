from fastapi import APIRouter
from starlette import status

mainRoutes = APIRouter()

@mainRoutes.get('/', status_code=status.HTTP_200_OK)
def welcome() :
    return {'Saludos': 'Bienvenido a la api de videojuegos'}
