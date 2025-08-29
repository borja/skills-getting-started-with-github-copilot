from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['high_school']
activities = db['activities']

print("Current activities in database:")
for activity in activities.find():
    print(f"\nActivity: {activity['_id']}")
    print(f"Participants: {activity['participants']}")
    print(f"Max participants: {activity['max_participants']}")
