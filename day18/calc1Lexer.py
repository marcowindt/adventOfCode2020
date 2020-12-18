# Generated from calc1.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("(\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\6\t#\n\t\r\t\16\t$\3\t\3\t\2\2")
        buf.write("\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\3\5\2\13\f\17")
        buf.write("\17\"\"\2(\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\3\23\3\2\2\2\5\25\3\2\2\2\7\27\3\2\2\2\t\31\3\2\2\2")
        buf.write("\13\33\3\2\2\2\r\35\3\2\2\2\17\37\3\2\2\2\21\"\3\2\2\2")
        buf.write("\23\24\7-\2\2\24\4\3\2\2\2\25\26\7/\2\2\26\6\3\2\2\2\27")
        buf.write("\30\7,\2\2\30\b\3\2\2\2\31\32\7\61\2\2\32\n\3\2\2\2\33")
        buf.write("\34\7*\2\2\34\f\3\2\2\2\35\36\7+\2\2\36\16\3\2\2\2\37")
        buf.write(" \4\62;\2 \20\3\2\2\2!#\t\2\2\2\"!\3\2\2\2#$\3\2\2\2$")
        buf.write("\"\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\b\t\2\2\'\22\3\2\2\2")
        buf.write("\4\2$\3\2\3\2")
        return buf.getvalue()


class calc1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIV = 4
    LPAR = 5
    RPAR = 6
    DIGIT = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "TIMES", "DIV", "LPAR", "RPAR", "DIGIT", "WS" ]

    ruleNames = [ "PLUS", "MINUS", "TIMES", "DIV", "LPAR", "RPAR", "DIGIT", 
                  "WS" ]

    grammarFileName = "calc1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


