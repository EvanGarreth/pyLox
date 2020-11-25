__version__ = '0.0.1'

import sys, os
from pathlib import Path
from .scanner import Scanner
from .error import LoxError

class Lox(object):
    def __init__(self):
        self.error = LoxError()

    def run_file(self, filename):
        filename = Path(filename)
        with open(filename, 'r') as file:
            data = file.read()
        self.run(data)

        if self.error.had_error:
            sys.exit(os.EX_DATAERR)

    def run_prompt(self):
        while True:
            data = input("> ")
            if data == "":
                break
            self.run(data)
            self.error.had_error = False

    def run(self, data):
        scanner = Scanner(data)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)
