import requests

r = requests.get('https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_0.tar')  
with open('/Users/nickpangaro/2021-Facial-Age-Gender-Recognition/DATASET', 'wb') as f:
    f.write(r.content)