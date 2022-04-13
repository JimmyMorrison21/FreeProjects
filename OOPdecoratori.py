from datetime import datetime as dt

class Unit:

    __LVL, __POSITION = 1,5
    __slots__ = ['__lvl', '__position', '__creation']

    def __init__(self):
        self.__lvl = Unit.__LVL
        self.__position = Unit.__POSITION
        self.__creation = dt.today()

    @property
    def lvl(self):
        return f'Уровень Юнита: {self.__lvl}', f'Дата создания: {self.__creation}', f'Позиция:{self.__position}'

    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += Unit.__typeTest(numeric)
        if self.__lvl >= 100: self.__lvl = 100

    @classmethod
    def set_cls_field(cls, lvl=1, position=2):
        cls.__LVL = Unit.__typeTest(lvl)
        cls.__POSITION = Unit.__typeTest(position)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError ('Must be int')


Unit.set_cls_field(6,3)
x = Unit()
print(x.lvl)