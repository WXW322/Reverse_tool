from netzob.all import *
from collections import OrderedDict
import re

class StateLine:
    def __init__(self, symbols, name = 'line'):
        self.name = name
        self.Symbols = symbols
        self.Symbol_dic = {}
        for symbol in  self.Symbols:
            self.Symbol_dic[symbol.name] = 1
        self.Symbol_result = []

    def mes2sym(self, data):
        r_sym = UnknownSymbol(RawMessage(data))
        r_data = OrderedDict()
        for symbol in self.Symbols:
            t_sym, t_data = AbstractField.abstract(data, [symbol])
            if(type(t_sym) != UnknownSymbol):
                r_sym = t_sym
                r_data = t_data
                break
        return(r_sym, r_data)

    def messages2sym(self, datas):
        Sym_r = []
        for data in datas:
            Sym_r.append(self.mes2sym(data))
        self.Symbol_result = Sym_r
        return Sym_r

    def mes2SymName(self, datas):
        Results = self.messages2sym(datas)
        stateList = []
        for result in Results:
            if re.match('Unknown Symbol', result[0].name):
                stateList.append('Unknown Symbol')
            else:
                stateList.append(result[0].name)
        return stateList



            
        
