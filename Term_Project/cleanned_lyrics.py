import pandas as pd
import string
lyrics_data = pd.read_csv("./Term_Project/lyrics-data.csv")
artists = pd.read_csv("./Term_Project/artists-data.csv")
lyrics_data.dropna(inplace=True)

lyrics = lyrics_data.drop(
lyrics_data[lyrics_data['Idiom'] != 'ENGLISH'].index)
lyrics = lyrics_data['Lyric']
cleanned_lyrics = lyrics.apply(lambda s: s.translate(
    str.maketrans('', '', string.punctuation + u'\xa0')))
cleanned_lyrics = cleanned_lyrics.apply(lambda s: s.lower())
cleanned_lyrics = cleanned_lyrics.apply(lambda s: s.translate(
    str.maketrans(string.whitespace, ' '*len(string.whitespace), '')))
cleanned_lyrics = cleanned_lyrics.drop_duplicates()

cleanned_lyrics_file = pd.DataFrame([],columns=['artists','songs','lyrics'])