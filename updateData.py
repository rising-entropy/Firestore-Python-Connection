import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'Students')
docs = doc_ref.get()


PRNMapID = {}

for doc in docs:
    if doc.exists:
        studentInstance = doc.to_dict()
        PRNMapID[studentInstance['prn']] = studentInstance['userID']
    else:
        print(u'No such document!')
        
print(PRNMapID)