import os
import shutil
if os.path.exists("demofile.txt"):
    shutil.copy("demofile.txt","backup.txt")
    print("Backup created.")

path="backup.txt"

if os.path.exists(path) and os.path.isfile(path):
    if os.access(path, os.W_OK):
        try:
            os.remove(path)
            print("Backup deleted.")
        except OSError as error:
            print("Could not delete:",error)
else:
    print("Backup does not exist")
