import ply.lex as lex
import ply.yacc as yacc

class LexerClass():

    tokens = (
    'ENTERO', 'REAL', 'BINARIO', 'HEXADECIMAL',
    'MAS', 'MENOS', 'MULT', 'DIV',
    'NEG', 'EXP', 'LOG', 'SIN', 'COS'
    )

    t_MAS = r'\+'
    t_MENOS = r'-'
    t_MULT = r'\*'
    t_DIV = r'/'

    def __init__(self):
        self.lexer = lex.lex(module=self)

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

    def t_ignore_SINGLE_COMMENT(self, t):
        r'\#.*'
        pass

    def t_ignore_MULTI_COMMENT(self, t):
        r"'''(.|\n)*?'''"
        pass
    
    t_ignore = ' \t\n'

    def t_error(self, t):
        print("[Lexer error]: Error en el valor", t.value)
        t.lexer.skip(1)

    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token.type, token.value)