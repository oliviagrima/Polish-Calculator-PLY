import os
import sys
from lexer import LexerClass
from parser import ParserClass

l= LexerClass()
p= ParserClass()

if len (sys.argv) < 2:
    raise Exception('File name is missing')

file_name = sys.argv[1]
with open(file_name, 'r') as file:
    data = file.read()
    #l.test(data)
    p.test(data)

"""
resultado = p.parser.parse(data, lexer=l.lexer) 

if not resultado:
    sys.exit("Error de parser o fichero vacío")

for line, num in resultado:
    print("[Line", i, "]", resultado)
"""
"""
lines = data.strip().split('\n')
for i,line in enumerate(lines, start=1):
    resultado = p.parser.parse(line)
    if resultado is not None:
        print("[Line", i, "]", resultado)
"""