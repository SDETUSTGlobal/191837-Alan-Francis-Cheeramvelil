import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
# Check if file exists
	if path.exists("Python.txt"):
# get the path to the file in the current directory
	    src = path.realpath("Python.txt");
# rename the original file
	os.rename("career.Python.txt","Python.txt")
# now put things into a ZIP archive
	root_dir,tail = path.split(src)
    shutil.make_archive("Python archive", "zip", root_dir)
# more fine-grained control over ZIP files
with ZipFile("testPython.zip","w") as newzip:
	newzip.write("Python.txt")
	newzip.write("Python.txt.bak")
if __name__== "__main__":
	  main()