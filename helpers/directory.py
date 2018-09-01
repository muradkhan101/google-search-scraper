import os

def make_directories(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return True