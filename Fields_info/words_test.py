from field_discover import words_discover
import logging
import sys
sys.path.append('../log_info/')
sys.path.append('../Config/')
sys.path.append('../common/')
from logger import get_logger
from fields_measure import Fields_measure
from iec104 import iec104
from f_cg import transer

def ve_word():
    word_dis = words_discover()
    word_r = word_dis.infer_words_by_ve("/home/wxw/data/iec104_test", "single", 4, "yes", "abs", "normal", 0, 0)
    word_transer = transer()
    iec104_w = iec104()
    word_t = word_transer.field_keys(iec104_w.fields)
    t_measure = Fields_measure(word_r, word_t)
    t_measure.measure(10)
    words_logger = get_logger('../log_info/word_log', 'word_log')
    words_logger.error(word_r)

ve_word()