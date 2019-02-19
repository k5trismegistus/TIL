import sys
from lark import Lark, Transformer

class Calculator(Transformer):
    def __init__(self):
        self.variables = dict()

    def program(self, items):
        return items[-1]

    def assignment(self, items):
        self.variables[items[0]] = items[1]

    def new_symbol(self, items):
        return items[0]

    def addition(self, items):
        return items[0] + items[1]

    def substraction(self, items):
        return items[0] - items[1]

    def multiplication(self, items):
        return items[0] * items[1]

    def divisiton(self, items):
        return items[0] / items[1]

    def symbol(self, items):
        return self.variables.get(items[0], 0)

    def number(self, items):
        return float(items[0])

if __name__ == '__main__':
    program = open('program.txt').read()

    rule = open('grammer.txt').read()
    calc_parser = Lark(rule, start='program', parser='lalr')
    calculator = Calculator()
    tree = calc_parser.parse(program)

    print(tree.pretty())
    result = calculator.transform(tree)

    print(f'計算結果: {result}')
