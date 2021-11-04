# Generated from /home/marcos/Descargas/DHS/proyectobase-master/src/main/python/fechas.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fechasParser import fechasParser
else:
    from fechasParser import fechasParser

# This class defines a complete generic visitor for a parse tree produced by fechasParser.

class fechasVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fechasParser#s.
    def visitS(self, ctx:fechasParser.SContext):
        return self.visitChildren(ctx)



del fechasParser