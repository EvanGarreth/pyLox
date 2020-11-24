__version__ = '0.0.1'

import sys, os
from pathlib import Path
from .scanner import Scanner

class Lox(object):
    _had_error = False

    def run_file(self, filename):
        filename = Path(filename)
        with open(filename, 'r') as file:
            data = file.read()
        self.run(data)

        if self._had_error:
            sys.exit(os.EX_DATAERR)

    def run_prompt(self):
        while True:
            data = input("> ")
            if data == "":
                break
            self.run(data)
            self._had_error = False

    def run(self, data):
        scanner = Scanner(data)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    def error(self, line, message):
        self._report(line, "", message)

    def _report(self, line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        self._had_error = True
