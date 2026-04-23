from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    category: str
    price: float
    in_stock: bool

class ItemCreate(BaseModel):
    name: str
    category: str
    price: float
    in_stock: bool

items: List[Item] = []
next_id = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items", response_model=List[Item])
def list_items(category: Optional[str] = None, in_stock: Optional[bool] = None):
    results = items
    if category is not None:
        results = [item for item in results if item.category == category]
    if in_stock is not None:
        results = [item for item in results if item.in_stock == in_stock]
    return results

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item)
def create_item(item_create: ItemCreate):
    global next_id
    item = Item(id=next_id, **item_create.dict())
    items.append(item)
    next_id += 1
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemCreate):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated_item = Item(id=item_id, **item_update.dict())
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
