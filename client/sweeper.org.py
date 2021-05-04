# to copy all of my documents into another location.
import os
import pathlib
import shutil


writeToFile=True

filePath=["D:\\", "C:\\Users"]
# ext=['mkv','docx','doc','pdf','mp4','zip',]
fileExt=["**\*.docx","**\*.doc","**\*.pdf","**\*.jpg","**\*.png","**\*.txt","**\*.py","**\*.sh"]
fileList={}
for each_drive in filePath:
    fileList[each_drive]={}
    for each_type in fileExt:
        fileList[each_drive][each_type]=list(pathlib.Path(each_drive).glob(each_type))

if writeToFile:
    with open('test.txt', 'w') as file1:
        for each in fileList.values():
            for each2 in each.values():
                for entry in each2:
                    print(entry)
                    file1.writelines(str(str(entry)+ "\n"))

#######################################
# create destination directory
file1=open ('test.txt', 'r')
text= file1.readlines()
# print(text)
for each in text:
    each=each[:-1]
    destination="BackupDIR-"+each[0]+each[2:]
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    try:
        shutil.copy(each,destination)
    except PermissionError:
        pass