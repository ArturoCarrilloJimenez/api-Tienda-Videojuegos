from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from configs.db import get_db

from models.Carrito import CarritoPy, CarritoDB
from utils.fuction_jwt import get_current_user

carritoRouter = APIRouter(tags=['Carrito'], prefix='/card')


# Login
@carritoRouter.get('/all', status_code=status.HTTP_200_OK, response_model=list[CarritoPy])
def sow_Carrito(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    userId = current_user.get("id")
    return db.query(CarritoDB).filter(CarritoDB.id_user == userId).all()


# TODO validar que los campos unique no estén ya en la bd
# Login
@carritoRouter.post('/add', status_code=status.HTTP_201_CREATED, response_model=CarritoPy)
def add_New_Carrito(carrito: CarritoPy, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    newCard = CarritoDB(id_user = current_user.get("id"), id_article = carrito.id_article, cantidad = carrito.cantidad)
    db.add(newCard)
    db.commit()
    db.refresh(newCard)
    return newCard


# Login
@carritoRouter.delete('/delete/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=CarritoPy)
def del_Usuario(id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    carrito = db.query(CarritoDB).filter(CarritoDB.id_article == id, CarritoDB.id_user == current_user.get('id')).first()
    if carrito:
        db.delete(carrito)
        db.commit()
        return carrito
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se ha encontrado el registro')


# Login
@carritoRouter.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=CarritoPy)
def update_User(id: int, carrito: CarritoPy, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    updateCarrito = db.query(CarritoDB).filter(CarritoDB.id_article == id, CarritoDB.id_user == current_user.get('id')).first()
    if updateCarrito:
        updateCarrito.cantidad = carrito.cantidad
        db.commit()
        db.refresh(updateCarrito)
        return updateCarrito
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encuentra el usuario')


@carritoRouter.get('/buy', status_code=status.HTTP_202_ACCEPTED, response_model=list[CarritoPy])
def comprar(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) :
    userId = current_user.get("id")
    registros = db.query(CarritoDB).filter(CarritoDB.id_user == userId).all()
    if registros :
        for registro in registros:
            db.delete(registro)
        db.commit()
        return registros
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error al realizar el pedido')