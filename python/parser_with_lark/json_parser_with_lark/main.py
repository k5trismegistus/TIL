from lark import Lark, Transformer

class JSONTransformer(Transformer):
    def list(self, items):
        return list(items)

    def pair(self, items):
        return items[0], items[1]

    def dict(self, items):
        return dict(items)

    def number(self, items):
        return float(items[0])

    def string(self, items):
        return items[0][1:-1]

    def true(self, _):
        return True

    def false(self, _):
        return False

    def null(self, _):
        return None

rule = open('grammer.txt').read()

json_parser = Lark(rule, start='value', parser='lalr', transformer=JSONTransformer())

t = json_parser.parse('{"key": [], "key3": true}')

print(t)

