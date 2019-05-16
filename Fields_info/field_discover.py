from netzob.all import *
import sys
import time
sys.path.append('../common/')
sys.path.append("../ngrambuild/")
sys.path.append('../splitter/')
sys.path.append('../log_info/')
import time
from readdata import *
from ranker import ranker
from word_convert import word_convert
from VE_spliter import splitter
from logger import get_logger

class words_discover:
    def __init__(self):
        self.name = "words_deal"

    def infer_words_by_ve(self, data_path, r_way, h, combine, model, v_way, T, r):
        datas = read_datas(data_path, r_way)
        datas = get_puredatas(datas)
        messages = add_tail(datas, h)
        message_splitter = splitter()
        message_split = message_splitter.split_by_ve(messages, h, combine, model, v_way, T, r)
        m_logger = get_logger('../log_info/messge_splited_log' + str(time.time()), 'msg_split')
        for message in message_split:
            m_logger.error(message)
        T_word_convert = word_convert()
        words_prim = T_word_convert.convert_words_byloc(message_split)
        t_time = str(time.time())
        p_logger = get_logger('../log_info/p_log' + t_time, 'word_count')
        for key in words_prim:
            p_logger.error(key + str(words_prim[key].content))
        words_count = T_word_convert.get_words_count(words_prim)
        t_ranker = ranker()
        words_rank = t_ranker.rank_dic(words_count,True)
        return words_rank




