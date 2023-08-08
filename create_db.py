from database import Base, engine
import models

print("Creating databases ....")
models.Base.metadata.create_all(bind=engine)