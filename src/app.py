"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Team-based soccer practice and competitive matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["david@mergington.edu", "maya@mergington.edu"]
    },
    "Swimming Club": {
        "description": "Swimming lessons and aquatic fitness sessions",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["leo@mergington.edu", "nina@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Explore painting, drawing, and mixed media art projects",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "noah@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting, stagecraft, and rehearsal for school performances",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": ["mia@mergington.edu", "lucas@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "Prepare for science competitions and build STEM projects",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["sophia@mergington.edu", "ethan@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for contests",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 18,
        "participants": ["olivia@mergington.edu", "liam@mergington.edu"]
    },
    "Volleyball Team": {
        "description": "Competitive volleyball practice and interschool matches",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["alex@mergington.edu", "sophia@mergington.edu"]
    },
    "Track and Field": {
        "description": "Run, jump, and throw events with coaching for improvement",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": ["maria@mergington.edu", "kevin@mergington.edu"]
    },
    "Pottery Studio": {
        "description": "Create ceramic art using pottery wheels and hand-building techniques",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["isla@mergington.edu", "noah@mergington.edu"]
    },
    "Dance Ensemble": {
        "description": "Choreograph and rehearse dance pieces for school events",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 18,
        "participants": ["emma@mergington.edu", "oliver@mergington.edu"]
    },
    "Debate Team": {
        "description": "Practice argumentation, public speaking, and competitive debates",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["sophia@mergington.edu", "ethan@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Build and program robots for challenges and competitions",
        "schedule": "Thursdays, 3:30 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["mia@mergington.edu", "lucas@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
