import requests
import os
import tarfile
from os import path

directory = 'dataset'

if not (path.exists(directory)):
    os.mkdir(directory)

r = requests.get('https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_0.tar')  
with open('dataset/dataset.tar', 'wb') as f:
    f.write(r.content)

my_tar = tarfile.open(dataset.tar.gz)
my_tar.extractall()
my_tar.close
 
if r:
    print('Success!')
else:
    print('An error has occurred.')