import sys
from lark import Lark
from lark.tree import Tree

class Environment():
    def __init__(self, parent_env):
        self._parent_env = parent_env
        self._env = dict()

    def get(self, key):
        value = self._env.get(key, None)
        if not value:
            value = self._parent_env.get(key)
        return value

    def set(self, key, value):
        self._env[key] = value

class Function():
    def __init__(self, parameters, tree):
        self._parameters = parameters
        self._tree = tree

    def parameters(self):
        return self._parameters

    def tree(self):
            return self._tree

class Calculator():
    def __default__(self, tree, env):
        raise

    def program(self, tree, env):
        for sub_tree in tree.children:
            r = self.visit(sub_tree, env)
            if sub_tree.data == 'return_state':
                return r

    def assignment(self, tree, env):
        key = self.visit(tree.children[0], env)
        value = self.visit(tree.children[1], env)
        env.set(key, value)

    def return_state(self, tree, env):
        return self.visit(tree.children[0], env)

    def new_symbol(self, tree, env):
        return tree.children[0].value

    def parameter(self, tree, env):
        return tree.children[0].value

    def function(self, tree, env):
        key = self.visit(tree.children[0], env)
        parameters = []
        if len(tree.children) > 2:
            parameters = [self.visit(child, env) for child in tree.children[1:-1] ]
        ast = tree.children[-1]

        func = Function(parameters, ast)
        env.set(key, func)

    def function_call(self, tree, env):
        func = self.visit(tree.children[0], env)

        arguments = [self.visit(c, env) for c in tree.children[1:]]
        if len(arguments) != len(func.parameters()):
            raise BaseException('Number of arguments is wrong')

        local_env = Environment(env)
        for (k, v) in zip(func.parameters(), arguments):
            local_env.set(k, v)

        return self.visit(func.tree(), local_env)

    def addition(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        return left + right

    def substraction(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        return left - right

    def multiplication(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        return left * right

    def divisiton(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        return left / right

    def symbol(self, tree, env):
        key = tree.children[0].value
        return env.get(key)

    def number(self, tree, env):
        return float(tree.children[0].value)

    def visit(self, tree, env):
        f = getattr(self, tree.data, self.__default__)
        return f(tree, env)


if __name__ == '__main__':
    program = open('program.txt').read()

    rule = open('grammer.txt').read()
    calc_parser = Lark(rule, start='program', parser='lalr')

    tree = calc_parser.parse(program)
    print(tree.pretty())

    global_env = Environment(None)

    visitor = Calculator()
    result = visitor.visit(tree, global_env)

    print(f'計算結果: {result}')
