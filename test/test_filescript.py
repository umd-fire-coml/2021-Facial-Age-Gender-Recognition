import os 
from filescript import check_files, check_jpg

# they should return false on remote because the file path is not specified 
def test_jpg():
    assert bool(check_jpg()) == False

def test_numfiles(): 
    assert bool(check_files()) == False

if __name__ == "__main__":
    test_jpg()
    test_numfiles()

    print("All files are ok!")