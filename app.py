import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("🚀 Route Optimizer Frontend")

menu = st.sidebar.selectbox(
    "Choose an action",
    ["Create User", "Create Trip", "Create Trip Stop"]
)

# ===== Helper function to handle API responses =====
def handle_response(res):
    try:
        if res.status_code == 200:
            st.success(res.json().get("Message", "Success"))
        elif res.status_code == 400:
            detail = res.json().get("detail", "Bad Request")
            st.error(f"⚠️ {detail}")
        else:
            st.error(f"❌ Error {res.status_code}: {res.text}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")


# ===== Users =====
if menu == "Create User":
    st.header("👤 Create User")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    created_at = st.text_input("Created At (optional, e.g. 2025-09-28)")

    if st.button("Create User"):
        if not username or not email or not password:
            st.error("Please fill all required fields")
        else:
            payload = {
                "username": username,
                "email": email,
                "password_hash": password,
                "created_at": created_at if created_at else None
            }
            try:
                res = requests.post(f"{BASE_URL}/users", json=payload)
                handle_response(res)
            except Exception as e:
                st.error(f"Request failed: {e}")


# ===== Trips =====
elif menu == "Create Trip":
    st.header("🗺️ Create Trip")
    user_id = st.number_input("User ID", min_value=1, step=1)
    trip_name = st.text_input("Trip Name")
    created_at = st.text_input("Created At (optional)")

    if st.button("Create Trip"):
        if not user_id or not trip_name:
            st.error("Please fill all required fields")
        else:
            payload = {
                "user_id": int(user_id),
                "trip_name": trip_name,
                "created_at": created_at if created_at else None
            }
            try:
                res = requests.post(f"{BASE_URL}/trips", json=payload)
                handle_response(res)
            except Exception as e:
                st.error(f"Request failed: {e}")


# ===== Trip Stops =====
elif menu == "Create Trip Stop":
    st.header("📍 Create Trip Stop")
    trip_id = st.number_input("Trip ID", min_value=1, step=1)
    stop_order = st.number_input("Stop Order", min_value=1, step=1)
    location_name = st.text_input("Location Name")
    distance_to_next_km = st.number_input("Distance to Next (km)", min_value=0.0, step=0.1, format="%.2f")
    duration_to_next_min = st.number_input("Duration to Next (min)", min_value=0.0, step=1.0, format="%.1f")
    transport_mode_to_next = st.text_input("Transport Mode to Next (optional)")

    if st.button("Create Trip Stop"):
        if not trip_id or not stop_order or not location_name:
            st.error("Please fill all required fields")
        else:
            payload = {
                "trip_id": int(trip_id),
                "stop_order": int(stop_order),
                "location_name": location_name,
                "distance_to_next_km": distance_to_next_km if distance_to_next_km > 0 else None,
                "duration_to_next_min": duration_to_next_min if duration_to_next_min > 0 else None,
                "transport_mode_to_next": transport_mode_to_next if transport_mode_to_next else None
            }
            try:
                res = requests.post(f"{BASE_URL}/trip_stops", json=payload)
                handle_response(res)
            except Exception as e:
                st.error(f"Request failed: {e}")
