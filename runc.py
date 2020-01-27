#! /usr/bin/env python
import argparse
import subprocess
import os.path
import time
import json


with open('C:/Users/Sourav/Desktop/shell/Argparse/runc--C-CPP-auto-runner/config.json') as f:
    data = json.load(f)


def open_file(file_path, args):
    while not os.path.exists(file_path):
        time.sleep(1)

    if os.path.isfile(file_path):
        print("runc.py: Opening " + file_path + " ...")
        relative_file = "./" + file_path
        command = [relative_file]
        if args.infile:
            command.extend(["<", str(args.infile)])

        final_command = " ".join(command)  # To be able to run all at once

        print("Running : {}".format(final_command))
        print("*" * 70)

        # Making shell=True to be able to feed the input file into the binary file
        subprocess.call(final_command, shell=True)
        if args.delete:
            subprocess.call(["rm", file_path])
    else:
        raise ValueError("%s isn't a file!" % file_path)


def compile_and_run(args):
    time.sleep(0.5)
    output = (str(args.input)).split(".")[0]
    if args.out:
        output = str(args.out)

    command = ["g++", args.input, "-o", output]

    print("Running : {}".format(" ".join(command)))
    subprocess.call(command)
    # Calling open_file to open the file with given parameters
    open_file(output, args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=data["__description__"])
    parser.add_argument("input", help="Name of the c++ file")
    parser.add_argument(
        "-o", "--out", help="Specify the compiled file's name")
    parser.add_argument('-V', '--version', action='version',
                        version=data["__name__"] + " : " + data["__version__"])
    parser.add_argument(
        '-u', "--using", help="Specify the compiler version", choices=[11, 14], type=int)
    parser.add_argument("-i", "--infile", help="Give the input file")
    parser.add_argument(
        "-d", "--delete", help="Don't keep the output file", action="store_true")

    args = parser.parse_args()
    compile_and_run(args)
