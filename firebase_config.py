import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate(r"C:\Users\Mahima\Downloads\athleteedge-c3eb6-firebase-adminsdk-fbsvc-85ab4ade95.json")
firebase_admin.initialize_app(cred)

# Firestore DB
db = firestore.client()

# Reference to 'athletes' collection
athlete_collection = db.collection('athletes')
