from sqlalchemy.orm import Session
from models.Usuarios import UsuarioPy, UsuarioDB
from utils.hash import hashing

def getUsuario(db: Session) -> list[UsuarioDB] :
    return db.query(UsuarioDB).all()

def getOneUsuario(id: int, db: Session) :
    return db.query(UsuarioDB).filter(UsuarioDB.id == id).first()

def addUsuario(user: UsuarioPy, db: Session) -> None :
    newUsuario = UsuarioDB(username = user.username, password = hashing(user.password), name = user.name, admin = False)
    db.add(newUsuario)
    db.commit()
    db.refresh(newUsuario)

def addAdminUsuario(user: UsuarioPy, db: Session) -> None :
    newUsuario = UsuarioDB(id=user.id,username = user.username, password = hashing(user.password), name = user.name, admin = True)
    db.add(newUsuario)
    db.commit()
    db.refresh(newUsuario)

def deleteUsuario(id: int, db: Session) :
    usuario = getOneUsuario(id, db)
    if usuario:
        db.delete(usuario)
        db.commit()
        return True
    return False

def modifyUsuario(id: int, db: Session, updateUser: UsuarioPy) :
    user = getOneUsuario(id, db)
    if user:
        user.username = updateUser.username
        user.password = hashing(updateUser.password)
        user.name = updateUser.name
        db.commit()
        db.refresh(user)
        return True
    return False

def isAdmin(id: int, db: Session) :
    return db.query(UsuarioDB).filter(UsuarioDB.id == id).first().admin