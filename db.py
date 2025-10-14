# db.py
import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# ========== USERS ==========

def create_user(username, email, password_hash, created_at=None):
    return supabase.table("users").insert({
        "username": username,
        "email": email,
        "password_hash": password_hash,
        "created_at": created_at
    }).execute()

# Get all users
def get_all_users():
    return supabase.table("users").select("*").order("created_at", desc=False).execute()

def update_user(user_id, password_hash):
    return supabase.table("users").update({
        "password_hash": password_hash
    }).eq("user_id", user_id).execute()

# Delete user
def delete_user(user_id):
    return supabase.table("users").delete().eq("user_id", user_id).execute()

# ========== TRIPS ==========

def create_trip(user_id, trip_name, created_at=None):
    return supabase.table("trips").insert({
        "user_id": user_id,
        "trip_name": trip_name,
        "created_at": created_at
    }).execute()

# Get all trips for a user
def get_trips_by_user(user_id):
    return supabase.table("trips").select("*").eq("user_id", user_id).order("created_at", desc=False).execute()

# Update trip name
def update_trip_name(trip_id, trip_name):
    return supabase.table("trips").update({
        "trip_name": trip_name
    }).eq("trip_id", trip_id).execute()

# Delete trip
def delete_trip(trip_id):
    return supabase.table("trips").delete().eq("trip_id", trip_id).execute()

# ========== TRIP STOPS ==========

def create_trip_stop(trip_id, stop_order, location_name, distance_to_next_km=None, duration_to_next_min=None, transport_mode_to_next=None):
    return supabase.table("trip_stops").insert({
        "trip_id": trip_id,
        "stop_order": stop_order,
        "location_name": location_name,
        "distance_to_next_km": distance_to_next_km,
        "duration_to_next_min": duration_to_next_min,
        "transport_mode_to_next": transport_mode_to_next,
    }).execute()

# Get all trip stops for a trip
def get_trip_stops(trip_id):
    return supabase.table("trip_stops").select("*").eq("trip_id", trip_id).order("stop_order", desc=False).execute()

# Update trip stop
def update_trip_stop(stop_id, **kwargs):
    return supabase.table("trip_stops").update(kwargs).eq("stop_id", stop_id).execute()

# Delete trip stop
def delete_trip_stop(stop_id):
    return supabase.table("trip_stops").delete().eq("stop_id", stop_id).execute()
