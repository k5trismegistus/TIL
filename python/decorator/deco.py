class Deco():
    def __init__(self, value):
        self._value = value

    def decorator_func(func):
        def f(self, *args, **kwargs):
            print(f'value={self._value}')
            func(self, *args, **kwargs)
        return f

    @decorator_func
    def do(self, num):
        print(self._value * num)

if __name__ == '__main__':
    d = Deco('test')
    d.do(3)