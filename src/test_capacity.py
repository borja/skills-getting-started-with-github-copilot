from pymongo import MongoClient

def test_capacity():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['high_school']
    activities = db['activities']
    
    # Let's use Math Olympiad which has a max of 10 participants
    activity = activities.find_one({"_id": "Math Olympiad"})
    print(f"\nCurrent participants in Math Olympiad: {len(activity['participants'])}")
    print(f"Maximum capacity: {activity['max_participants']}")
    print(f"Space left: {activity['max_participants'] - len(activity['participants'])}")
    
    # Print current participants
    print("\nCurrent participant list:")
    for participant in activity['participants']:
        print(f"- {participant}")

if __name__ == "__main__":
    test_capacity()
