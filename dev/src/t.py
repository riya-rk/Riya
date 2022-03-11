import json
from flask_restful import Api, Resource, reqparse
import argparse

#def get():
 #   f = open(r'C:\Users\shriy\Documents\sample4.json', "r")
  #  data = json.loads(f.read())
   # print(data)
    #return {'data': data}, 200
#get()

def post():

    f1={
        "firstName":"riya"
        "and add other attributes the same way"
    }

    f = open(r'C:\Users\shriy\Documents\sample4.json', "r")
    data = json.loads(f.read())
    #print(data)
    d = {
        'firstName': [f1['firstName']],
        'lastName': [f1['lastName']],
        'gender': [f1['gender']],
        'age': [f1['age']],
        'number': [f1['number']],
        'password': [f1['password']],

    }

    data['users'].append(d)
    #return {'data': data}, 201
    print(data)

post()
