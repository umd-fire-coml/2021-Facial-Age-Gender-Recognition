import sys
import os
from os import path
from src.Dataset import Downloader


def folder_present():
    Downloader.downloader("https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki_crop.tar")
    path = os.getcwd()
    parent = os.path.dirname(path)
    os.path.join(parent)
    os.path.join('src')
    assert not (os.listdir('wiki_crop'))