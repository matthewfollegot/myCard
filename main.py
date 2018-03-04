import pymongo

from flask import Flask, request, jsonify

from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient() 		#creating connection

db = client.ebuscardb
db.dataset 					#collection

#db.ebuscardb.insert({'first_name': 'Ahrar', 'last_name': 'Monsur', 'phone': '2052991285', 'email': 'ahrarmonsur@gmail.com', 'contacts': {}})

#UPDATING CONTACTS INTO EMPTY ARRAY $SET COMMAND
#db.ebuscardb.update({'_id': ObjectId('5a9bbeffc19535109e029467')}, {"$set": {"contacts": [ObjectId('5a9b24135804ece0f5c1e5ea')]}})

#UPDATING CONTACTS INTO CURRENT ARRAY $PUSH COMMAND
db.ebuscardb.update({'_id': ObjectId('5a9bbeffc19535109e029467')}, {"$push": {"contacts": [ObjectId('5a9b25355804ece0f5c1e5eb')]}})

cursor = db.ebuscardb.find() #returns all documents without any criteria/restriction

for document in cursor: 	 #iterates through cursor and prints the matching docs
	print(document)

	#QUERY BY _id
	#print(db.ebuscardb.find_one({'_id': ObjectId('5a9b25815804ece0f5c1e5ec')}))

	

	#remove ahrar
	#db.ebuscardb.remove({'first_name': 'Ahrar'})




	