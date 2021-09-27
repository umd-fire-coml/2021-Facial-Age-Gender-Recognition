import os
from os import path

def folder_present():
    if(path.exists('dataset')):
        print('Success')
    else:
        print('fail')
    assert path.exists('dataset') 