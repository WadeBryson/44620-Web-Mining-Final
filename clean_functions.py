from spacytextblob.spacytextblob import SpacyTextBlob
from collections import Counter
import pickle, requests, spacy, pathlib, lyricsgenius, json


def polarity_score_from_lyrics(song, filename):
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')
    with open(filename, 'r') as f:
        lyrics = json.load(f)
    doc = nlp(lyrics)
    polarity = doc._.blob.polarity
    print(f'{song} Polarity: {polarity}')

def write_song_from_api_to_JSON(artist, song, filename):
    genius = lyricsgenius.Genius("lRsxb5ZjuM5SVrA2OYk-MpRv7LJZL806cKMfhhhBuaaplNYZQteRazYt-8XOJNiz")
    artist = genius.search_artist(artist, max_songs=1, sort="title")
    song = artist.song(song)
    with open(filename, 'w') as filename:
        json.dump(song.lyrics, filename)

def frequent_verbs(filename):
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')
    with open(filename, 'r') as f:
        lyrics = json.load(f)
        doc = nlp(lyrics)
    verbs = ['VERB']
    verb_tokens = [token.text.lower() for token in doc if not (token.is_space or token.is_punct or token.is_stop or token.pos_ not in verbs)]
    verb_count = Counter(verb_tokens)
    verb_top_5 = verb_count.most_common(5)
    print('The top 5 verbs and their frequency are:')
    for token, count in verb_top_5:
        print(f'{token} - {count}')

orig_list = [9,8,7,2]
new_list = [2*i for i in orig_list]
print(sum(new_list))


