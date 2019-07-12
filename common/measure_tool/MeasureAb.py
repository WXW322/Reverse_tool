from common.measure_tool.measure_base import Base_measure

class MeasureAb(Base_measure):
    def __init__(self):
        super(MeasureAb,self).__init__()

    def MeasureDic(self, dicA, dicB):
        t_lo = True
        for key in dicA:
            if(dicA[key] != dicB[key]):
                print(key, dicA[key], dicB[key])
                t_lo = False
                break
        return t_lo

    def Measure(self, DataTure, DataPredict):
        return self.MeasureDic(DataTure, DataPredict)
