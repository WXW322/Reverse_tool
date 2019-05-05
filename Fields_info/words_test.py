from field_discover import words_discover
import logging
import sys
sys.path.append('../log_info/')
from logger import get_logger

def ve_word():
    word_dis = words_discover()
    word_r = word_dis.infer_words_by_ve("/home/wxw/data/iec104_test", "single", 4, "yes", "abs", "normal", 0, 0)
    words_logger = get_logger('../log_info/word_log')
    words_logger.error(word_r)

ve_word()