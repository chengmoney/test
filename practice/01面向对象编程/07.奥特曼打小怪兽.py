from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """ 战斗者 """
    __slots__ = ('_name', '_hp', '_attack_power')

    def __init__(self, name, hp, attack_power):
        """
        :param name: 姓名
        :param hp:  血量
        :param attack_power: 攻击力
        """
        self._name = name
        self._hp = hp
        self._attack_power = attack_power

    @property  # 将一个方法变成一个属性
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def attack_power(self):
        return self._attack_power

    @name.setter
    def name(self, name):
        self._name = name

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp > 0 else 0

    @attack_power.setter
    def attack_power(self, attack_power):
        self._attack_power = attack_power

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻击
        :param other:被攻击对象

        """
        pass


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp', '_attack_power')

    def __init__(self, name, hp, mp, attack_power):
        """
        :param name:
        :param hp:
        :param mp: 魔法值
        :param attack_power:
        """
        super().__init__(name, hp, attack_power)
        self._mp = mp

    def normal_attack(self, other):
        attack_hp = randint(self.attack_power * 0.4, self.attack_power)
        print('对{}发起普通{}攻击'.format(other.name, attack_hp))
        other.hp -= attack_hp

    def magic_attack(self, others):
        """
        魔法值超过20的时候,可以对多个对象发动魔法攻击,消耗20点魔法值
        :param others: 攻击对象
        :return: 成功为True,失败为False
        """
        if self._mp > 20:
            for other in others:
                other.hp -= self.attack_power
            return True
        else:
            return False

    def critical_attack(self, other):
        """
        暴击:有10%的几率暴击3倍,有20%的几率暴击2倍,有30%的几率暴击1倍
        :param other:被攻击者
        :return: 无
        """
        n = randint(1, 10)
        if n == 10:
            attack = self.attack_power * 3
            print('对{}发起3倍暴击{}攻击'.format(other.name, attack))
            other.hp -= attack
        elif n == 8 or n == 9:
            attack = self.attack_power * 2
            print('对{}发起2倍暴击{}攻击'.format(other.name, attack))
            other.hp -= attack
        elif 5 <= n <= 7:
            attack = self.attack_power * 1
            print('对{}发起1倍暴击{}攻击'.format(other.name, attack))
            other.hp -= attack
        else:
            self.normal_attack(other)


class Master(Fighter):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)

    def attack(self, other):
        other.hp -= self.attack_power


ut = Ultraman('cy', 400, 100, 5)
mt = Master('hh', 200, 10)

while mt.alive:
    ut.critical_attack(mt)





