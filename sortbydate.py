import os
import sys
import shutil
from datetime import datetime


def get_date_file(file):
    stamp = os.path.getctime(file)
    datee = datetime.fromtimestamp(stamp)
    _folder = f"{datee.day}-{datee.month}-{datee.year}"
    return _folder


def main():
    list_files = os.listdir()
    for file in list_files:
        if os.path.isdir(file) or file == "sortbydate.exe" or file == "sortbydate.py":
            continue
        else:
            _folder = get_date_file(file)
            if not os.path.exists(_folder):
                os.makedirs(_folder)
            dest_path = _folder + "/" + file
            status = shutil.move(src=file, dst=dest_path)
            print(f"moving {file} to {status}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
