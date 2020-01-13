"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    __slots__ = '_name'

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def employee(self):
        """计算每个月的工资"""
        pass


class Manager(Employee):
    __slots__ = '_name'

    def employee(self):
        per_month_salary = 15000
        print('经理每个月的工资为{}'.format(per_month_salary))


class Programmer(Employee):
    __slots__ = ('_name', '_hours')

    def __init__(self, name, hours):
        super().__init__(name)
        self._hours = hours

    def employee(self):
        per_month_salary = self._hours * 150
        print('程序员这个月工作了{}个小时,工资为{}'.format(self._hours, per_month_salary))


class Salesman(Employee):
    __slots__ = ('_name', '_sale')

    def __init__(self, name, sale):
        super().__init__(name)
        self._sale = sale

    def employee(self):
        per_month_salary = 1200 + self._sale * 0.05
        print('销售员这个月的销售额为{},本月工资为{}'.format(self._sale, per_month_salary))


def main():
    management = Manager('成憨憨')
    programmer = Programmer('刘傻傻', 40)
    salesman = Salesman('嘿嘿', 100000)
    management.employee()
    programmer.employee()
    salesman.employee()


if __name__ == '__main__':
    main()




