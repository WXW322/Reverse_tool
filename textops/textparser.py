"""
This class is mainly for split text messages.
Give it message data and delimiter, it will
return the split results. 
"""

import sys
from netzob.all import *
sys.path.append('../common/')
from common.readdata import *
class textparser:
    def __init__(self):
        self.name = 'parser'

    def split(self, messages, delimiter):
        t_messages = []
        for message in messages:
            t_messages.append(RawMessage(data=message))
        symbol = Symbol(messages=t_messages)
        Format.splitDelimiter(symbol, '\r\n')
        result = symbol.getcells()
        print(result)

    def teststates(self):
        pass

if __name__ == '__main__':
    message_parser = textparser()
    messages = read_datas('/home/wxw/data/http_small', 'single')
    messages = get_puredatas(messages)
    message_parser.split(messages, '\r\n')



