""" { { Web } } """
from flask import Flask, request, jsonify, redirect, render_template, url_for  # get the Flask object from the flask module

app = Flask(__name__)    # Make an app using the current file

""" { { Database } } """
import pymongo 
from bson.objectid import ObjectId
from pymongo import MongoClient
import json

import logging
logging.basicConfig(level=logging.DEBUG)

client = MongoClient()
db = client.ebuscardb
db.dataset                  #collection

'''
array = ['2', '3']
person1 = jsonify(
                    {
                        'id' : "1",
                        'first_name' :"John",
                        'last_name' : "Doe",
                        'email' : "1@gmail.com",
                        'linkedin': "1@linkedin.com",
                        'phone_number' : "111",
                        contacts_ids = [1,2]
                    }
                 )'''

""" { { Web and Database } } """
@app.route('/')
def database_test():
    print("SADASD")
    return ( '<h1>database_test visited</h1>' )

@app.route('/login', methods=['POST'])
def login():
    print("login page accessed")
    username = request.form['Username']
    password = request.form['Password']  
    return redirect( url_for('render') + username )
    #return redirect('https://www.google.ca/', code = 302)
    #return redirect('file:///C:/Users/nicol/odrive/uWaterloo/Programming%20Side%20Projects/StarterHacks/ContactsApp/MainHomePage.Html', code = 302)
    #return "<h1>username : " + username + "<br>password : " + password + "<br></h1>"
    ''' print("username : {}\n".format(username))
    print("password : {}\n".format(password))'''
'''
@app.route('/view_my_profile>')
def view_my_profile():
    first_name  = request.form['First Name']
    last_name   = request.form['Last Name']
    company     = request.form['Company']
    email       = request.form['Email']
    phone_number= request.form['Phone Number']
    address    = request.form['Address']
    return render_template('personalProfile.html', 
                            firstName = first_name,
                            lastName  = last_name,
                            email     = email,
                            company   = company,
                            #position  = ???,
                            phone
                            ) '''

@app.route('/testLogin/<string:name>') #redirecting to the correct page from a given name
def testLogin(name):
    return redirect( url_for('render') + name )

@app.route('/render/')
@app.route('/render/<string:name>') #rendering a template populated with a given input string
def render(name=None):
    return render_template('test.html', name=name)

@app.route('/show_db')
def show_db():
    print('show_db called!')
    cursor = db.ebuscardb.find()
    for document in cursor:
        print(document)


@app.route('/delete_db')
def delete_db():
    print('delete_db called!')

@app.route('/test')
def test_fn():
    return ( '<h1>database_test visited</h1>' )

#@app.route('/createProfile', methods=['POST'])
@app.route('/createProfile')
def createProfile():
    '''
    username = request.form['Username']
    first_name = request.form['First_name']
    last_name = request.form['Last_name']
    linkedin = request.form['Linkedin']
    email = request.form['Email']
    phone = request.form['Phone']   
    '''
    username = 'u'
    first_name = 'f'
    last_name = 'l'
    linkedin = 'l'
    email = 'e'
    phone = 'p'   
    
    
    '''profileObj = jsonify( 
                        {
                            'username'      : username,
                            'first_name'    : first_name,
                            'last_name'     : last_name,
                            'email'         : email,
                            'phone'         : phone,
                            'linkedin'      : linkedin,
                            'contacts'      : {}
                        } 
                     ) '''
    
    profileObj = {
                    'username'      : username,
                    'first_name'    : first_name,
                    'last_name'     : last_name,
                    'email'         : email,
                    'phone'         : phone,
                    'linkedin'      : linkedin,
                    'contacts'      : {}
                 } 
    
    db.ebuscardb.insert(profileObj)
    return ( 'new profile craeted' )
    db.ebuscardb
    #store profileObj into the mongodb via pymongo code

@app.route('/updateContacts'
            +'/<string:myID>'
            +'/<string:otherID>')
def updateContacts(myID, 
                   otherID):

    #pymongo code to find (query) the document that matches 'myId'
    #ditto but matches 'otherId'
    #push 'otherId' to the contactsArray of 'myId' document
    #push 'myId' to the contactsArray of 'otherId' document
    return

@app.route('/viewContactsList'
        +'/<string:myID>')
def viewContactsList(myID):

    #find (query) the document that matches 'myID'
    return #return the contactsArray of the object of that matched document

@app.route('/viewContact'
        +'/<string:contactID>', methods=['POST'])
def viewContact(contactID):
    #find (query) the document that matches 'contactID'
    #return #return the JSON object of that matched document
    return jsonify( 
                    {
                        'contactID' : contactID,
                        'field1'    : 'value1'
                    }
                  )

if __name__ == '__main__':
     app.run( host='0.0.0.0', debug=True ) #the public/shared IP address