from sqlalchemy import Boolean, Column, Integer, String, Float, Text

from database import Base, SessionLocal


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text)
    price = Column(Float)
    on_offer = Column(Boolean, default=False)
    
    def __repr__(self):
        return f" {self.name}"

    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
