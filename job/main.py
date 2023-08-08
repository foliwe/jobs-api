from typing import List
from fastapi import FastAPI, Depends
from . import schemas,models
from sqlalchemy.orm import Session
from . database import SessionLocal, engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/job')
async def create_job(request: schemas.JobBase, db: Session = Depends(get_db)):
    new_job = models.Job(**request.model_dump())
    db.add(new_job)
    db.commit()
    db.refresh
    return new_job

@app.get("/jobs")
def get_all_jobs(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()
    return {'jobs': jobs}


@app.get("/job/{id}")
def show_job(id, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == id).first()
    return {'job': job}
    
# @app.post("/item")
# def creat_item():
#     pass

# @app.get("/item/{item_id}")
# def get_item(item_id:int):
#     pass

# @app.put("/item/{item_id}")
# def update_item(item_id:int):
#     pass


# @app.delete("/item/{item_id}")
# async def delete_item(item_id:int):
#     pass

