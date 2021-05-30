# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
import csv

# cred = credentials.Certificate("./serviceAccountKey.json")
# default_app = firebase_admin.initialize_app(cred)
# db = firestore.client()

# doc_ref = db.collection(u'Students')
# docs = doc_ref.get()


PRNMapID = {}

# for doc in docs:
#     if doc.exists:
#         studentInstance = doc.to_dict()
#         PRNMapID[studentInstance['prn']] = studentInstance['userID']
#     else:
#         print(u'No such document!')

dic = {}
        
with open('GPA.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lst = []
        for i in range(1, len(row)-1):
            lst.append(row[i])
        dic[row[0]] = lst
        
print(dic)
# print(PRNMapID)