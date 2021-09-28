import os
from os import path

path = os.getcwd()
parent = os.path.dirname(path)
path_of_imdb = os.path.dirname('imdb')

os.path.join(parent)
os.path.join(os.path.join)

def folder_present():
    if not (os.listdir('imdb')):
        print('Fail')
        return (False)
    else:
        print('Success')
        return (True)