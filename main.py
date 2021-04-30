from pathlib import Path
from os import makedirs
from os.path import dirname
from shutil import move

from socket import gethostname
from platform import system

# the following line prevents the code from running inside my machine
#temporary Bypass for testing of file listing and indexing. DO not comment this line once shuitl.move() is used

#######################################################################################################
# if gethostname() != 'debian':
#     print("The code is supposed to be run inside of a VM you dimwit.")
#     exit()
#######################################################################################################


FILETYPES = ['/**/*.test1','/**/*.test2']

def get_files_from_windows():
    print("Working on it")


def get_files_from_mac():
    print("MAC OS Detected. No use running this :?")


def get_file_index():
    print("Linux Detected")

    #on Linux we start with the root directory so no need for a basepath


def main():
    # to detect what OS the system is running
    sysn = system()

    if sysn == 'Linux':
        get_file_index()
    elif sysn == 'Win':  # dont know the output
        get_files_from_windows()
        pass
    elif sysn == 'MacOS':  # dont know the output
        get_files_from_mac()
        # never used a MAC so dont know how to get files from this thing.


# lets first index the files that need to be encrypted.

if __name__=='__main__':
    main()
