from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dummy database
items = {"1": "Apple", "2": "Banana"}

class Item(BaseModel):
    item_name: str

@app.get("/items/{item_id}")
def get_item(item_id: str):
    return {"item_id": item_id, "item_name": items.get(item_id, "Not found")}

@app.post("/items/{item_id}")
def add_item(item_id: str, item: Item):
    items[item_id] = item.item_name
    return {"message": "Item added successfully", "item": items[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    if item_id in items:
        items[item_id] = item.item_name
        return {"message": "Item updated", "item": items[item_id]}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    return {"error": "Item not found"}

# PATCH - Update only a part of the item (Send JSON in the body)
@app.patch("/items/{item_id}")
def update_item_field(item_id: str, item: Item):
    if item_id in items:
        items[item_id] += " " + item.item_name  # Appending the new value
        return {"message": f"Updated item to {items[item_id]}"}
    return {"error": "Item not found"}
