"""
   子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。通过方法重写我们可以让父类的
同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，
这个就是多态（poly-morphism）。
    所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。Python从语法层面并没有像Java或C#那样提供对抽象类的
支持，但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实
例化（创建对象）。
"""
from abc import ABCMeta, abstractmethod


class Animal(object, metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Animal):

    def make_voice(self):
        print('%s:汪汪汪' % self._name)


class Cat(Animal):
    def make_voice(self):
        print('%s:喵喵喵' % self._name)


def main():
    pets = (Dog('旺财'), Cat('牛奶'))
    for pet in pets:
        pet.make_voice()


main()
