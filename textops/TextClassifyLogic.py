
from textops.Model.TextModel import TextModel
from common.analyzer.ApriorFreAnalyZer import ApriorFreAnalyZer
from textops.DelimiterFindLogic import *
from textops.TextParseLogic import TextParseLogic
import sys

class TextClassifyLogic:
    def __init__(self, datas):
        self.datas = datas

    def GetLocData(self):
        nowLocData = []
        for data in self.datas:
            nowLocData.append(data.now())
        return nowLocData

    def GetFrequentWords(self):
        nowLocDatas = self.GetLocData()
        Datas = [str(data) for data in nowLocDatas]
        print(len(Datas))
        freWords = ApriorFreAnalyZer([str(data) for data in nowLocDatas], 0.3).getApriorFre()
        print(freWords)


    def ConvertFreWords(self):
        pass

    def ClassifyMessages(self):
        pass

if __name__ == '__main__':
    datas = read_datas('/home/wxw/data/http_small', 'single')
    messages = read_datas('/home/wxw/data/http_small', 'single')
    messages = get_puredatas(messages)
    message_parser = TextParseLogic()
    messages = message_parser.ConvertDataToMessage(messages, '\r\n')
    textClassify = TextClassifyLogic(messages)
    textClassify.GetFrequentWords()