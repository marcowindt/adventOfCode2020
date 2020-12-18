# Generated from calc2.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calc2Parser import calc2Parser
else:
    from calc2Parser import calc2Parser

# This class defines a complete listener for a parse tree produced by calc2Parser.
class calc2Listener(ParseTreeListener):

    # Enter a parse tree produced by calc2Parser#expression.
    def enterExpression(self, ctx:calc2Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by calc2Parser#expression.
    def exitExpression(self, ctx:calc2Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by calc2Parser#number.
    def enterNumber(self, ctx:calc2Parser.NumberContext):
        pass

    # Exit a parse tree produced by calc2Parser#number.
    def exitNumber(self, ctx:calc2Parser.NumberContext):
        pass



del calc2Parser