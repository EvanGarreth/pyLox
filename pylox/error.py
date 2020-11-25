class LoxError:
    had_error = False

    @staticmethod
    def error(self, line, message):
        self._report(line, "", message)

    @staticmethod
    def _report(self, line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        self.had_error = True