#! /usr/bin/env python
import argparse
import subprocess
import os.path
import time
import json


with open('./config.json') as f:
    data = json.load(f)


def open_file(file_path, delete):
    while not os.path.exists(file_path):
        time.sleep(1)

    if os.path.isfile(file_path):
        print("2) Successfully compiled :-)\n3) Opening the file...")
        print("=" * 70)
        print("")
        open_file = "./" + file_path
        subprocess.call([open_file])
        if delete:
            subprocess.call(["rm", file_path])
    else:
        raise ValueError("%s isn't a file!" % file_path)


def compile_and_run(args):
    print("1) Compiling " + args.input + " ... ")
    time.sleep(0.5)
    command = ["g++", args.input]
    output = "a.exe"
    if args.out:
        output = str(args.out)
        command.extend(["-o", str(args.out)])

    subprocess.call(command)
    open_file(output, args.delete)

    # if args.out and not args.using and not args.inf:
    #     subprocess.call(["g++", str(args.input), ])
    #     open_file((str(args.out) + ".exe"))
    # else:


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=data["__description__"])
    parser.add_argument("input", help="Name of the c++ file")
    parser.add_argument(
        "-o", "--out", help="Specify the compiled file's name")
    parser.add_argument('-V', '--version', action='version',
                        version=data["__name__"] + " : " + data["__version__"])
    parser.add_argument(
        '-u', "--using", help="Specify the compiler version", choices=[11, 14], type=int)
    parser.add_argument("-i", "--inf", help="Give the input file", type=str)
    parser.add_argument("-d", "--delete", help="Don't keep the output file", action="store_true")

    args = parser.parse_args()
    compile_and_run(args)
