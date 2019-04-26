from netzob.all import *
import math
import readdata
import sys
sys.path.append('../Inference/')
import word_deal
import numpy as np
import time

class info:
    def __init__(self):
        self.name = "info"
        self.datas = None

    def read_data(self, path):
        datas = readdata.read_datas(path)
        p_datas = readdata.get_puredatas(datas)
        self.datas = p_datas
        return p_datas

    def get_raw(self, los):
        t_f = []
        if los[0] == los[1]:
            for data in self.datas:
                if(los[0] < len(data)):
                    t_f.append(data[los[0]:los[0] + 1])
        else:
            for data in self.datas:
                if(los[1] < len(data)):
                    t_f.append(data[los[0]:los[1]])
        return t_f

    def byte2int(self, data):
        t_list = []
        i = 0
        while(i < len(data)):
            t_list.append(data[i])
            i = i + 1
        return t_list
            
    def byte2str(self, data):
        t_data = self.byte2int(data)
        return '_'.join(t_data)

    def get_entry(self, datas):
        result = -1
        if(len(datas) > 0):
            result = 0
        for data in datas:
            result = result + (- data) * math.log(data, 2)
        return result

    def caculate_prob(self, vector):
        t_r = {}
        for v in vector:
            if v not in t_r:
                t_r[v] = 1
            else:
                t_r[v] = t_r[v] + 1
        for key in t_r:
            t_r[key] = t_r[key] / len(vector)
        return t_r


    def get_lo(self, los):
        t_raw = self.get_raw(los)
        t_dic = self.caculate_prob(t_raw)
        t_f = []
        for key in t_dic:
            t_f.append(t_dic[key])
        return self.get_entry(t_f)

    def huxinxi(self, vectorone, vectortwo, vectorthree):
        t_probone = self.caculate_prob(vectorone)
        t_probtwo = self.caculate_prob(vectortwo)
        t_probsum = self.caculate_prob(vectorthree)
        t_info = 0 
        i = 0
        for key_one in t_probone:
            for key_two in t_probtwo:
                key_m = key_one + key_two
                if key_m in t_probsum:
                    t_info = t_info + t_probsum[key_m] *np.log(t_probsum[key_m] / (t_probone[key_one] * t_probtwo[key_two]))
        return t_info

    def merge_key(self, key_one, key_two):
        t_f = []
        if type(key_one) == int:
            t_f.append(key_one)
        else:
            for data in key_one:
                t_f.append(data)
        if type(key_two) == int:
            t_f.append(key_two)
        else:
            for data in key_two:
                t_f.append(data)
        return '_'.join(t_f)

    def merge_list(self, LA, LB):
        i = 0
        merge_l = []
        while(i < len(LA)):
            merge_l.append(LA[i] + LB[i])
            i = i + 1
        return merge_l

    def get_munation(self, los):
        data_los = []
        for lo in los:
            data_los.append(self.get_raw(lo))
        muations = {}
        i = 0
        while(i < len(data_los) - 1):
            l_a = data_los[i]
            l_b = data_los[i+1]
            if(len(l_a) != len(l_b)):
                muations[i] = 0
                i = i + 1
                continue
            l_m = self.merge_list(l_a,l_b)
            muations[i] = self.huxinxi(l_a, l_b, l_m)
            i = i + 1
        return muations


        
        

    def get_loenrty(self, los):
        return self.get_keyentry(self.get_lo(los))

    def D(self, x, y):
        return abs(x - y) / (min(x, y) + 1)

    def D_mu(self, x, y):
        return x/y

    def get_fieldbys(self, length, threshold):
        t_keys = {}
        i = 0
        t_ens = {}
        while(i <= length):
            t_keys[i] = 0
            t_ens[i] = self.get_lo((i, i))
            i = i + 1
        i = 0
        while(i < length):
            if(self.D(t_ens[i], t_ens[i+1]) < threshold):
                t_keys[i] = 1
            i = i + 1
        return self.get_fields(t_keys)

    def get_fieldsbymu(self, legnth, thre_c, thre_v):
        t_keys = {}
        i = 0
        t_ens = {}
        t_mutations = {}
        los = []
        while(i <= length):
            t_keys[i] = 0
            t_ens[i] = self.get_lo((i, i))
            los.append((i, i))
            i = i + 1
        t_mutations = self.get_munation(los)
        i = 0
        while(i < length):
            if(t_ens[i] < thre_c):
                if(t_ens[i+1] < thre_c):
                    t_keys[i] = 1
            else:
                 if(self.D_mu(t_mutations[i], t_ens[i]) > thre_v):
                     t_keys[i] = 1
            i = i + 1
        return self.get_fields(t_keys)


                    
    def get_fields(self, los_info):
        t_f = []
        i = 0
        length = len(los_info) - 1
        while(i < length):
            start = i
            t_end = i + 1
            if(los_info[i] == 0):
                i = i + 1
            else:
                j = i + 1
                while(j <= length and los_info[j] == 1):
                    j = j + 1
                t_end = j + 1
            t_f.append((start, t_end))
            i = t_end
        return t_f
    




def chang(path, length):
    t_info = info()
    t_info.read_data(path)
    i = 0
    t_f = []
    while(i < length):
        t_f.append(t_info.get_loenrty((i, i)))
        i = i + 1
    print(t_f)

def get_los(path, length, thre, b_rs):
    t_lo = info()
    t_lo.read_data(path)
    t_r = t_lo.get_fieldbys(length, thre)
    print(t_r)
    M_dealer = word_deal.message_dealer()
    M_dealer.set_conlo(t_r)
    M_dealer.set_rlo(b_rs)
    M_dealer.get_f1()

def get_fs(path, length):
    t_lo = info()
    t_lo.read_data(path)
    los = []
    t_entrys = {}
    for i in range(length):
        t_entrys[i] = t_lo.get_lo((i, i))
        los.append((i,i))
    print(t_lo.get_munation(los))
    print(t_entrys)
start = time.time()    
#get_fs('/home/wxw/data/modbusdata/', 10)
#get_fs('/home/wxw/data/iec104/', 13)
get_fs('/home/wxw/data/cip_datanew/', 24)
end = time.time()
print(end - start)
"""
chang('/home/wxw/data/cip_datanew/', 24)
chang('/home/wxw/data/modbusdata/', 10)
chang('/home/wxw/data/iec104/', 13)
sys.exit()
#get_los('/home/wxw/data/cip_datanew/', 24, 0.3)
Rs = [9, 12, 24]
rights = [[(0,2),(2,5),(5,6),(6,7),(7,8)], [(0,1),(1,2),(2,4),(4,6),(6,7),(7,8),(8,9),(9,10),(10,12)], [(0, 2), (2, 4), (4, 8), (8, 12), (12, 20), (20,24)]]
thres = [i * 0.1 for i in range(1, 10)]
pathsf = ['/home/wxw/data/modbusdata/', '/home/wxw/data/iec104/', '/home/wxw/data/cip_datanew/']
pathst = ['/home/wxw/paper/researchresult/icccn/modbus.txt', '/home/wxw/paper/researchresult/icccn/iec104.txt', '/home/wxw/paper/researchresult/icccn/cip.txt']
for i in range(3):
    t_f = open(pathst[i], 'w+')
    sys.stdout = t_f
    for j in thres:
        print(j)
        get_los(pathsf[i], Rs[i], j, rights[i])
    t_f.close()
"""





