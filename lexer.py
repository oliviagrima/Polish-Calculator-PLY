import sys
import ply.lex as lex
import ply.yacc as yacc

class LexerClass():
    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = (
    'ENTERO', 'REAL', 'BINARIO', 'HEXADECIMAL',
    'MAS', 'MENOS', 'MULT', 'DIV',
    'NEG', 'EXP', 'LOG', 'SIN', 'COS'
    )

    t_MAS = r'\+'
    t_MENOS = r'-'
    t_MULT = r'\*'
    t_DIV = r'/'

    def t_REAL(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_BINARIO(self, t):
        r'0b[01]+'
        t.value = int(t.value, 2)
        return t

    def t_HEXADECIMAL(self, t):
        r'0x[A-F0-9]+'
        t.value = int(t.value, 16)
        return t
    
    def t_ENTERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_NEG(self, t):
        r'neg'
        return t
    
    def t_EXP(self, t):
        r'exp'
        return t
    
    def t_LOG(self, t):
        r'log'
        return t
    
    def t_SIN(self, t):
        r'sin'
        return t

    def t_COS(self, t):
        r'cos'
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    t_ignore_COMMENT = r'\#.*'
    t_ignore_MULTI_COMMENT = r"'''(.|\n)*?'''"
    t_ignore = ' \t'

    def t_error(self, t):
        print("Lexer error", t.value)
        t.lexer.skip(1)

    lexer = lex.lex()

    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token.type, token.value)
    
            