from netzob.all import *
from treelib import *
import numpy as np
import time
import sys
sys.path.append("../ngrambuild/")
sys.path.append("../common/")
sys.path.append("../class/")
sys.path.append("../Inferformat/")
import pyngram
from f_cg import transer
import parse
from readdata import *

class splitter:

    def split_by_ve(self, messages, h, combine, model, v_way, T=0, r=0, ways="g"):
        voter = pyngram.voters()
        split_messages = voter.single_message_voter(messages, h, combine, model, v_way, T, r)
        converter = transer()
        return converter.listtoids(split_messages[0])






