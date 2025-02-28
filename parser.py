from lexer import LexerClass
import ply.yacc as yacc
import math

class ParserClass:
    
    tokens = LexerClass.tokens

    def __init__(self):
        self.lexer = LexerClass()
        self.parser = yacc.yacc(module=self)
        self.memory = {"{MEMORY}": 0}

    precedence = (
        ('left', 'MAS', 'MENOS'),
        ('left', 'MULT', 'DIV'),
        ('right','NEG', 'EXP', 'LOG', 'SIN', 'COS')
        )

    def p_exp_binaria(self, p):
        '''
        expresion : MAS expresion expresion
                   | MENOS expresion expresion 
                   | MULT expresion expresion 
                   | DIV expresion expresion  
        '''
        if p[1] == '+':
            if p[2] == "inf" and p[3] == "inf":
                    p[0] = "inf"
            elif (p[2] == "inf" and p[3] == "-inf") or (p[2] == "-inf" and p[3] == "inf"):
                    p[0] = "nan"
            elif p[2] == "nan" or p[3] == "nan":
                p[0] = "nan"
            elif p[2] == "-inf" and p[3] == "-inf":
                    p[0] = "-inf"
            elif p[2] == "inf" or p[3] == "inf":
                    p[0] = "inf"
            elif p[2] == "-inf" or p[3] == "-inf":
                    p[0] = "-inf"
            else:
                p[0] = p[2] + p[3]

        elif p[1] == '-':
            if (p[2] == "-inf" and p[3] == "-inf") or (p[2] == "inf" and p[3] == "inf"):
                    p[0] = "nan"
            elif p[2] == "nan" or p[3] == "nan":
                p[0] = "nan"
            elif p[2] == "inf" and p[3] == "-inf":
                    p[0] = "inf"
            elif p[2] == "-inf" and p[3] == "inf":
                    p[0] = "-inf"
            elif p[2] == "-inf" or p[3] == "inf":
                    p[0] = "-inf"
            elif p[2] == "inf" or p[3] == "-inf":
                    p[0] = "inf"
            else:
                p[0] = p[2] - p[3]

        elif p[1] == '*':
            if p[2] == "inf" and p[3] == "inf":
                p[0] = "inf"
            elif (p[2] == "inf" and p[3] == "-inf") or (p[2] == "-inf" and p[3] == "inf"):
                p[0] = "-inf"
            elif p[2] == "-inf" and p[3] == "-inf":
                p[0] = "inf"
            elif p[2] == "nan" or p[3] == "nan":
                p[0] = "nan"
            elif (p[2] == "inf" and p[3] == 0) or (p[2] == 0 and p[3] == "inf") or (p[2] == "-inf" and p[3] == 0) or (p[2] == 0 and p[3] == "-inf"):
                p[0] = "nan"
            elif (p[2] == "inf" and p[3] < 0) or (p[2] < 0 and p[3] == "inf"):
                p[0] = "-inf"
            elif (p[2] == "-inf" and p[3] < 0) or (p[2] < 0 and p[3] == "-inf"):
                p[0] = "inf"
            elif (p[2] == "-inf" and p[3] > 0) or (p[2] > 0 and p[3] == "-inf"):
                p[0] = "-inf"
            elif  (p[2] == "inf" and p[3] > 0) or (p[2] > 0 and p[3] == "inf"):
                p[0] = "inf"
            else:
                p[0] = p[2] * p[3]

        elif p[1] == '/':
            if (p[2] == "inf" and p[3] == "inf") or (p[2] == "-inf" and p[3] == "-inf") or (p[2] == "inf" and p[3] == "-inf") or (p[2] == "-inf" and p[3] == "inf"):
                p[0] = "nan"
            elif p[2] == "nan" or p[3] == "nan":
                p[0] = "nan"
            elif (p[2] == "inf" and p[3] > 0) or (p[2] == "-inf" and p[3] < 0):
                p[0] = "inf"
            elif (p[2] == "-inf" and p[3] > 0) or (p[2] == "inf" and p[3] < 0):
                p[0] = "-inf"
            elif p[3] == "inf" or p[3] == "-inf":
                p[0] = 0
            elif p[3] == 0:
                p[0] = "nan"
            else:
                p[0] = p[2] / p[3]

        else:
            p[0] = "nan"
    
    def p_exp_unaria(self, p):
        '''
        expresion : NEG expresion
                   | EXP expresion
                   | LOG expresion
                   | SIN expresion
                   | COS expresion
        '''
        if p[1] == 'neg':
            if p[2] == "inf":
                p[0] = "-inf"
            else:
                p[0] = -p[2]
        elif p[1] == 'exp':
            if p[2] == "inf" or p[2] == "-inf":
                p[0] = "nan"
            else:
                p[0] = math.exp(p[2])
        elif p[1] == 'log':
            if p[2] <= 0:
                p[0] = "nan"
            else:
                p[0] = math.log10(p[2])
        elif p[1] == 'sin':
            p[0] = math.sin(p[2])
        elif p[1] == 'cos':
            p[0] = math.cos(p[2])
        else:
            p[0] = "nan"

    def p_exp_numero(self, p):
        '''
        expresion : ENTERO
                    | REAL
                    | BINARIO
                    | HEXADECIMAL
                    | INF
                    | NAN
        '''
        p[0] = p[1]

    def p_exp_variable(self, p):
        '''
        expresion : MEMORY
        '''
        p[0] = self.memory["{MEMORY}"]

    def p_exp_memory(self, p):
        '''
        expresion : MEMORY IGUAL expresion
        '''
        self.memory["{MEMORY}"] = p[3]
        p[0] = p[3]

    def p_error(self, p):
        print("[Parser error]: Error en la sintaxis de entrada")

    """
    def test(self, data):
        self.parser.parse(data, lexer=self.lexer.lexer)
    """
    """
    def test(self, data):
        lines = data.strip().split('\n')
        for i,line in enumerate(lines, start=1):
            resultado = self.parser.parse(line)
            if resultado is not None:
                print("[Line", i, "]", resultado)
    """
    
    def test(self, data):
        in_multiline_comment = False  # Bandera para detectar comentarios multilínea
        
        for i, line in enumerate(data.strip().split('\n'), start=1):
            line = line.strip()

            # Detectar inicio y fin de comentario multilínea
            if line.startswith("'''"):
                in_multiline_comment = not in_multiline_comment
                continue  # Saltar la línea que contiene ''' para que no la procese el parser

            if in_multiline_comment or not line or line.startswith('#'):
                continue  # Saltar líneas dentro de comentarios multilínea o líneas vacías
            
            # Procesar la línea con el parser
            resultado = self.parser.parse(line, lexer=self.lexer.lexer)
            if resultado is not None:
                print("[Line", i, "]", resultado)