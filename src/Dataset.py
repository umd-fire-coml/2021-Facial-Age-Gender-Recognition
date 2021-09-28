import requests
import os
import tarfile
import sys
from os import path

link = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_0.tar"
file_name = "dataset.tar"

with open('dataset.tar', 'wb') as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
            sys.stdout.flush()

my_tar = tarfile.open(file_name)
my_tar.extractall()
my_tar.close
os.remove(file_name)

if response:
    print("Success!")
else:
    print("An error has occurred.")