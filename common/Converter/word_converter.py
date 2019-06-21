from common.Converter.base_convert import Converter
from common.analyzer.analyzer_common import base_analyzer
from Data_base.Data_redis.redis_deal import redis_deal
from common.ranker import ranker
import sys
import time

class word_convert(Converter):
    def __init__(self):
        super().__init__
        self.rank = ranker()

    def split_words(self, words, t_len):
        words_r = {}
        for i in range(1, t_len + 1):
            words_r[i] = []
        for word in words:
            words_r[len(word.split(' '))].append(word)
        return words_r

    def get_childs(self, word, words):
        w_len = len(word)
        t_children = []
        for l_word in words:
            if l_word[0:w_len] == word:
                t_children.append(l_word)
        return t_children

    def convert_word_order(self, words_s, words_l):
        start = 0
        w_orders = {}
        for word_s in words_s:
            w_childs = self.get_childs(word_s, words_l)
            w_orders[word_s] = start + int(len(w_childs)/2)
            start = start + int(len(w_childs))
        return w_orders

    def splitwords_bylen(self, raw_words, len_max):
        """
        :param words:
        :param raw_words:
        :param len_max:
        :return:
        """
        word_length = {}
        for i in range(1, len_max + 1):
            word_length[i] = []
        for word in raw_words:
            word_length[len(word.split(' '))].append((word, raw_words[word]))
        return word_length

    def itemtoborder(self, words):
        """
        :param words:tuple of words
        :return: the split border
        """
        words_rank = self.rank.rank_tulple(words)
        borders = [word[0] for word in words_rank]
        borders.append(words_rank[-1][1])
        if len(borders) > 0:
            borders.pop(-1)
        return borders

    def convert_raw_word_to_order(self, raw_words):
        analyzer = base_analyzer()
        word_ranker = ranker()
        converter = word_convert()
        num_words = converter.splitwords_bylen(raw_words, 5)
        for len_word in num_words:
            num_words[len_word] = word_ranker.rank_tulple(num_words[len_word], reverse=True)
        prime_words = [word[0] for word in num_words[4]]
        prime_orders = {}
        for i in range(len(prime_words)):
            prime_orders[prime_words[i]] = i
        order_words = {}
        order_words[4] = prime_orders
        start_time = time.time()
        for i in range(1, 4):
            order_words[i] = converter.convert_word_order([word[0] for word in num_words[i]], prime_words)
        end_time = time.time()
        print(end_time - start_time)
        print(word_ranker.rank_dic(order_words[1]))
        print(num_words[1])






if __name__ == '__main__':
    redis_read = redis_deal()
    raw_words = redis_read.read_from_redis('modbus_one_frequent_voter_abs_normal_0_0correct_raw_words')
    word_converter = word_convert()
    word_converter.convert_raw_word_to_order(raw_words)






