from google.cloud import firestore
db = firestore.Client()
doc_ref = db.collection(u'users').document(u'testuser1')
doc_ref.set({u'first':u'Test', u'last':u'User1'})

