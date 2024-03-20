import os
import time

cur_dir = os.path.dirname(__file__)
dirs = os.walk(cur_dir)
for dirpath, dirname, files in dirs:
    print("{dirpath:=^50}".format(dirpath=dirpath))
    if not dirname: dirname = None
    if not files: files = None
    print(f"|-dirs-{dirname}\n|-files-{files}\n")

    if files:
        for file in files:
            full_path = os.path.join(dirpath, file)
            raw_last_write = os.path.getmtime(full_path)
            size = os.path.getsize(full_path)
            last_write = time.gmtime(raw_last_write)
            print(f"{full_path}\n"
                  f"|:| LAST WRITE: {last_write.tm_mday}-{last_write.tm_mon}-{last_write.tm_year}\n"
                  f"|:| SIZE: {size} Bytes\n"
                  f"|:| PARENT DIR: {os.path.dirname(full_path)}")
    print("\n")
