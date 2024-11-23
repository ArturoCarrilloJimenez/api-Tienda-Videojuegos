from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Articulos,Carrito,Categorias,Usuarios
from routes.mainRoutes import mainRoutes
from routes.categoryRoutes import categoryRoutes
from routes.articulosRoutes import articlesRoutes
from routes.auth import auth_routes
from routes.userRoutes import userRouter
from routes.carritoRoutes import carritoRouter

from configs.db import engine

app = FastAPI(title='Api tienda videojuegos', version='1.0')

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mainRoutes, prefix='/api')
app.include_router(categoryRoutes, prefix='/api')
app.include_router(articlesRoutes, prefix='/api')
app.include_router(userRouter, prefix='/api')
app.include_router(carritoRouter, prefix='/api')
app.include_router(auth_routes, prefix='/api')

# Creación del modelo
Articulos.Base.metadata.create_all(bind=engine)
Categorias.Base.metadata.create_all(bind=engine)
Usuarios.Base.metadata.create_all(bind=engine)
Carrito.Base.metadata.create_all(bind=engine)

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run(app = 'main:app', host='0.0.0.0', port=8000, reload = True)