from abc import *

class Base_measure:
    __class__ = ABCMeta

    def __init__(self, true_result, pre_result):
        self.true_data = true_result
        self.pre_data = pre_result
    @abstractmethod
    def measure(self):
        pass

