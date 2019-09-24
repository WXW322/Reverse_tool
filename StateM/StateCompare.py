from common.analyzer.analyzer_common import base_analyzer

class StateCompare:
    def __init__(self):
        pass

    def comPareStates(self, statesA, statesB):
        return base_analyzer.getSetDis(statesA, statesB)


