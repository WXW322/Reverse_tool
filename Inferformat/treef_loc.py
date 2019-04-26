from treef import *
from node import *
import sys
sys.path.append('../common/Model/')
from canf import *

class treefL(treef):
    def __init__(self, datas, T_c, T_r):
        super(treefL, self).__init__(datas)
        self.R = T_r
        self.C = T_c

    def generate_T(self):
        t_ids = []
        for id in self.datas:
            t_ids.append(id)
        self.tree = node()
        self.tree.children = self.generate_node(t_ids)
        return self.tree

    def generate_node(self, n_data):
        t_r = []
        t_start = self.datas[n_data[0]].now()
        #if(len(n_data) < self.C):
         #   return [node((t_start, -1), n_data)]
        t_num = {}
        for data in n_data:
            t_next = self.datas[data].next()
            if t_next not in t_num:
                t_num[t_next] = []
            t_num[t_next].append(data)
        t_v = []
        for key in t_num:
            if(float(len(t_num[key])) / float(len(n_data)) >= self.R and len(t_num[key]) >= self.C):
                t_node = node((t_start, key), t_num[key])
                if(t_start != key):
                    t_node.children = t_node.children + self.generate_node(t_num[key])
                t_r.append(t_node)
            else:
                t_v.append(t_num[key])
        if(len(t_v) > 0):
            t_node = node((t_start, -1), t_v)
            t_r.append(t_node)
        return t_r






