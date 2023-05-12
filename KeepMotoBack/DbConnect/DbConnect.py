import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("Resources/KeepMoto.json")
firebase_admin.initialize_app(cred)

