from netzob.all import *
from FieldTypeInfer.BaseFieldTypeInfer import BaseFieldTypeInfer
from common.Converter.base_convert import Converter
from common.analyzer.analyzer_common import base_analyzer


class WholeFieldTypeInfer(BaseFieldTypeInfer):
    def __init__(self):
        self.MaxLen = 40
        self.lengthThreshold = 0.8
        self.constThreshold = 0.98
        self.idThreshold = 0.7

    def inferConst(self, datas):
        wordDic = Converter.convert_raw_to_count(datas)
        wordDic = sorted(wordDic.items(), key=lambda x: x[1])
        if (wordDic[0][1] > self.constThreshold):
            return 1
        else:
            return 0

    def inferSeriesId(self, datas):
        ids = []
        for i, data in enumerate(datas):
            ids.append(i)
        datasBigInt = Converter.bytesToBigInt(datas)
        datasLittle = Converter.byteToLittle(datas)
        tRate = max(base_analyzer.pearson(ids, datasBigInt), base_analyzer.pearson(ids, datasLittle))
        if (tRate > self.idThreshold):
            return 1
        else:
            return 0

    def inferLen(self, datas, lens):
        datasLenBig = Converter.bytesToBigInt(datas)
        datasLittle = Converter.byteToLittle(datas)
        personBig = base_analyzer.pearson(datasLenBig, lens)
        personLittle = base_analyzer.pearson(datasLittle, lens)
        if personBig > self.lengthThreshold or personLittle > self.lengthThreshold:
            return 1
        else:
            return 0

    def inferFunc(self, datas):
        datasDic = Converter.convert_raw_to_count(datas)
        datasEntry = base_analyzer.get_entry([value for value in datasDic.values()])



