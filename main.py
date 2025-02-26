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
    content = file.read()
    ####l.test(content)
    p.test(content)