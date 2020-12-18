# Generated from calc1.g4 by ANTLR 4.9
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
        buf.write("\"\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\5\2\23\n\2\3\2\3\2\3\2\7\2\30\n\2")
        buf.write("\f\2\16\2\33\13\2\3\3\6\3\36\n\3\r\3\16\3\37\3\3\2\3\2")
        buf.write("\4\2\4\2\4\3\2\3\4\3\2\3\6\2#\2\22\3\2\2\2\4\35\3\2\2")
        buf.write("\2\6\7\b\2\1\2\7\b\7\7\2\2\b\t\5\2\2\2\t\n\7\b\2\2\n\23")
        buf.write("\3\2\2\2\13\r\t\2\2\2\f\13\3\2\2\2\r\20\3\2\2\2\16\f\3")
        buf.write("\2\2\2\16\17\3\2\2\2\17\21\3\2\2\2\20\16\3\2\2\2\21\23")
        buf.write("\5\4\3\2\22\6\3\2\2\2\22\16\3\2\2\2\23\31\3\2\2\2\24\25")
        buf.write("\f\5\2\2\25\26\t\3\2\2\26\30\5\2\2\6\27\24\3\2\2\2\30")
        buf.write("\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33")
        buf.write("\31\3\2\2\2\34\36\7\t\2\2\35\34\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37\35\3\2\2\2\37 \3\2\2\2 \5\3\2\2\2\6\16\22\31\37")
        return buf.getvalue()


class calc1Parser ( Parser ):

    grammarFileName = "calc1.g4"

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
            return self.getToken(calc1Parser.LPAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calc1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(calc1Parser.ExpressionContext,i)


        def RPAR(self):
            return self.getToken(calc1Parser.RPAR, 0)

        def number(self):
            return self.getTypedRuleContext(calc1Parser.NumberContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(calc1Parser.PLUS)
            else:
                return self.getToken(calc1Parser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(calc1Parser.MINUS)
            else:
                return self.getToken(calc1Parser.MINUS, i)

        def TIMES(self):
            return self.getToken(calc1Parser.TIMES, 0)

        def DIV(self):
            return self.getToken(calc1Parser.DIV, 0)

        def getRuleIndex(self):
            return calc1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calc1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [calc1Parser.LPAR]:
                self.state = 5
                self.match(calc1Parser.LPAR)
                self.state = 6
                self.expression(0)
                self.state = 7
                self.match(calc1Parser.RPAR)
                pass
            elif token in [calc1Parser.PLUS, calc1Parser.MINUS, calc1Parser.DIGIT]:
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==calc1Parser.PLUS or _la==calc1Parser.MINUS:
                    self.state = 9
                    _la = self._input.LA(1)
                    if not(_la==calc1Parser.PLUS or _la==calc1Parser.MINUS):
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
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = calc1Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 18
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 19
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << calc1Parser.PLUS) | (1 << calc1Parser.MINUS) | (1 << calc1Parser.TIMES) | (1 << calc1Parser.DIV))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 20
                    self.expression(4) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
                return self.getTokens(calc1Parser.DIGIT)
            else:
                return self.getToken(calc1Parser.DIGIT, i)

        def getRuleIndex(self):
            return calc1Parser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = calc1Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 26
                    self.match(calc1Parser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 29 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
                return self.precpred(self._ctx, 3)
         




