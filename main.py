
from fastapi import FastAPI
# from . import schemas
from pydantic import BaseModel

app = FastAPI()




class Item(BaseModel):
    id:int
    name: str
    description: str
    price: float
    on_offer: bool

@app.put("/item/{item_id}")
async def update_item(item_id:int, item:Item):
    return {'name':item.name,
            'description': item.description,
            'price': item.price,
            'on_offer': item.on_offer
            }

 
