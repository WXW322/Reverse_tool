
class prime_b:
    def __init__(self, datas):
        self.datas = datas
        self.loc = 0

    def next(self):
        if(self.loc < len(self.datas) - 1):
            self.loc = self.loc + 1
        return self.datas[self.loc]

    def now(self):
        return self.datas[self.loc]