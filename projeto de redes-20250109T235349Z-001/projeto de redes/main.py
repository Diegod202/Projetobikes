from typing import List

from fastapi import FastAPI, Form, HTTPException, Query

app = FastAPI()

# In-memory storage for bikes
bikes = []

@app.get("/bikes")
async def list_bikes():
    """
    Retrieve the list of bikes.
    """
    return {
        "status": "success",
        "message": "Bikes retrieved successfully.",
        "data": bikes
    }

@app.get("/bikes/{bike_id}")
async def get_bike_by_id(bike_id: int):
    """
    Retrieve a bike by its ID.
    """
    for bike in bikes:
        if bike["id"] == bike_id:
            return {
                "status": "success",
                "message": "Bike retrieved successfully.",
                "data": bike
            }
    raise HTTPException(status_code=404, detail="Bike not found.")

@app.get("/bikes_search")
async def search_bikes_by_name(name: str = Query(...)):
    """
    Search bikes by name.
    """
    matching_bikes = [bike for bike in bikes if name.lower() in bike["name"].lower()]
    if matching_bikes:
        return {
            "status": "success",
            "message": "Bikes retrieved successfully.",
            "data": matching_bikes
        }
    raise HTTPException(status_code=404, detail="No bikes found with the given name.")

@app.post("/bikes")
async def create_bike(
    name: str = Form(...),
    brand: str = Form(...),
    price: float = Form(...),
    type: str = Form(...),
    description: str = Form(...)
):
    """
    Add a new bike to the list.
    """
    bike = {
        "id": len(bikes) + 1,  # Generate a simple ID
        "name": name,
        "brand": brand,
        "price": price,
        "type": type,
        "description": description
    }
    bikes.append(bike)
    return {
        "status": "success",
        "message": "Bike added successfully.",
        "data": bike
    }

@app.put("/bikes/{bike_id}")
async def update_bike(
    bike_id: int,
    name: str = Form(...),
    brand: str = Form(...),
    price: float = Form(...),
    type: str = Form(...),
    description: str = Form(...)
):
    """
    Update a bike's details by its ID.
    """
    for bike in bikes:
        if bike["id"] == bike_id:
            bike.update({"name": name, "brand": brand, "price": price, "type": type, "description": description})
            return {
                "status": "success",
                "message": "Bike updated successfully.",
                "data": bike
            }
    raise HTTPException(status_code=404, detail="Bike not found.")

@app.delete("/bikes")
async def delete_bike(bike_id: int):
    """
    Delete a bike by its ID.
    """
    for index, bike in enumerate(bikes):
        if bike["id"] == bike_id:
            deleted_bike = bikes.pop(index)
            return {
                "status": "success",
                "message": "Bike deleted successfully.",
                "data": deleted_bike
            }
    raise HTTPException(status_code=404, detail="Bike not found.")