class KlassMethod():

    @classmethod
    def create(cls, name):
        ins = cls(name)

        return ins

    @classmethod
    def create_and_call_private(cls, name):
        ins = cls(name)
        ins.__priv()

    def __init__(self, value):
        self.value = value

    def say(self):
        print(self.value)

    def __priv(self):
        print(f'{self.value} (private)')


if __name__ == '__main__':
    ins = KlassMethod.create('hello, world')
    ins.say()

    ins2 = KlassMethod.create_and_call_private('hello, world')

    try:
        ins.__priv()
    except:
        print('これはNG')
