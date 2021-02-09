from abc import ABC, abstractmethod


class Talker(ABC):
    # 使用abstractmethod 装饰器来表示这个方法是抽象方法
    @abstractmethod
    def talk(self):
        pass


# 抽象类不能被实例化
Talker()