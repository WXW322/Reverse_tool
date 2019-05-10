"""
This class is mainly for split text messages.
Give it message data and delimiter, it will
return the split results. 
"""

import sys
from netzob.all import *
sys.path.append('../common/')
import read
class textparser:
    def __init__(self):
        self.name = parser

    def split(self, messages, delimiter):
        t_messages = []
        for message in messages:
            t_messages.append(RawMessages(message))
        symbol = Symbol(t_messages)
        Format.splitDelimiter(symbol, b'\r\n')
        result = symbol.getcells()

    def teststates(self):
        pass

