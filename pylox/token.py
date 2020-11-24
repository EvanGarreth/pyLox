class Token:
    token_type = None
    lexeme = None
    literal = None
    line = None

    def __init__(self, token_type, lexeme, literal, line):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self):
        return f"Token(token_type='{self.token_type}', \
            lexeme='{self.lexeme}', \
            literal='{self.literal}', \
            line='{self.line}')"

    def __str__(self):
        return f"{self.token_type}, {self.lexeme}, {self.literal}"
