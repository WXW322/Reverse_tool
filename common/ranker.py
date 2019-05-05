from netzob.all import *
import sys

class ranker:
    def rank_dic(self, dics, reverse = False):
        try:
            dic_r = sorted(dics.items(), key = lambda x:x[1], reverse=reverse)
            return dic_r
        except Exception as e:
            print("rank ley error:" + e)


