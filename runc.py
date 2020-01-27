#! /usr/bin/env python
import argparse
import subprocess
import os.path
import time


def open_file(file_path):
    while not os.path.exists(file_path):
        time.sleep(1)

    if os.path.isfile(file_path):
        open_file = "./" + file_path
        subprocess.call([open_file])
    else:
        raise ValueError("%s isn't a file!" % file_path)



parser = argparse.ArgumentParser(description="Runs c++ files by reducing the compilation process")
parser.add_argument("input", help="Name of the c++ file")
parser.add_argument("-o", "--out", help="Specify the compiled file's name [Optional]")
parser.add_argument("-u", "--upgrade", help="Upgrade the C++ compiler", default="11")


args = parser.parse_args()

print(args.input)
print(args.out)
if args.out:
    subprocess.call(["g++", str(args.input), "-o", str(args.out)])
    open_file((str(args.out) + ".exe"))
else:
    subprocess.call(["g++", args.input, args.upgrade])
    open_file("a.exe")
