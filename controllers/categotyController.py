from sqlalchemy.orm import Session
from models.Categorias import CategoriaPy, CategoriasDB

def getCategories(db: Session) -> list[CategoriaPy] :
    return db.query(CategoriasDB).all()

def getOneCategory(id: int, db: Session) :
    return db.query(CategoriasDB).filter(CategoriasDB.id == id).first()

def addCategory(category: CategoriaPy, db: Session) -> None :
    newCategory = CategoriasDB(name=category.name)
    db.add(newCategory)
    db.commit()
    db.refresh(newCategory)

def deleteCategory(id: int, db: Session) :
    category = getOneCategory(id, db)
    if category:
        db.delete(category)
        db.commit()
        return True
    return False

def modifyCategory(id: int, db: Session, updateCategory: CategoriaPy) :
    category = getOneCategory(id, db)
    if category:
        category.name = updateCategory.name
        db.commit()
        db.refresh(category)
        return True
    return False