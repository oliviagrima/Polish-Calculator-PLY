"""
P1 - Procesadores del Lenguaje
Olivia Grima Pérez e Íñigo García-Velasco González
"""

from lexer import LexerClass
import ply.yacc as yacc
import math

class ParserClass:
    
    tokens = LexerClass.tokens

    def __init__(self):
        self.lexer = LexerClass()
        self.parser = yacc.yacc(module=self)
        self.memory = {"{MEMORY}": 0}

    def p_program(self, p):
        ''' program : lista_expresiones 
                    | empty'''
        p[0] = p[1]

    def p_lista_expresiones(self, p):
        '''
        lista_expresiones : expresion lista_expresiones
                        | expresion
        '''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]  
    
    def p_empty(self, p):
        ''' empty : '''
        p[0] = []

    def p_exp_binaria(self, p):
        '''
        expresion : MAS expresion expresion
                   | MENOS expresion expresion 
                   | MULT expresion expresion 
                   | DIV expresion expresion  
        '''
        if isinstance(p[2], list):
            val2 = p[2][0]
        else:
            val2 = p[2]

        if isinstance(p[2], list):
            val3 = p[3][0]
        else:
            val3 = p[3]
       
        if isinstance(val2, tuple):
            val2 = val2[1]

        if isinstance(val3, tuple):
            val3 = val3[1]
        
        if p[1] == '+':
            if val2 == "inf" and val3 == "inf":
                resultado = "inf"
            elif (val2 == "inf" and val3 == "-inf") or (val2 == "-inf" and val3 == "inf"):
                resultado = "nan"
            elif val2 == "nan" or val3 == "nan":
                resultado = "nan"
            elif val2 == "-inf" and val3 == "-inf":
                resultado = "-inf"
            elif val2 == "inf" or val3 == "inf":
                resultado = "inf"
            elif val2 == "-inf" or val3 == "-inf":
                resultado = "-inf"
            else:
                resultado = val2 + val3 

        elif p[1] == '-':
            if (val2 == "-inf" and val3 == "-inf") or (val2 == "inf" and val3 == "inf"):
                resultado = "nan"
            elif val2 == "nan" or val3 == "nan":
                resultado = "nan"
            elif val2 == "inf" and val3 == "-inf":
                resultado = "inf"
            elif val2 == "-inf" and val3 == "inf":
                resultado = "-inf"
            elif val2 == "-inf" or val3 == "inf":
                resultado = "-inf"
            elif val2 == "inf" or val3 == "-inf":
                resultado = "inf"
            else:
                resultado = val2 - val3 

        elif p[1] == '*':
            if val2 == "inf" and val3 == "inf":
                resultado = "inf"
            elif (val2 == "inf" and val3 == "-inf") or (val2 == "-inf" and val3 == "inf"):
                resultado = "-inf"
            elif val2 == "-inf" and val3 == "-inf":
                resultado= "inf"
            elif val2 == "nan" or val3 == "nan":
                resultado = "nan"
            elif (val2 == "inf" and val3 == 0) or (val2 == 0 and val3 == "inf") or (val2 == "-inf" and val3 == 0) or (val2 == 0 and val3 == "-inf"):
                resultado = "nan"
            elif (val2 == "inf" and val3 < 0) or (val2 < 0 and val3 == "inf"):
                resultado = "-inf"
            elif (val2 == "-inf" and val3 < 0) or (val2 < 0 and val3 == "-inf"):
                resultado = "inf"
            elif (val2 == "-inf" and val3 > 0) or (val2 > 0 and val3 == "-inf"):
                resultado = "-inf"
            elif  (val2 == "inf" and val3 > 0) or (val2 > 0 and val3 == "inf"):
                resultado = "inf"
            else:
                resultado = val2 * val3 

        elif p[1] == '/':
            if (val2 == "inf" and val3 == "inf") or (val2 == "-inf" and val3 == "-inf") or (val2 == "inf" and val3 == "-inf") or (val2 == "-inf" and val3 == "inf"):
                resultado = "nan"
            elif val2 == "nan" or val3 == "nan":
                resultado = "nan"
            elif (val2 == "inf" and val3 > 0) or (val2 == "-inf" and val3 < 0):
                resultado = "inf"
            elif (val2 == "-inf" and val3 > 0) or (val2 == "inf" and val3 < 0):
                resultado = "-inf"
            elif val3 == "inf" or val3 == "-inf":
                resultado = 0
            elif val3 == 0:
                if val2 == 0:
                    resultado = "nan"
                else:
                    resultado = "inf"
            else:
                resultado = val2 / val3 

        else:
            resultado = "nan"
        
        p[0] = [(p.lineno(1), resultado)]
    
    def p_exp_unaria(self, p):
        '''
        expresion : NEG expresion
                   | EXP expresion
                   | LOG expresion
                   | SIN expresion
                   | COS expresion
        '''
        if isinstance(p[2], list):
            val2 = p[2][0]
        else:
            val2 = p[2]
        
        if isinstance(val2, tuple):
            val2 = val2[1]
       
        if p[1] == 'neg':
            if val2 == "inf":
                resultado = "-inf"
            elif val2 == "nan":
                resultado = "nan"
            else:
                resultado = -val2
        elif p[1] == 'exp':
            if val2 == "inf" or val2 == "-inf" or val2 == "nan":
                resultado = "nan"
            else:
                resultado = math.exp(val2)
        elif p[1] == 'log':
            if isinstance(val2, str):
                if val2 == "inf":
                    resultado = "inf"
                elif val2 == "-inf" or val2 == "nan":
                    resultado = "nan"
                else:
                    resultado = "nan"
            else: 
                if val2 <= 0:
                    resultado = "nan"
                else:
                    resultado = math.log10(val2)
        elif p[1] == 'sin':
            if val2 == "inf" or val2 == "-inf" or val2 == "nan":
                resultado = "nan"
            else:
                resultado = math.sin(val2)
        elif p[1] == 'cos':
            if val2 == "inf" or val2 == "-inf" or val2 == "nan":
                resultado = "nan"
            else:
                resultado = math.cos(val2)
        else:
            resultado = "nan"

        p[0] = [(p.lineno(1), resultado)]

    def p_exp_numero(self, p):
        '''
        expresion : ENTERO
                    | REAL
                    | BINARIO
                    | HEXADECIMAL
                    | INF
                    | NAN
        '''
        p[0] = [(p.lineno(1), p[1])]

    def p_exp_variable(self, p):
        '''
        expresion : MEMORY
        '''
        p[0] = [(p.lineno(1), self.memory["{MEMORY}"])]

    def p_exp_memory(self, p):
        '''
        expresion : MEMORY IGUAL expresion
        '''

        if isinstance(p[3], list):
            self.memory["{MEMORY}"] = p[3][0][1]
        else:
            val2 = p[3]

        p[0] = [(p.lineno(1), self.memory["{MEMORY}"])]

    def p_error(self, p):
        print("[Syntax error]: Error en la sintaxis de entrada")

    def test(self, data):
        resultado = self.parser.parse(data, lexer=self.lexer.lexer)
        if resultado:
            for line, result in resultado:
                print("[Line", line, "]", result)
        else:
            print("[Parser error]: No se ha podido procesar la entrada")