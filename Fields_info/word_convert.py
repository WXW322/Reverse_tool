from netzob.all import *
from const_field import loc_field
import sys
sys.path.append('../common/')
from f_cg import transer


class word_convert:

    def loctokey(self, loc):
        key = ""
        try:
            key = key + str(loc[0]) + " "
            key = key + str(loc[1])
        except Exception as e:
            print("convert key error:" + str(e))
        return key

    def keytoloc(self, key):
        try:
            locs = key.split(" ")
            start = int(locs[0])
            end = int(locs[1])
            return (start, end)
        except Exception as e:
            print("key to str error:" + str(e))


    def convert_words_byloc(self, sequences):
        t_words = {}
        word_transfer = transer()
        for sequence in sequences:
            words_sequence = word_transfer.border2item(sequence[1])
            for word in words_sequence:
                word_key = self.loctokey(word)
                if word_key not in t_words:
                    t_words[word_key] = []
                t_words[word_key].append(sequence[0])
        for key in t_words:
            loc_r = self.keytoloc(key)
            t_words[key] = loc_field(loc_r, t_words[key])
        return t_words

    def get_words_count(self, words):
        words_r = {}
        for word in words:
            words_r[word] = (words[word].get_content_count())
        return words_r






