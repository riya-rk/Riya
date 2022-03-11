from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        f=open(r'C:\Users\shriy\Documents\sample4.json',"r")
        data = json.loads(f.read())
        print(data)
        return {'data' : data}, 200



    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('gender', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('number', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()

        f = open(r'C:\Users\shriy\Documents\sample4.json', "r")
        data = json.loads(f.read())
        print(data)
        new_data={
            'firstName' : args['firstName'],
            'lastName'  : args['lastName'],
            'gender'    : args['gender'],
            'age'       : args['age'],
            'number'    : args['number'],
            'password'  : args['password']
        }

        data['users'].append(new_data)
        print(data)
        return {'data' : data}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=True)
        args = parser.parse_args()
        f = open(r'C:\Users\shriy\Documents\sample4.json', "r")
        data = json.loads(f.read())

        data = data[data['firstName'] != args['firstName']]

        new_data = jsom.dumps(data)
        print(new_data)
        return {'message' : 'Record deleted successfully.'}, 200



# Add URL endpoints
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()