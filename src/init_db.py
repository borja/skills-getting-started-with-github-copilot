from pymongo import MongoClient

# Initial activities data (same as in app.py)
initial_activities = {
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
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly games",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ethan@mergington.edu", "ava@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Explore painting, drawing, and sculpture techniques",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["isabella@mergington.edu", "liam@mergington.edu"]
    },
    "Drama Club": {
        "description": "Act, direct, and produce school plays and performances",
        "schedule": "Fridays, 3:30 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["noah@mergington.edu", "amelia@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Tuesdays, 4:00 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["oliver@mergington.edu", "charlotte@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
        "max_participants": 14,
        "participants": ["elijah@mergington.edu", "harper@mergington.edu"]
    }
}

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['high_school']
    activities_collection = db['activities']

    # Clear existing data
    activities_collection.delete_many({})
    
    # Insert new data
    for name, details in initial_activities.items():
        activities_collection.insert_one({
            "_id": name,  # Using activity name as the document ID
            **details
        })
    
    print("Database initialized with the following activities:")
    for activity in activities_collection.find():
        print(f"\nActivity: {activity['_id']}")
        print(f"Participants: {activity['participants']}")
        print(f"Max participants: {activity['max_participants']}")

if __name__ == "__main__":
    main()
