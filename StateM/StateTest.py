from netzob.all import *
from common.Model.format import format
from StateM.Stateline import StateLine
from common.readdata import *
from StateM.StateGenerator import StateGenerator
from StateM.StateCompare import StateCompare
from StateM.StateSplit import StateSplit
import re
import sys


def test_normal():
    f1 = Field(name="f1", domain="111")
    f2 = Field(name="f2", domain=ASCII(nbChars=(2, 3)))
    f3 = Field(name="f3", domain="like")
    f = Symbol([f1, f2, f3])
    aa, bb = AbstractField.abstract("2111ablike", [f])
    print(type(aa) == UnknownSymbol)


def test_int():
    f1 = Field(name="f1", domain=10)
    f2 = Field(name="f2", domain='111')
    f3 = Field(name="f3", domain="like")
    f = Symbol([f1, f2, f3])
    aa, bb = AbstractField.abstract("2111ablike", [f])
    print(type(aa) == UnknownSymbol)


def test_bytes():
    f1 = Field(name='f1', domain=b'x')
    tt = BitArray(nbBits=(16, 24))
    f2 = Field(name='f2', domain=tt)
    f3 = Field(name='f3', domain=b'cc')
    f = Symbol([f1, f2, f3])
    aa, bb = AbstractField.abstract(b'xaacc', [f])
    print(bb)


def test_f():
    s_datas = [[('C', 'function', 'GET'), ('V', 'payload', (0, -1))],
               [('C', 'funciton', 'POST'), ('V', 'payload', (0, -1))], \
               [('C', 'function', b'HTTP/1.1'), ('V', 'payload', (0, -1))]]
    s_names = ['GET', 'POST', 'RESPONSE']
    f = format("http")
    symbols = f.get_symbols(s_datas, s_names)
    return symbols


def testState(path):
    t_datas = read_datas(path)[0:20]
    t_datas = get_puredatas(t_datas)
    symbols = test_f()
    State = StateLine(symbols)
    stateList = State.mes2SymName(t_datas)
    for s in stateList:
        print(s)
    return stateList

def getSessions(path):
    stateSplit = StateSplit()
    t_datas = read_datas(path)[0:20]
    datasSplit = stateSplit.splitByDire(t_datas)
    symbols = test_f()
    State = StateLine(symbols)
    tSessions = []
    for dataSplit in datasSplit:
        tSessions.append(State.mes2SymName(dataSplit))
        print(tSessions[0])
    return tSessions



if __name__ == '__main__':
    symbolNames = getSessions('/home/wxw/data/http/httpSplitOne')
    tNames = set()
    for names in symbolNames:
        for name in names:
            if name not in tNames:
                tNames.add(name)
    stateGenerators = StateGenerator(tNames)
    for names in symbolNames:
        stateGenerators.graphGenerator(names)
    #stateGenerators.graphShow()
    links = stateGenerators.getLinkHase()
    writeLinks = {'Unknown Symbol RESPONSE', 'POST Unknown Symbol'}
    stateCom = StateCompare()
    print(stateCom.comPareStates(links, writeLinks))


