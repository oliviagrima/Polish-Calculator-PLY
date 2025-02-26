from lexer import LexerClass
import ply.yacc as yacc
import math

class ParserClass:
    
    tokens = LexerClass.tokens

    def __init__(self):
        self.lexer = LexerClass()
        self.parser = yacc.yacc(module=self)

    def p_exp_binaria(self, p):
        '''
        expresion : MAS expresion expresion
                   | MENOS expresion expresion 
                   | MULT expresion expresion 
                   | DIV expresion expresion 
        '''
        if p[1] == '+':
            p[0] = p[2] + p[3]
        elif p[1] == '-':
            p[0] = p[2] - p[3]
        elif p[1] == '*':
            p[0] = p[2] * p[3]
        elif p[1] == '/':
            if p[3] == 0:
                raise ZeroDivisionError("nan")
            else:
                p[0] = p[2] / p[3]
    
    def p_exp_unaria(self, p):
        '''
        expresion : NEG expresion
                   | EXP expresion
                   | LOG expresion
                   | SIN expresion
                   | COS expresion
        '''
        if p[1] == 'neg':
            p[0] = -p[2]
        elif p[1] == 'exp':
            p[0] = math.exp(p[2])
        elif p[1] == 'log':
            if p[2] <= 0:
                raise ValueError("nan")
            else:
                p[0] = math.log10(p[2])
        elif p[1] == 'sin':
            p[0] = math.sin(p[2])
        elif p[1] == 'cos':
            p[0] = math.cos(p[2])

    def p_exp_numero(self, p):
        '''
        expresion : ENTERO
                    | REAL
                    | BINARIO
                    | HEXADECIMAL
        '''
        p[0] = p[1]

    def p_error(self, p):
        print("[Parser error]: Error en la sintaxis de entrada")

    def test(self, data):
        self.parser.parse(data)