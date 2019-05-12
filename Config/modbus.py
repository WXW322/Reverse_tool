
class modbus:
    def __init__(self):
        self.coms = []
        self.lo = 7
        self.feilds = [(0, 2), (2, 4), (4, 6), (6, 7), (7, 8), (8, 10), (10, 12), (8, 9), (12, 13)]
