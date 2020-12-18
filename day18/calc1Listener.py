# Generated from calc1.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calc1Parser import calc1Parser
else:
    from calc1Parser import calc1Parser

# This class defines a complete listener for a parse tree produced by calc1Parser.
class calc1Listener(ParseTreeListener):

    # Enter a parse tree produced by calc1Parser#expression.
    def enterExpression(self, ctx:calc1Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by calc1Parser#expression.
    def exitExpression(self, ctx:calc1Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by calc1Parser#number.
    def enterNumber(self, ctx:calc1Parser.NumberContext):
        pass

    # Exit a parse tree produced by calc1Parser#number.
    def exitNumber(self, ctx:calc1Parser.NumberContext):
        pass



del calc1Parser