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
    parser=argparse.ArgumentParser()
    parser.add_argument('firstName')
    args=parser.parse_args()
    f1={
        "firstName": [args['firstName']]
    }
    print(f1)

post()
