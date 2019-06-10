from netzob.all import *
from treelib import *
import numpy as np
import time
import sys
from ngrambuild.pyngram import voters
from common.f_cg import transer
from common.readdata import *
from Data_base.Data_redis.redis_deal import redis_deal
from Config.ve_strategy import ve_strategy
import json

class splitter:

    def split_by_ve(self, messages, h, combine, model, v_way, T=0, r=0, ways="g"):
        voter = voters()
        split_messages = voter.single_message_voter(messages, h, combine, model, v_way, T, r)
        converter = transer()
        return converter.listtoids(split_messages)






