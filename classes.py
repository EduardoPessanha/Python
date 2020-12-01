import sys
from types import ModuleType


class Teste:
    def __novo__(self):

        pass


class VerboseModule(ModuleType):
    def __repr__(self):
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)


sys.modules[__name__].__class__ = VerboseModule


class Meta(type):
    def __getattribute__(*args):
        print("Metaclass getattribute invoked")
        return type.__getattribute__(*args)


class C(object, metaclass=Meta):
    def __len__(self):
        return 10

    def __getattribute__(*args):
        print("Class getattribute invoked")
        return object.__getattribute__(*args)


c = C()
c.__len__()
print(len(c))