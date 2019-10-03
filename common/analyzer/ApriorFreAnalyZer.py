
from common.analyzer.BaseFreAnalyZer import BaseFreAnalyZer
import sys

class ApriorFreAnalyZer(BaseFreAnalyZer):
    def __init__(self, texts, supportRate):
        super().__init__(texts)
        self.freTextSet = set()
        self.support = supportRate
        self.freTexts = []

    def genStr(self):
        seNew = []
        for i in range(0, len(self.freTexts) - 1):
            for j in range(i, len(self.freTexts)):
                textNew = self.freTexts[i] + self.freTexts[j]
                if textNew not in self.freTextSet:
                    seNew.append(textNew)
        return seNew

    def genInitSingle(self):
        tempTextSet = set()
        for s in self.texts:
            if s not in tempTextSet:
                tempTextSet.add(s)
        return tempTextSet

    def genInitSet(self):
        tempTextSet = set()
        for text in self.texts:
            for s in text:
                if s not in tempTextSet:
                    tempTextSet.add(s)
        return tempTextSet

    # Compare study
    def filterSe(self, sequences):
        tempSet = set()
        for se in sequences:
            tempSupport = self.getWordsCount(se)
            if tempSupport / self.getTextLength(len(se)) >= self.support and se not in tempSet:
                tempSet.add(se)
        return tempSet

    def filterSeBySet(self, sequences):
        tempSet = set()
        for se in sequences:
            tempSupport = self.geSetWordsCount(se)
            #print(se, tempSupport)
            if tempSupport / self.getTextLengthSet(len(se)) >= self.support and se not in tempSet:
                tempSet.add(se)
        return tempSet

    def filterSeByCnt(self, sequences):
        tempSet = set()
        for se in sequences:
            tempSupport = self.getTextCnt(se)
            # print(se, tempSupport)
            if tempSupport / len(self.texts) >= self.support and se not in tempSet:
                tempSet.add(se)
        return tempSet



    def updateSet(self, newDatas):
        for data in newDatas:
            if data not in self.freTextSet:
                self.freTexts.append(data)
                self.freTextSet.add(data)

    def filterShort(self):
        for i in range(len(self.freTexts)):
            for j in range(len(self.freTexts)):
                if len(self.freTexts[j]) > len(self.freTexts[i]) and self.freTexts[j].find(self.freTexts[i]) != -1:
                    if self.freTexts[i] in self.freTextSet:
                        self.freTextSet.remove(self.freTexts[i])

    def getApriorFre(self):
        tempTextSet = self.genInitSet()
        self.updateSet(self.filterSeByCnt(list(tempTextSet)))
        while(True):
            nowSe = self.filterSeByCnt(self.genStr())
            if(len(nowSe) == 0):
                break
            else:
                self.updateSet(nowSe)
        self.filterShort()
        return self.freTextSet

if __name__ == '__main__':
    aprior = ApriorFreAnalyZer(['GET sadasd', 'GET kkjjll', 'POST jjkslasm', 'POST xoxixo'], 0.2)
    print(aprior.getApriorFre())

