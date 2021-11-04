import sys
from antlr4 import *
#from compiladorLexer import compiladorLexer
#from compiladorParser import compiladorParser
from fechasLexer import fechasLexer
from fechasParser import fechasParser

def main(argv):
    archivo = "../../entrada.txt" #entrada.txt
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = fechasLexer(input)
    stream = CommonTokenStream(lexer)
    parser = fechasParser(stream)
    tree = parser.s()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)