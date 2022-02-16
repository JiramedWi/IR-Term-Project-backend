import string

import pandas as pd
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
# from flask_cors import CORS
from numpy import require

import requireFunction as fucntion
from bm25 import BM25

lyrics_data = './Term_Project/assets/data.csv'

app = Flask(__name__)
api = Api(app)
# CORS(app)


# validation request
def notFoundScoreType():
    abort(404, message='Select the score rank first!')


class Lyricsdata(Resource):
    def get(self):
        data = pd.read_csv(lyrics_data)
        data = data.tail(1)
        data = data.to_dict()
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query', required=True, type=str)
        parser.add_argument('score', required=True, type=str)
        args = parser.parse_args()
        query = args['query']
        query = [query]

        if args['score'] == 'tf':
            tf = fucntion.tf_ranking(query)
        elif args['score'] == 'tf-idf':
            tf = fucntion.tf_idf_ranking(query)
        elif args['score'] == 'bm25':
            tf = fucntion.bm25_ranking(query[0])
        else:
            notFoundScoreType()
        return {'ranks :': tf + query}, 200
        # return {'lyrics': "query: "+query + " , score: "+score}, 200

# class Iula(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('query', required=True, type=str)
#         args = parser.parse_args()
#         return {}

# api.com/
api.add_resource(Lyricsdata, '/query')
# api.add_resource(Iula, '/iula')

if __name__ == '__main__':
    app.run(debug=True)
