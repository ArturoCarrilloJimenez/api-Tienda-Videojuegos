from configs.db import SessionLocal
import controllers.userController as ctrl
from models.Usuarios import UsuarioPy

if __name__ == '__main__' :
    username = input('Introduce el nombre de usuario ')
    password = input('Introduce una contraseña ')

    ctrl.deleteUsuario(0, SessionLocal())
    ctrl.addAdminUsuario(UsuarioPy(id=0, username=username, password=password, name='admin'), SessionLocal())