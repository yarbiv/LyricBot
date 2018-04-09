import genius
import sys
name = sys.argv[1].replace("`", "")
api = genius.Genius()
artist = api.search_artist(str(name))
api.save_artist_lyrics(artist)