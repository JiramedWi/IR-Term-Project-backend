from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import string
lyrics_data = pd.read_csv("./Term_Project/data/lyrics-data.csv")
lyrics_data.dropna(inplace=True)

app = Flask(__name__)
api = Api(app)


class cleanLyricsData(Resource):
    def get(self):
        lyrics = lyrics_data.drop(
            lyrics_data[lyrics_data['Idiom'] != 'ENGLISH'].index)
        lyrics = lyrics_data['Lyric']
        cleanned_lyrics = lyrics.apply(lambda s: s.translate(
            str.maketrans('', '', string.punctuation + u'\xa0')))
        cleanned_lyrics = cleanned_lyrics.apply(lambda s: s.lower())
        cleanned_lyrics = cleanned_lyrics.apply(lambda s: s.translate(
            str.maketrans(string.whitespace, ' '*len(string.whitespace), '')))
        cleanned_lyrics = cleanned_lyrics.drop_duplicates()
        cleanned_lyrics = cleanned_lyrics.to_dict()
        return {'lyrics': cleanned_lyrics}, 200


# api.com/
api.add_resource(cleanLyricsData, '/')

if __name__ == '__main__':
    app.run(debug=True)
