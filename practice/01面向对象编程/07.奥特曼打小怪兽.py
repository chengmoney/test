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

    @property
    def mp(self):
        return self._mp

    def attack(self, other):
        attack_hp = randint(self.attack_power * 0.4, self.attack_power)
        print('{}对{}发起普通{}攻击'.format(self.name, other.name, attack_hp))
        other.hp -= attack_hp

    def magic_attack(self, others):
        """
        魔法值超过20的时候,可以对多个对象发动魔法攻击,消耗20点魔法值
        :param others: 攻击对象
        :return: 成功为True,失败为False
        """
        if self._mp > 20:
            for other in others:
                if other.alive:
                    other.hp -= self.attack_power
                    print('{}对{}发起{}魔法攻击'.format(self.name, other.name, self.attack_power))
            self._mp -= 20
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
            self.attack(other)

    def __str__(self):
        return '~~~{}奥特曼~~~\n'.format(self.name) + \
                '生命值{}'.format(self._hp) + \
                '魔法值{}'.format(self._mp)


class Master(Fighter):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)

    def attack(self, other):
        other.hp -= self.attack_power

    def __str__(self):
        return '~~~{}小怪兽~~~\n'.format(self.name) + \
                '生命值{}'.format(self._hp)


def is_any_alive(fighters):
    for fighter in fighters:
        if fighter.hp > 0:
            return True
    return False


def select_master(masters):
    """随机选择一个存活的怪兽"""
    num = len(masters)
    while True:
        index = randrange(num)
        master = masters[index]
        if master.hp > 0:
            return master


def display_info(ultm, masters):
    print(ultm)
    for master in masters:
        print(master)


def main():
    u = Ultraman('迪加', 200, 50, 10)
    m1 = Master('皮卡丘', 50, 5)
    m2 = Master('妙蛙种子', 40, 10)
    m3 = Master('喵喵兽', 20, 15)
    ms = [m1, m2, m3]
    fight_round = 1
    display_info(u, ms)
    while u.alive and is_any_alive(ms):
        print('-----------第{}回合----------'.format(fight_round))
        m = select_master(ms)
        skill = randint(1, 10)
        if skill <= 5:
            u.critical_attack(m)
        else:
            if u.magic_attack(ms):
                print('{}对怪兽们发动了魔法攻击'.format(u.name))
        for master in ms:
            if master.alive:
                master.attack(u)
                print('{}对{}发动了攻击,攻击{}点血'.format(master.name, u.name, master.attack_power))
        fight_round += 1
        display_info(u, ms)

    print('-----------战斗结束-----------')
    if u.alive:
        print('奥特曼胜利')
    else:
        print('怪兽胜利')


if __name__ == '__main__':
    main()













