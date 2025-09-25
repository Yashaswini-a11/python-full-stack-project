# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

#load environment variables
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase=create_client(url,key)

# create task
def create_users(username,email,password_hash):
    return supabase.table("users").insert({
        "username": username,
        "email": email,
        "password_hash": password_hash,
    }).execute()

#get all users
def get_all_users():
    return supabase.table("users").selete("*").order("created_at").execute()

#supabase user status
def update_user(user_id,password_hash):
    return supabase.table("users").update({"password_hash":password_hash}).eq("id",user_id).execute()

#delete user
def delete_user(user_id):
    return supabase.table("users").delete().eq("id",user_id).execute()

#create trip
def create_trip(user_id, trip_name):
    return supabase.table("trips").insert({
        "user_id": user_id,
        "trip_name": trip_name,
    }).execute()

#get all trips
def get_trips_by_user(user_id):
    return supabase.table("trips").select("*").eq("user_id", user_id).order("created_at").execute()

#update trip name
def update_trip_name(trip_id, trip_name):
    return supabase.table("trips").update({"trip_name": trip_name}).eq("trip_id", trip_id).execute()

#delete trip
def delete_trip(trip_id):
    return supabase.table("trips").delete().eq("trip_id", trip_id).execute()

#create trip stop
def create_trip_stop(trip_id, stop_order, location_name, distance_to_next_km=None, duration_to_next_min=None, transport_mode_to_next=None):
    return supabase.table("trip_stops").insert({
        "trip_id": trip_id,
        "stop_order": stop_order,
        "location_name": location_name,
        "distance_to_next_km": distance_to_next_km,
        "duration_to_next_min": duration_to_next_min,
        "transport_mode_to_next": transport_mode_to_next,
    }).execute()

#get all trip_stops
def get_trip_stops(trip_id):
    return supabase.table("trip_stops").select("*").eq("trip_id", trip_id).order("stop_order").execute()

#update trip stops
def update_trip_stop(stop_id, **kwargs):
    return supabase.table("trip_stops").update(kwargs).eq("stop_id", stop_id).execute()

#delete trip stops
def delete_trip_stop(stop_id):
    return supabase.table("trip_stops").delete().eq("stop_id", stop_id).execute()

