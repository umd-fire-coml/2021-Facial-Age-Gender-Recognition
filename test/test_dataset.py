import sys
import os
from os import path

from src.dataset import Downloader   


path = os.getcwd()
parent = os.path.dirname(path)

os.path.join(parent)
os.path.join('src')


Downloader.downloader("https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki_crop.tar")

def folder_present():
    if (os.path.exists('dataset.tar')):
        print("Fail")
        return (False)
    else:
        print("Success")
        return (True)