#!/usr/bin/env python3
from . import Lox
import sys, os
from pathlib import Path

if __name__ == "__main__":
    lox = Lox()
    if len(sys.argv) > 2:
        print(f"Usage: {sys.argv[0]} [script]")
        sys.exit(os.EX_USAGE)
    elif len(sys.argv) == 2:
        lox.run_file(sys.argv[1])
    else:
        lox.run_prompt()

    sys.exit(os.EX_OK)