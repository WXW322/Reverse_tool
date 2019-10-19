from common.readdata import *

class StateSplit:
    def __init__(self):
        pass

    def generateStates(self, messages):
        result = []
        for message in messages:
            result.append((get_ip(message.source), message.data))
        return result

    def splitByDire(self, messages):
        ipMessages = self.generateStates(messages)
        splitResults = []
        i = 0
        sourceIp = ipMessages[0][0]
        while(i < len(ipMessages)):
            tempResult = []
            while(i < len(ipMessages) and ipMessages[i][0] == sourceIp):
                tempResult.append(ipMessages[i][1])
                i = i + 1
            while (i < len(ipMessages) and ipMessages[i][0] != sourceIp):
                tempResult.append(ipMessages[i][1])
                i = i + 1
            splitResults.append(tempResult)
        return splitResults
