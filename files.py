import os
import shutil

MAIN = r'C:\Users\Aspire\Desktop\Ict Activity\Data analysis'
DIRS = r'C:\Users\Aspire\Desktop\Ict Activity\web authoring'

for root, subdirs, files in os.walk(DIRS):
    print("root", root)
    print("subdirs", subdirs)
    print("files", files)
    for file in files:
        path = os.path.join(root, file)
        shutil.move(path, MAIN)