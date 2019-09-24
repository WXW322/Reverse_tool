

class StateGenerator:
    def __init__(self, symbolNames):
        self.symbols = {}
        for name in symbolNames:
            self.symbols[name] = {}

    def nodeGenerate(self, firstState, secondState):
        if secondState not in self.symbols[firstState]:
            self.symbols[firstState][secondState] = 1

    def graphGenerator(self, stateLines):
        i = 0
        while(i < len(stateLines) - 1):
            self.nodeGenerate(stateLines[i], stateLines[i+1])
            i = i + 1

    def graphShow(self):
        print("The Node is:")
        for name in self.symbols:
            print('%s: '%(name), end='')
            for subName in self.symbols[name]:
                print('%s ,'%(subName), end='')
            print('')

    def getLinkHase(self):
        links = set()
        for firstName in self.symbols:
            for secondName in self.symbols[firstName]:
                nameHash = '%s %s'%(firstName, secondName)
                links.add(nameHash)
        return links
