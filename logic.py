import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing SUPABASE_URL or SUPABASE_KEY in .env file")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# ================= USERS =================
class Users:
    def add_user(self, username, email, password_hash, created_at=None):
        data = {
            "username": username,
            "email": email,
            "password_hash": password_hash,
            "created_at": created_at,
        }
        try:
            result = supabase.table("users").insert(data).execute()
            return {"Success": True, "Message": "User added!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def get_users(self):
        try:
            result = supabase.table("users").select("*").execute()
            return {"Success": True, "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def update_user(self, user_id, password_hash):
        try:
            result = supabase.table("users").update({"password_hash": password_hash}).eq("user_id", user_id).execute()
            return {"Success": True, "Message": "User updated!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def delete_user(self, user_id):
        try:
            result = supabase.table("users").delete().eq("user_id", user_id).execute()
            return {"Success": True, "Message": "User deleted!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}


# ================= TRIPS =================
class Trip:
    def add_trip(self, user_id, trip_name, created_at=None):
        data = {
            "user_id": user_id,
            "trip_name": trip_name,
            "created_at": created_at,
        }
        try:
            result = supabase.table("trips").insert(data).execute()
            return {"Success": True, "Message": "Trip added!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def get_trips(self, user_id):
        try:
            result = supabase.table("trips").select("*").eq("user_id", user_id).execute()
            return {"Success": True, "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def update_trip(self, trip_id, trip_name):
        try:
            result = supabase.table("trips").update({"trip_name": trip_name}).eq("trip_id", trip_id).execute()
            return {"Success": True, "Message": "Trip updated!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def delete_trip(self, trip_id):
        try:
            result = supabase.table("trips").delete().eq("trip_id", trip_id).execute()
            return {"Success": True, "Message": "Trip deleted!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}


# ================= TRIP STOPS =================
class Trip_stops:
    def add_trip_stop(self, trip_id, stop_order, location_name, distance_to_next_km=None, duration_to_next_min=None, transport_mode_to_next=None):
        data = {
            "trip_id": trip_id,
            "stop_order": stop_order,
            "location_name": location_name,
            "distance_to_next_km": distance_to_next_km,
            "duration_to_next_min": duration_to_next_min,
            "transport_mode_to_next": transport_mode_to_next,
        }
        try:
            result = supabase.table("trip_stops").insert(data).execute()
            return {"Success": True, "Message": "Trip stop added!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def get_trip_stops(self, trip_id):
        try:
            result = supabase.table("trip_stops").select("*").eq("trip_id", trip_id).order("stop_order").execute()
            return {"Success": True, "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def update_trip_stop(self, stop_id, **kwargs):
        try:
            result = supabase.table("trip_stops").update(kwargs).eq("stop_id", stop_id).execute()
            return {"Success": True, "Message": "Trip stop updated!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    def delete_trip_stop(self, stop_id):
        try:
            result = supabase.table("trip_stops").delete().eq("stop_id", stop_id).execute()
            return {"Success": True, "Message": "Trip stop deleted!", "Data": result.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}
