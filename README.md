# smart travel route optimizer

Planning trips with many stops can be difficult and time-consuming. This project presents a Smart Travel Route Optimizer that helps users find the best order to visit multiple places, saving time and money. The system uses real travel data to calculate distances and travel times between locations, then applies optimization methods to create efficient routes. All user trips and routes are stored in a cloud database for easy access and management. This tool supports different travel preferences and transportation types, making trip planning easier and more convenient for travelers.

# features

1. **Multi-Destination Input**
   Allow users to enter multiple places or stops they want to visit on a trip.

2. **Route Optimization**
   Automatically calculate the most efficient order to visit all destinations based on shortest distance, time, or cost.

3. **Distance and Time Estimation**
   Provide estimated travel distances and durations between stops.

4. **Multiple Transport Modes**
   Support different transportation options (car, public transit, walking, cycling) and optimize accordingly.

5. **Customizable Preferences**
   Users can prioritize optimization criteria (e.g., minimize cost vs. time).

6. **Save and Manage Trips**
   Users can save their planned trips and revisit or edit them later.

7. **Interactive Map Visualization**
   Display the optimized route on a map with markers for each destination.

8. **Estimated Arrival and Departure Times**
   Calculate and show expected arrival and departure times at each stop.

9. **Cost Prediction**
   Provide estimated travel costs based on distance, transport mode, or other factors.

10. **User Authentication**
    Allow users to create accounts, log in, and manage their trips securely.

# project structure

Smart Travel Route Optimizer/
|
|---src/           #Core application logic
|    |---logic.py  #Business logic and task
operations
|   |---db.py      #Database operations
|
|----api/          #Backend API
|    |__main.py    #FastAPI endpoints
|
|----frontend/     #Frontend application
|     |__app.py    #Streamlit web interface
|
|___requirements.txt   #Python Dependencies
|
|___README.md          #Project documentation
|
|___.env               #Python Variables


## Quick Start

### Prerequisites

- Python 3.8 or higher
- A Supabase account
- Git(Push,Cloning)

### 1. Clone or Download the Project 

# Option 1: Clone with Git
git clone <repository url>

# Option 2: Download and extract the ZIP file

### 2. Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3. Set Up Supabase Database

1.Create a Supabase Project:

2.Create the users table:

- Go to the SQL Editor in your supabase dashboard run this SQL commands:

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE trips (
    trip_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    trip_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE trip_stops (
    stop_id SERIAL PRIMARY KEY,
    trip_id INTEGER REFERENCES trips(trip_id) ON DELETE CASCADE,
    stop_order INTEGER NOT NULL,
    location_name VARCHAR(255) NOT NULL,
    distance_to_next_km NUMERIC(10,2),
    duration_to_next_min NUMERIC(10,2),
    transport_mode_to_next VARCHAR(50)
);


### 4. Configure Environment Variables

1. Create a `.env` file in the project root

2. Add your supabase credentials to `.env`:

SUPABASE_URL="https://bxqkfhkynukbczpzpmnr.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ4cWtmaGt5bnVrYmN6cHpwbW5yIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI1MTYsImV4cCI6MjA3MzY1ODUxNn0nCAGWlSSj5Fjfw29Ea482QPi-5RRXp0ATeF0mNqAE2M"

### 5. Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

the app will open in your browser at `http://loacalhost:8080`

## FastAPI Backend

cd api
python main.py

The API will be avaliable at `http://loacalhost:8080`

## How to use

## Technical Details

**Python Libraries**:
- Flask or FastAPI (backend web framework)
- Pandas (data manipulation)
- NumPy (numerical computations)
- Google OR-Tools (route optimization algorithms)
- Requests (API calls)
- SQLAlchemy or Supabase Python Client (database interaction)
- Streamlit (for quick frontend apps)

### Technologies used

**Frontend**: Streamlit (Python web framework)
**Backend**: FastAPI (Python REST API framework)
**Database**: Supabase (PostgreSQL-based-backend-as-a-service)
**Language**: Python 3.8+

### Key Components

1. **`src/db.py`**: Database operations 
- Handles all CRUD operations with Supabase

2. **`src/logic.py`**: Business logic 
- Task validation and processing

## Troubleshooting

## Common Issues

1. **"Module not found" errors**
- Make sure you've installed all dependencies: `pip install -r requirements.txt`
- Check that you're running commands from the correct directory

## Future Enhancements

- **Real-Time Traffic and Weather Integration**:
Adjust routes dynamically based on current traffic and weather conditions.

- **Multi-Day Trip Planning**:
Plan routes across several days with accommodation stops and rest breaks.

- **Personalized Recommendations**:
Suggest popular attractions, restaurants, or services near stops.

- **Multi-User Collaboration**:
Allow multiple users to collaborate on the same trip planning.

- **Integration with Booking APIs**:
Connect to flight, hotel, or transport booking services to book directly.

## Support

If you encounter any issues or have questions:

mail id: yashaswinipenumuchu2006@gmail.com
phone number: 9987579201





