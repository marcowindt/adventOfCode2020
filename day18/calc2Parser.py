# Generated from calc2.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("%\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\7\2\33\n\2\f\2\16\2\36\13\2\3\3\6\3!\n\3\r\3\16\3\"\3")
        buf.write("\3\2\3\2\4\2\4\2\4\3\2\3\4\3\2\5\6\2\'\2\22\3\2\2\2\4")
        buf.write(" \3\2\2\2\6\7\b\2\1\2\7\b\7\7\2\2\b\t\5\2\2\2\t\n\7\b")
        buf.write("\2\2\n\23\3\2\2\2\13\r\t\2\2\2\f\13\3\2\2\2\r\20\3\2\2")
        buf.write("\2\16\f\3\2\2\2\16\17\3\2\2\2\17\21\3\2\2\2\20\16\3\2")
        buf.write("\2\2\21\23\5\4\3\2\22\6\3\2\2\2\22\16\3\2\2\2\23\34\3")
        buf.write("\2\2\2\24\25\f\6\2\2\25\26\t\2\2\2\26\33\5\2\2\7\27\30")
        buf.write("\f\5\2\2\30\31\t\3\2\2\31\33\5\2\2\6\32\24\3\2\2\2\32")
        buf.write("\27\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\3\3\2\2\2\36\34\3\2\2\2\37!\7\t\2\2 \37\3\2\2\2!\"")
        buf.write("\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\5\3\2\2\2\7\16\22\32\34")
        buf.write("\"")
        return buf.getvalue()


class calc2Parser ( Parser ):

    grammarFileName = "calc2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "TIMES", "DIV", "LPAR", 
                      "RPAR", "DIGIT", "WS" ]

    RULE_expression = 0
    RULE_number = 1

    ruleNames =  [ "expression", "number" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    TIMES=3
    DIV=4
    LPAR=5
    RPAR=6
    DIGIT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(calc2Parser.LPAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calc2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(calc2Parser.ExpressionContext,i)


        def RPAR(self):
            return self.getToken(calc2Parser.RPAR, 0)

        def number(self):
            return self.getTypedRuleContext(calc2Parser.NumberContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(calc2Parser.PLUS)
            else:
                return self.getToken(calc2Parser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(calc2Parser.MINUS)
            else:
                return self.getToken(calc2Parser.MINUS, i)

        def TIMES(self):
            return self.getToken(calc2Parser.TIMES, 0)

        def DIV(self):
            return self.getToken(calc2Parser.DIV, 0)

        def getRuleIndex(self):
            return calc2Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calc2Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [calc2Parser.LPAR]:
                self.state = 5
                self.match(calc2Parser.LPAR)
                self.state = 6
                self.expression(0)
                self.state = 7
                self.match(calc2Parser.RPAR)
                pass
            elif token in [calc2Parser.PLUS, calc2Parser.MINUS, calc2Parser.DIGIT]:
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==calc2Parser.PLUS or _la==calc2Parser.MINUS:
                    self.state = 9
                    _la = self._input.LA(1)
                    if not(_la==calc2Parser.PLUS or _la==calc2Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 14
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 15
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 24
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = calc2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 18
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 19
                        _la = self._input.LA(1)
                        if not(_la==calc2Parser.PLUS or _la==calc2Parser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 20
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = calc2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 21
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 22
                        _la = self._input.LA(1)
                        if not(_la==calc2Parser.TIMES or _la==calc2Parser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 23
                        self.expression(4)
                        pass

             
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(calc2Parser.DIGIT)
            else:
                return self.getToken(calc2Parser.DIGIT, i)

        def getRuleIndex(self):
            return calc2Parser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = calc2Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 29
                    self.match(calc2Parser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 32 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




