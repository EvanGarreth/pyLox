from .token import Token
from .token_type import Token_Type as TT

class Scanner(object):
    _source = None
    _tokens = []
    _start = 0
    _current = 0
    _line = 0
    _keywords = {
        "and": TT.AND,
        "class": TT.CLASS,
        "else": TT.ELSE,
        "false": TT.FALSE,
        "for": TT.FOR,
        "fun": TT.FUN,
        "if": TT.IF,
        "nil": TT.NIL,
        "or": TT.OR,
        "print": TT.PRINT,
        "return": TT.RETURN,
        "super": TT.SUPER,
        "this": TT.THIS,
        "true": TT.TRUE,
        "var": TT.VAR,
        "while": TT.WHILE,
    }

    def __init__(self, source):
        self._source = source

    def scan_tokens(self):
        while not self._is_at_end():
            self._start = self._current
            self._scan_token()
        
        eof_token = Token(TT.EOF, "", None, self._line)
        self._tokens.append(eof_token)
        return self._tokens

    def _scan_token(self):
        character = self._advance()

        # do nothing for meaningless characters
        if character in [' ', '\r', '\t']:
            return
        if character == '\n':
            self._line += 1
            return

        # match everything but numbers and identifiers
        token_type = {
            # single character tokens
            '(': TT.LPAREN,
            ')': TT.RPAREN,
            '{': TT.LBRACE,
            '}': TT.RBRACE,
            ',': TT.COMMA,
            '.': TT.DOT,
            '-': TT.MINUS,
            '+': TT.PLUS,
            ';': TT.SEMICOLON,
            '*': TT.STAR,

            # will peek ahead to verify below, since these could potentially be 2 character tokens
            '!': TT.NOT,
            '=': TT.ASSIGN,
            '<': TT.LT,
            '>': TT.GT,

            # catch these and test them after
            '/': TT.SLASH,
            '"': TT.STRING,
        }

        # check for a number or identifier, otherwise announce an error
        if (token := token_type.get(character)) is None:
            print(token)
            if self._is_digit(character):
                self._number()
            elif self._is_alpha(character):
                self._identifier()
            else:
                print(self._line, f"Unexpected character '{character}'.")
                #.error(self._line, "Unexpected character '{character}'.")
            return
    
        if token is TT.NOT and self._match('='):
            token = TT.NOTEQUAL
        elif token == TT.ASSIGN and self._match('='):
            token = TT.EQUAL
        elif token == TT.LT and self._match('='):
            token = TT.LE
        elif token == TT.GT and self._match('='):
            token = TT.GE

        # check if the slash is for a comment and consume the rest of the line if so
        if token == TT.SLASH and self._match('/'):
            while self._peek() != '\n' and not self._is_at_end():
                self._advance()
        elif token == TT.STRING:
            self._string()
        else:
            self._add_token(token)

    def _identifier(self):
        while self._is_alphanumeric(self._peek()):
            self._advance()

        text = self._source[self._start:self._current]
        # determine if type is a keyword or user defined identifier
        if (ttype := self._keywords.get(text)) is None:
            ttype = TT.IDENTIFIER

        self._add_token(ttype)
    
    def _number(self):
        while self._is_digit(self._peek()):
            self._advance()
        
        # check for a (single) fractional part
        if self._peek() == '.' and self._is_digit(self._peek_next()):
            # consume the dot
            self._advance()

            while self._is_digit(self._peek()):
                self._advance()
        
        number = self._source[self._start:self._current]
        self.__add_token(TT.NUMBER, float(number))

    def _string(self):
        while self._peek() != '"' and not self._is_at_end():
            if self._peek() == '\n':
                self._line += 1
            self._advance()

        if self._is_at_end():
            print(self._line, "Unterminated string.")
            #.error(self._line, "Unterminated string.")
            return
        
        self._advance()

        value = self._source[self._start + 1:self._current - 1]
        self.__add_token(TT.STRING, value)

    def _match(self, expected):
        if self._is_at_end():
            return False
        if self._source[self._current] != expected:
            return False
        
        self._current += 1
        return True

    def _peek(self):
        if self._is_at_end():
            return '\0'
        return self._source[self._current]

    def _peek_next(self):
        if self._current + 1 >= len(self._source):
            return '\0'
        return self._source[self._current + 1]

    def _is_alpha(self, c):
        return c.isalnum() or c == '_'

    def _is_alphanumeric(self, c):
        return self._is_alpha(c) or self._is_digit(c)

    def _is_digit(self, c):
        return c.isdigit()

    def _is_at_end(self):
        return self._current >= len(self._source)

    def _advance(self):
        self._current += 1
        return self._source[self._current - 1]

    def _add_token(self, ttype):
        self.__add_token(ttype, None)

    def __add_token(self, ttype, literal):
        text = self._source[self._start:self._current]
        self._tokens.append(Token(ttype, text, literal, self._line))
