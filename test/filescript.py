import os, sys, glob

DATA_FOLDER = 'PATH'
def check_files():
    totalFiles = 0
    totalDir = 0
    filesRequired = 20
    directoriesRequired = 2
    for base, dirs, files in os.walk(DATA_FOLDER):
        print('Searching in : ',base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
    print('Total Number of directories',totalDir)
    if totalFiles == filesRequired:
        print("All files are here!")
        return True
    else: 
        print("File missing") 
        return False


def check_jpg():
    # filepaths based on user's computer. 
    filepaths = ["", ""]
    jpgcounter = 0 
    jpgfiles = 72 

    for filep in filepaths:
        ext = os.path.splitext(filep)[-1].lower()
    if ext == ".mp3":
        jpgcounter += 1 

    if jpgcounter == jpgfiles:
        print("All jpgs are here!")
        return True
    else: 
        print("Jpg missing")
        return False

if __name__ == "__main__":
    print("Checking files")
    check_files()
    print("Checking jpg")
    check_jpg()
