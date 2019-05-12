import sys
sys.path.append('../common/measure_tool/')
from measure_base import Base_measure

class Fields_measure(Base_measure):
    def __init__(self, words_true, words_pre):
        super().__init__(words_true, words_pre)

    def measure(self, topk):
        true_dic = {}
        for item in self.true_data:
            true_dic[item] = 1
        i = 0
        infer_cnt = 0
        while(i < topk and i < len(self.pre_data)):
            if self.pre_data[i] in true_dic:
                infer_cnt = infer_cnt + 1
            i = i + 1
        return infer_cnt