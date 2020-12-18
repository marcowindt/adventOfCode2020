import os

from day18.calc1Lexer import calc1Lexer
from day18.calc1Parser import calc1Parser
from day18.calc2Lexer import calc2Lexer
from day18.calc2Parser import calc2Parser
import antlr4


TEST_EXPRESSIONS = """1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""


def handle_expression(expr):
    if expr.getChildCount() == 3:
        if expr.getChild(1).getText() == "+":
            return handle_expression(expr.getChild(0)) + handle_expression(expr.getChild(2))
        if expr.getChild(1).getText() == "-":
            return handle_expression(expr.getChild(0)) - handle_expression(expr.getChild(2))
        if expr.getChild(1).getText() == "*":
            return handle_expression(expr.getChild(0)) * handle_expression(expr.getChild(2))
        if expr.getChild(0).getText() == '(' and expr.getChild(2).getText() == ')':
            return handle_expression(expr.getChild(1))
        print(expr.getText())
    else:
        return int(expr.getText())


def solution():
    # expressions = TEST_EXPRESSIONS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        expressions = fd.read()

    # PART ONE
    s = 0
    for expression in expressions.splitlines():
        lexer = calc1Lexer(antlr4.InputStream(expression))
        stream = antlr4.CommonTokenStream(lexer)
        parser = calc1Parser(stream)
        tree = parser.expression()
        result = handle_expression(tree)
        s += result
    print("1:", s)

    # PART TWO
    s = 0
    for expression in expressions.splitlines():
        lexer = calc2Lexer(antlr4.InputStream(expression))
        stream = antlr4.CommonTokenStream(lexer)
        parser = calc2Parser(stream)
        tree = parser.expression()
        result = handle_expression(tree)
        s += result
    print("2:", s)


if __name__ == '__main__':
    # to get lexer and parser run: $ java -Xmx500M -cp antlr4.jar org.antlr.v4.Tool -Dlanguage=Python3 calc1.g4
    #                              $ java -Xmx500M -cp antlr4.jar org.antlr.v4.Tool -Dlanguage=Python3 calc2.g4
    solution()
