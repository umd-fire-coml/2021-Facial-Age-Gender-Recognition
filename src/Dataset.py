import requests
import os

directory = 'DATASET'
parent_dir = '2021-Facial-Age-Gender-Recognition/'

path = os.path.join(parent_dir, directory)

os.mkdir(path)

r = requests.get('https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_0.tar')  
with open('2021-Facial-Age-Gender-Recognition/DATASET', 'wb') as f:
    f.write(r.content)