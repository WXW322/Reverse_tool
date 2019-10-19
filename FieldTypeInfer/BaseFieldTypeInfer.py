
from abc import ABCMeta, abstractmethod

class BaseFieldTypeInfer(metaclass=ABCMeta):
    @abstractmethod
    def inferConst(self):
        pass

    @abstractmethod
    def inferSeriesId(self):
        pass

    @abstractmethod
    def inferFunc(self):
        pass

    @abstractmethod
    def inferLen(self):
        pass
    
