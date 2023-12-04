from src.gmaps import Gmaps

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

queries = [
   "hotpot in Ho Chi Minh city"
]

Gmaps.places(queries, max=100)