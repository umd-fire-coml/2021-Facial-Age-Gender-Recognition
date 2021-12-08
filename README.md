# 2021-Facial-Age-Gender-Recognition

![This is an image](https://camo.githubusercontent.com/e3136e24e49cce35cb1fa1213b38fa8feaadaf992851044b883581975ee1aa99/68747470733a2f2f687561686f6e6774752e6d652f6c6f676f2d62616e6e65722d464952452d434f4d4c2e706e67)

    The product predicts the face and gender of a person.
    The use of age and gender recognition has a myriad of
    applications including, security and the advertising industry.

    Machine learning facial age and gender recognition uses a model
    trained with a dataset of images to predict one's age and gender.
    Our model uses a series of convolutional layers to extract and learn
    information for better predictions. By training the model, we are
    able to make is more accurate as it gets more and more data to
    analyze age and gender. 

    Learn more about this project by watching our demonstration video
    for a high-level walkthrough 

## Interactive Notebook and Demonstration Video
    Here is the interactive notebook: https://colab.research.google.com/drive/11n9RuOZSQNjG7u2pkdJq4DnSOZha2HQz?usp=sharing.

    Here is the video: https://youtu.be/ouW145ZnGCY.

**Training**

    In order to have the age and gender stored in the list, the variable labels_f is used. Using sklearn, the data is split into train and test. We import train_test_split from sklearn. After getting the train models, we create a Convolutional layer. The model itself takes in input shape 
    which would be the image. Then Model.summary() is returned. 

**Testing**

    The method test_image takes in input the model we trained, and the image as well as the pixels in order to return the predictions. We use the method test_image to plot the image, where we have 2 labels one being the "Predicted Age" and "Predicted Sex". The image is also plotted with the predicted age and sex returned. 

**How to download the dataset**

    Run the Dataset.py script. This will download, unzip, and
    store the images in the desired file structure.

**Environment**

    The following packages are required to use this project: 
    tensorflow=2.6.0, scikit-learn(=1.0), requests(=2.26.0),
    pip(=21.2.4), pandas=(1.3.3), opencv-python(=4.5.3.56),
    matplotlib(=3.4.3), numpy(=1.19.5), keras(=2.6.0).
    The convention is to pip install evnironment requirements through
    creating a requirements.txt that lists each of the packages and
    then go a quick and simple pip install using the file.

**imdb/**

    This directory contains the dataset

**Dataset.py**

    Script that downloads, unzips, and
    assembles the dataset in the desired file structure.

**backbone.py**

    Our model.

**build_cache.m**

    Matlab file that uses wiki.mat to extract the
    age and gender metadata and filepaths into a csv.

**cache.csv**

    Contains filepath, age, and gender of each image.

**filescript.py**

    Checks if all files are present.

**generator.py**

    Reads csv as an array metadata. x_filepaths contains the
    full relative path (which will be used to load images) and
    the y_labels will contain the age and gender.

**main.py**

    Run main.py to call download script from Dataset.py

**wiki.mat**

    Contains metadata of images (age, gender, etc.)

**test_dataset.py**

    Checks if correct dataset is downloaded 

**test_env.py**

    Checks if all necessarily requirements are installed.

**test_filescript.py**

    Tests if the data is downloaded properly and in correct file
    order

**.gitignore**

    For purpose of controlling what gets pushed to github. Excludes
    dataset as it is very large.

**requirements.txt**

    Contains a list of the necessary enviroment requirements needed.

**test-requirements.txt**

    For testing purposes. To help run pytest. Can create your own
    test to check whether a file or script is working correct

## References

    Rasmus Rothe, Radu Timofte, Luc Van Gool, "Deep expectation of real and apparent age from a single image without facial landmarks," *International Journal of Computer Vision*, vol. 126, no. 2-4, p. 144-157, 2018. Available: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/.