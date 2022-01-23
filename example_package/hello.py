from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

users_path = './example_package/data/users.csv'
location_path = '/example_package/data.location.csv'

app = Flask(__name__)
api = Api(app)


class helloMFK(Resource):
    def get(self):
        return {'hello': 'world'}


class Users(Resource):
    def get(self):
        data = pd.read_csv(users_path)  # read local CSV
        data = data.to_dict()  # covert dataframe to dict
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True, type=int)
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('city', required=True, type=str)
        args = parser.parse_args()  # act as dictinary

        data = pd.read_csv(users_path)

        if args['userId'] in data['userId']:
            return{
                'message': f"{args['userId']} already exists"
            }, 409
        else:
            data = data.append({
                'userId': str(args['userId']),
                'name': args['name'],
                'city': args['city'],
                'locations': []
            }, ignore_index=True)
            data.to_csv(users_path, index=False)
            return {'data': data.to_dict()}, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True, type=int)
        args = parser.parse_args()  # act as dictinary

        data = pd.read_csv(users_path)

        if args['userId'] in data['userId']:
            data = data[data['userId'] != str(args['userId'])]
            data.to_csv(users_path, index=False)
            return {'data': data.to_dict()}, 200
        else:
            return{
                'message': f"{args['userId']} dose not exist"
            }, 404


# class Location(Resource):
    # def get(self):
    #     data = pd.read_csv(location_path)
    #     data = data.to_dict()
    #     return {}


# api.com/
api.add_resource(helloMFK, '/')
api.add_resource(Users, '/users')  # '/users' is our entry point

if __name__ == '__main__':
    app.run(debug=True)
