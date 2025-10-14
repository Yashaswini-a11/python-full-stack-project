from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from src.logic import Users, Trip, Trip_stops

# Initialize logic classes
users_logic = Users()
trips_logic = Trip()
trip_stops_logic = Trip_stops()

app = FastAPI(title="Route Optimizer API")

# ========= CORS =========
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========= Pydantic MODELS =========
class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str
    created_at: Optional[str] = None

class TripCreate(BaseModel):
    user_id: int
    trip_name: str
    created_at: Optional[str] = None

class TripStopCreate(BaseModel):
    trip_id: int
    stop_order: int
    location_name: str
    distance_to_next_km: Optional[float] = None
    duration_to_next_min: Optional[float] = None
    transport_mode_to_next: Optional[str] = None


# ========= ROOT =========
@app.get("/")
def home():
    return {"message": "✅ Route Optimizer API is running!"}


# ========= USERS =========
@app.post("/users")
def create_user(user: UserCreate):
    result = users_logic.add_user(user.username, user.email, user.password_hash, user.created_at)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.get("/users")
def get_users():
    return users_logic.get_users()

@app.put("/users/{user_id}")
def update_user(user_id: int, password_hash: str):
    result = users_logic.update_user(user_id, password_hash)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    result = users_logic.delete_user(user_id)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result


# ========= TRIPS =========
@app.post("/trips")
def create_trip(trip: TripCreate):
    result = trips_logic.add_trip(trip.user_id, trip.trip_name, trip.created_at)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.get("/trips/{user_id}")
def get_trips(user_id: int):
    return trips_logic.get_trips(user_id)

@app.put("/trips/{trip_id}")
def update_trip(trip_id: int, trip_name: str):
    result = trips_logic.update_trip(trip_id, trip_name)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.delete("/trips/{trip_id}")
def delete_trip(trip_id: int):
    result = trips_logic.delete_trip(trip_id)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result


# ========= TRIP STOPS =========
@app.post("/trip_stops")
def create_trip_stop(stop: TripStopCreate):
    result = trip_stops_logic.add_trip_stop(
        stop.trip_id,
        stop.stop_order,
        stop.location_name,
        stop.distance_to_next_km,
        stop.duration_to_next_min,
        stop.transport_mode_to_next
    )
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.get("/trip_stops/{trip_id}")
def get_trip_stops(trip_id: int):
    return trip_stops_logic.get_trip_stops(trip_id)

@app.put("/trip_stops/{stop_id}")
def update_trip_stop(
    stop_id: int,
    stop_order: Optional[int] = None,
    location_name: Optional[str] = None,
    distance_to_next_km: Optional[float] = None,
    duration_to_next_min: Optional[float] = None,
    transport_mode_to_next: Optional[str] = None,
):
    result = trip_stops_logic.update_trip_stop(
        stop_id,
        stop_order=stop_order,
        location_name=location_name,
        distance_to_next_km=distance_to_next_km,
        duration_to_next_min=duration_to_next_min,
        transport_mode_to_next=transport_mode_to_next
    )
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.delete("/trip_stops/{stop_id}")
def delete_trip_stop(stop_id: int):
    result = trip_stops_logic.delete_trip_stop(stop_id)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result


# ========= DEV =========
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
