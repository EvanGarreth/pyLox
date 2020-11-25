import sys

class LoxError:
    had_error = False

    @staticmethod
    def error(line, message):
        LoxError._report(line, "", message)

    @staticmethod
    def _report(line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        LoxError.had_error = True