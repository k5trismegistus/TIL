class BaseKlass():
    # こんなかんじでバウンドインナークラスを定義
    class InnerKlass():
        def __init__(self, value):
            self._value = value

        def value(self):
            return self._value

    def __init__(self):
        # Pythonらしく、`InnerKlass`だけだと名前解決できない
        self.inner = BaseKlass.InnerKlass('ハロー ハロー')

    def do(self):
        print(self.inner.value())

class InheritedKlass(BaseKlass):
    def __init__(self):
        # 継承したクラスもインナークラスを持っている
        self.inner1 = BaseKlass.InnerKlass('ぼくから世界へ 応答願います')
        self.inner2 = InheritedKlass.InnerKlass('ぼくらのコードは正しくつながっていますか')

    def do(self):
        print(self.inner1.value())
        print(self.inner2.value())

class MoreInheritedKlass(BaseKlass):
    # 継承もできる
    class InnerKlass(BaseKlass.InnerKlass):
        def __init__(self, value):
            self._value = value

        def value(self):
            return self._value + '───────'

    def __init__(self):
        self.inner1 = BaseKlass.InnerKlass('ぼくの世界は正しく回転している模様 ')
        self.inner2 = MoreInheritedKlass.InnerKlass('システムオールグリーン コミュニケーションは不全')

    def do(self):
        print(self.inner1.value())
        print(self.inner2.value())

if __name__ == '__main__':
    b = BaseKlass()
    b.do()

    i = InheritedKlass()
    i.do()

    mi = MoreInheritedKlass()
    mi.do()
