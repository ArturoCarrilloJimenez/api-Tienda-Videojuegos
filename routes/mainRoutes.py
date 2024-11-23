from fastapi import APIRouter
from starlette import status

mainRoutes = APIRouter(tags=['Pruebas'])

@mainRoutes.get('/', status_code=status.HTTP_200_OK)
def welcome() :
    return {'Saludos': 'Bienvenido a la api de videojuegos'}
