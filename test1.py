# coding: UTF-8
import os
import glob
import sys


def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def fuga(dir_path, *ext_arr):
    os.chdir(dir_path)
    file_arr = []
    for ext in ext_arr:
        file_arr.extend(glob.glob(ext))
    return file_arr


for file in fild_all_files('/Users/kenpos/Dropbox/source code/Python/Arbeit'):
    print file
