#! /usr/bin/env python
import argparse
import subprocess
import os.path
import time
import json

with open('./config.json') as f:
    data = json.load(f)


def open_file(file_path):
    while not os.path.exists(file_path):
        time.sleep(1)

    if os.path.isfile(file_path):
        print("Successfully compiled :-)\nOpening the file...")
        print("=" * 70)
        print()
        open_file = "./" + file_path
        subprocess.call([open_file])
    else:
        raise ValueError("%s isn't a file!" % file_path)


parser = argparse.ArgumentParser(description=data["__description__"])
# parser.add_argument("input", help="Name of the c++ file")
parser.add_argument(
    "-o", "--out", help="Specify the compiled file's name")
parser.add_argument('-V','--version', action='version', version=data["__name__"] + " : " + data["__version__"])


# parser.add_argument()
# parser.add_argument("-u", "--upgrade",help="Upgrade the C++ compiler", default="11")


args = parser.parse_args()

print("Compiling " + args.input + " ... ")
time.sleep(0.5)
if args.out:
    subprocess.call(["g++", str(args.input), "-o", str(args.out)])
    open_file((str(args.out) + ".exe"))
else:
    subprocess.call(["g++", args.input])
    open_file("a.exe")
