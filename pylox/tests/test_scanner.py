import pytest

#from .. import Lox
from ..scanner import Scanner
from ..token_type import Token_Type as TT

@pytest.mark.parametrize("data,expected",
    [
        (
            '(){},.-+;*123.456',
            [
                TT.LPAREN,
                TT.RPAREN,
                TT.LBRACE,
                TT.RBRACE,
                TT.COMMA,
                TT.DOT,
                TT.MINUS,
                TT.PLUS,
                TT.SEMICOLON,
                TT.STAR,
                TT.NUMBER,
                TT.EOF,
            ]
        ),
        (
            '!!====<<=>>=',
            [
                TT.NOT,
                TT.NOTEQUAL,
                TT.EQUAL,
                TT.ASSIGN,
                TT.LT,
                TT.LE,
                TT.GT,
                TT.GE,
                TT.EOF,
            ]
        ),
        (
            'and class else false for fun if nil or print return super this true var while',
            [
                TT.AND,
                TT.CLASS,
                TT.ELSE,
                TT.FALSE,
                TT.FOR,
                TT.FUN,
                TT.IF,
                TT.NIL,
                TT.OR,
                TT.PRINT,
                TT.RETURN,
                TT.SUPER,
                TT.THIS,
                TT.TRUE,
                TT.VAR,
                TT.WHILE,
                TT.EOF
            ]
        ),
        ('', [TT.EOF,]),
        ('"test string"', [TT.STRING, TT.EOF]),
        ('"Unterminated string', [TT.EOF]),
        ('// comment line', [TT.EOF]),
        ('variable = 123', [TT.IDENTIFIER, TT.ASSIGN, TT.NUMBER, TT.EOF]),
    ]
)
def test_scanner(data, expected):
    scanner = Scanner(data)
    # clear tokens for testing. Otherwise the list will expand with each further test.
    # can't think of an alternative to this since that functionality is kind of integral to the REPL
    scanner._tokens = []
    tokens = scanner.scan_tokens()
    for i,token in enumerate(tokens):
        assert token.token_type == expected[i]