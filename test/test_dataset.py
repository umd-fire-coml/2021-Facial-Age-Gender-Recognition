import os
from os import path

path = os.getcwd()
parent = os.path.dirname(path)

os.path.join(parent)
os.path.join('src')

def folder_present():
    if (os.path.exists('dataset.tar')):
        print("Fail")
        return (False)
    else:
        print("Success")
        return (True)