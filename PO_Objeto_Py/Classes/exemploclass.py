from os import system

system('clear')


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()

print(f"\n {x.i}")
print(f"\n {x.f()}\n")
print("\nSaudação:...", x.f())
print("\nNúmero:-----", str(x.i))
