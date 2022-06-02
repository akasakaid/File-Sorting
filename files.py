import os
import shutil
import sys

def GetAllFile():
    list_dir = os.listdir()
    return list_dir

def MoveFile(data):
    if os.path.isdir(data) or data == sys.argv[0]:
        return
    else:
        SplitName = data.split(".")
        if len(SplitName) == 0:
            if not os.path.exists("No Exstension File"):
                os.makedirs("No Exstension File")
            shutil.move(src=data,dst="No Exstension File")
            return
        EXT = SplitName[len(SplitName)-1]
        folder_out = EXT.upper() + " File"
        if not os.path.exists(folder_out):
            os.makedirs(folder_out)
        shutil.move(src=data,dst=folder_out)

All = GetAllFile()
for i in All:
    try:
        MoveFile(i)
    except PermissionError:
        pass
    except shutil.Error as e:
        print(e)