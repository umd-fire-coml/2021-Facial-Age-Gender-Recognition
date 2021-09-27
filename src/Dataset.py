import requests
import os

directory = 'DATASET'
parent_dir = '2021-Facial-Age-Gender-Recognition/'

path = os.path.join(parent_dir, directory)

os.mkdir(path)

#r = requests.get('https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_0.tar')  
r = requests.get('https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic-s.aa-cdn.net%2Fimg%2Fios%2F899287106%2F45820b5b6bba46c7fcd853a46d554a34%3Fv%3D1&imgrefurl=https%3A%2F%2Fwww.appannie.com%2Fen%2Fapps%2Fios%2Fapp%2Fcat-wallpapers-themes-backgrounds%2F&tbnid=UmfhHVuuVae8cM&vet=12ahUKEwjkkZ7jt5_zAhVxqHIEHco3AL4QMygEegUIARCJAg..i&docid=diIWF-6EuAE3sM&w=256&h=256&itg=1&q=cat&hl=en&client=safari&ved=2ahUKEwjkkZ7jt5_zAhVxqHIEHco3AL4QMygEegUIARCJAg')  
with open('2021-Facial-Age-Gender-Recognition/DATASET', 'wb') as f:
    f.write(r.content)