import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv

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

dic = {}
        
with open('GPA.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lst = []
        for i in range(1, len(row)):
            lst.append(row[i])
        dic[row[0]] = lst

#dic maps PRNs with Marks
#PRNMapID maps PRNs with Student Model userID

fieldNames = dic['prn']

del dic['prn']

for k, v in dic.items():
    
    requiredChanges = {}
    for i in range(len(fieldNames)):
        requiredChanges[fieldNames[i]] = v[i]
    stu_ref = doc_ref.document(PRNMapID[k])
    stu_ref.set(requiredChanges, merge=True)

# print(dic)
# print(PRNMapID)