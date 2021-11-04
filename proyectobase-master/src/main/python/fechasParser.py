# Generated from /home/marcos/Descargas/DHS/proyectobase-master/src/main/python/fechas.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\16\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\f\n\2\3\2")
        buf.write("\2\2\3\2\2\2\2\16\2\13\3\2\2\2\4\5\7\3\2\2\5\6\b\2\1\2")
        buf.write("\6\f\5\2\2\2\7\b\7\4\2\2\b\t\b\2\1\2\t\f\5\2\2\2\n\f\7")
        buf.write("\2\2\3\13\4\3\2\2\2\13\7\3\2\2\2\13\n\3\2\2\2\f\3\3\2")
        buf.write("\2\2\3\13")
        return buf.getvalue()


class fechasParser ( Parser ):

    grammarFileName = "fechas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "FECHA_BUSCADA", "FECHA", "WS" ]

    RULE_s = 0

    ruleNames =  [ "s" ]

    EOF = Token.EOF
    FECHA_BUSCADA=1
    FECHA=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._FECHA_BUSCADA = None # Token
            self._FECHA = None # Token

        def FECHA_BUSCADA(self):
            return self.getToken(fechasParser.FECHA_BUSCADA, 0)

        def s(self):
            return self.getTypedRuleContext(fechasParser.SContext,0)


        def FECHA(self):
            return self.getToken(fechasParser.FECHA, 0)

        def EOF(self):
            return self.getToken(fechasParser.EOF, 0)

        def getRuleIndex(self):
            return fechasParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = fechasParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.state = 9
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fechasParser.FECHA_BUSCADA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                localctx._FECHA_BUSCADA = self.match(fechasParser.FECHA_BUSCADA)
                print("FECHA_BUSCADA ->" + (None if localctx._FECHA_BUSCADA is None else localctx._FECHA_BUSCADA.text))
                self.state = 4
                self.s()
                pass
            elif token in [fechasParser.FECHA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 5
                localctx._FECHA = self.match(fechasParser.FECHA)
                print("FECHA ->" + (None if localctx._FECHA is None else localctx._FECHA.text))
                self.state = 7
                self.s()
                pass
            elif token in [fechasParser.EOF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 8
                self.match(fechasParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





