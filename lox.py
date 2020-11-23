#!/usr/bin/env python3
import sys
from pathlib import Path

def run_file(filename):
    filename = Path(filename)
    with open(filename, 'r') as file:
        data = file.read()
    run(data)

def run_prompt():
    while True:
        data = input("> ")
        if data == "":
            break
        run(data)

def run(data):
    tokens = data.split()
    for token in tokens:
        print(token)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f"Usage: {sys.argv[0]} [script]")
        sys.exit(64) # EX_USAGE, command used incorrectly. From UNIX sysexits.h
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()

    