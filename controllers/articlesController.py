from sqlalchemy.orm import Session
from models.Articulos import ArticulosPy, ArticulosDB
from models.Categorias import CategoriasDB

def getArticles(db: Session) -> list[ArticulosPy] :
    return db.query(ArticulosDB).all()

def getOneArticles(id: int, db: Session) :
    return db.query(ArticulosDB).filter(ArticulosDB.id == id).first()

def getArticleByCategory(nameCat: str, db: Session):
    return db.query(ArticulosDB).join(CategoriasDB).filter(CategoriasDB.name == nameCat).all()

def addArticle(article: ArticulosPy, db: Session) -> None :
    newArticle = ArticulosDB(name=article.name,price=article.price,tax=article.tax,description=article.description,image=article.image,stock=article.stock,idCategory=article.idCategory)
    db.add(newArticle)
    db.commit()
    db.refresh(newArticle)

def deleteArticle(id: int, db: Session) :
    article = getOneArticles(id, db)
    if article:
        db.delete(article)
        db.commit()
        return True
    return False

def modifyArticles(id: int, db: Session, updateCategory: ArticulosPy) :
    article = getOneArticles(id, db)
    if article:
        article.name = updateCategory.name
        article.price = updateCategory.price
        article.tax = updateCategory.tax
        article.description = updateCategory.description
        article.image = updateCategory.image
        article.stock = updateCategory.stock
        article.idCategory = updateCategory.idCategory
        db.commit()
        db.refresh(article)
        return True
    return False