
import time
from textops.Model.TextModel import TextModel
from common.analyzer.ApriorFreAnalyZer import ApriorFreAnalyZer
from textops.DelimiterFindLogic import *
from textops.TextParseLogic import TextParseLogic
import sys

class TextClassifyLogic:
    def __init__(self, datas):
        self.datas = datas
        self.freWords = None

    def GetLocData(self):
        nowLocData = []
        for data in self.datas:
            nowLocData.append(data.now())
        return nowLocData

    def filterShort(self, freWords, h):
        newFreWords = set()
        for value in freWords:
            if(len(value) >= h):
                newFreWords.add(value)
        return newFreWords

    def GetFrequentWords(self, rate, h):
        nowLocDatas = self.GetLocData()
        Datas = [str(data) for data in nowLocDatas]
        freWords = ApriorFreAnalyZer([str(data) for data in nowLocDatas], rate).getApriorFre()
        self.freWords = self.filterShort(freWords, h)
        return self.freWords


    def ConvertFreWords(self, data):
        freSet = {}
        for freWord in self.freWords:
            lo = data.find(freWord)
            if lo != -1:
                freSet[freWord] = lo
        frePattern = sorted(freSet.items(), key=lambda key:key[1])
        finalPattern = ''.join([item[0] for item in frePattern])
        return finalPattern

    def ClassifyMessages(self, messages):
        msgSet = {}
        for message in messages:
            freWord = self.ConvertFreWords(str(message.message))
            if freWord not in msgSet:
                msgSet[freWord] = []
            msgSet[freWord].append(message)
        return msgSet

    def FormatInfer(self, rate, h):
        self.GetFrequentWords(rate, h)
        messageClassify = self.ClassifyMessages(self.datas)
        finalFormats = []
        formatInfer = Format()
        for key,value in messageClassify.items():
            tMessages = []
            for message in value:
                singleMessage = RawMessage(message.message)
                tMessages.append(singleMessage)
            tempFormat = Symbol(messages=tMessages)
            formatInfer.splitAligned(tempFormat, doInternalSlick=True)
            finalFormats.append(tempFormat)
        return finalFormats



if __name__ == '__main__':
    beginTime = time.time()
    messages = read_datas('/home/wxw/data/http_measure', 'single')
    messages = get_puredatas(messages)
    message_parser = TextParseLogic()
    messages = message_parser.ConvertDataToMessage(messages, b'\r\n')
    textClassify = TextClassifyLogic(messages)
    textClassify.GetFrequentWords(0.2, 3)
    #msgSet = textClassify.FormatInfer(0.3, 3)
    #for value in msgSet:
    #    print(value._str_debug())
    #endTime = time.time()
    #print(endTime - beginTime)