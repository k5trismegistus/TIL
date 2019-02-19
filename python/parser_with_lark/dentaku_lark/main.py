import sys
from lark import Lark, Transformer

class Calculator(Transformer):
    def addition(self, items):
        return items[0] + items[1]

    def substraction(self, items):
        return items[0] - items[1]

    def multiplication(self, items):
        return items[0] * items[1]

    def divisiton(self, items):
        return items[0] / items[1]

    def fact(self, items):
        return float(items[0])

    def number(self, items):
        return float(items[0])

if __name__ == '__main__':
    expression = ' '.join(sys.argv[1:])

    rule = open('grammer.txt').read()
    calc_parser = Lark(rule, start='expr', parser='lalr')
    tree = calc_parser.parse(expression)

    print(tree.pretty())
    result = Calculator().transform(tree)
    print(f'計算結果: {result}')
