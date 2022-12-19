import os
import sys
import shutil
from datetime import datetime


def get_date_file(file):
    stamp = os.path.getmtime(file)
    datee = datetime.fromtimestamp(stamp)
    bulan = str(datee.month).zfill(2)
    hari = str(datee.day).zfill(2)
    _folder = f"{datee.year}-{bulan}-{hari}"
    return _folder


def main():
    list_files = os.listdir()
    for file in list_files:
        if os.path.isdir(file):
            continue
        else:
            try:
                _folder = get_date_file(file)
                if not os.path.exists(_folder):
                    os.makedirs(_folder)
                dest_path = _folder + "/" + file
                status = shutil.move(src=file, dst=dest_path)
                print(f"moving {file} to {status}")
            except Exception as e:
                print(e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
