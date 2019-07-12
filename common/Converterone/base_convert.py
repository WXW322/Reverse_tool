from common.readdata import *
import numpy as np
from Config.ve_strategy import ve_strategy
import sys
from sklearn.feature_extraction.text import CountVectorizer
from Data_base.Data_redis.redis_deal import redis_convert

class Converter:
    def __init__(self):
        pass

    def convert_raw_to_text(self, message):
        phrase = ''
        for i in range(len(message)):
            if(len(phrase) == 0):
                phrase = phrase + str(message[i])
            else:
                phrase = phrase + ' ' + str(message[i])
        return phrase

    def ConvertRawToLengthText(self, message):
        """
        converse a message to n-gram item
        message: a list o bytes
        return : str of n-gram items
        """
        t_list = []
        t_len = len(message)
        i = 0
        t_flist = ''
        h = ve_strategy().vote_parameters['height']
        while (i < t_len):
            if (len(t_flist) == 0):
                t_flist = t_flist + str(message[i])
            else:
                t_flist = t_flist + ' ' + str(message[i])
            i = i + 1
        i = 0
        while(i < h):
            t_flist = t_flist + ' ' + ve_strategy().vote_parameters['stop_words']
            i = i + 1
        return t_flist

    def ConvertRawToLengthTexts(self,messages):
        """
        function: converse messages to n-gram items
        messages: a list of message
        t_lists: str sentence lists
        """
        t_lists = ''
        for message in messages:
            if(len(t_lists) == 0):
                t_lists = t_lists + self.ConvertRawToLengthText(message)
            else:
                t_lists = t_lists + '. ' + self.ConvertRawToLengthText(message)
        return t_lists

    def filter_words(self, t_dic):
        stop_word = ve_strategy().vote_parameters['stop_words']
        t_words_new = {}
        for key in t_dic:
            if key.find(stop_word) == -1:
                t_words_new[key] = t_dic[key]
        return t_words_new

    def ConvertRawToDict(self, messages):
        """
        function : get frequent of each words
        messages: str multiple sentences
        t_dics: dict words and its frequent
        """
        t_inputs = [self.ConvertRawToLengthTexts(messages)]
        length = ve_strategy().vote_parameters['height']
        vetorizer = CountVectorizer(ngram_range=(1, length), stop_words=[' ', '.'], token_pattern='(?u)\\b\\w\\w*\\b')
        X = vetorizer.fit_transform(t_inputs)
        t_arrays = np.squeeze(X.toarray())
        words = vetorizer.get_feature_names()
        t_len = len(words)
        t_dics = {}
        i = 0
        while (i < t_len):
            t_dics[words[i]] = int(str(t_arrays[i]))
            i = i + 1
        t_dics = self.filter_words(t_dics)
        self.words_table = t_dics
        prefix = ve_strategy().GetWordsKeys('RawWords')
        redis_convert.insert_to_redis(prefix, t_dics)
        return t_dics

    def convert_text_to_raw(self, phrase):
        pass

    def convert_raw_to_count(self, datas):
        r_wordnum = {}
        for data in datas:
            if data in r_wordnum:
                r_wordnum[data] = r_wordnum[data] + 1
            else:
                r_wordnum[data] = 1
        return r_wordnum

    def ConvertRawToNormalFrequent(self, RawDicts, nrange):
        """
        function: caculate normalized frequence of words
        t_dics: dict words and its frequent
        nrange:the length of words
        t_frer: dict words and its frequence
        """
        t_fredic = {}
        t_biaozhun = {}
        t_mean = {}
        t_std = {}
        for i in range(1, nrange + 1):
            t_fredic[i] = []
            t_biaozhun[i] = []
        for key in RawDicts:
            t_fredic[len(key.split(' '))].append(RawDicts[key])

        for i in range(1,nrange + 1):
            t_fredic[i] = sum(t_fredic[i])
        t_frer = {}
        for key in RawDicts:
            t_frer[key] = -np.log(RawDicts[key] / t_fredic[len(key.split(' '))])
            t_biaozhun[len(key.split(' '))].append(t_frer[key])
        for i in range(1,nrange + 1):
            t_mean[i] = np.mean(np.array(t_biaozhun[i]))
            t_std[i] = np.std(np.array(t_biaozhun[i]),ddof = 1)
        for key in RawDicts:
            if t_std[len(key.split(' '))] != 0:
                t_frer[key] = (t_frer[key] - t_mean[len(key.split(' '))]) / t_std[len(key.split(' '))]
            else:
                t_frer[key] = 0
        return t_frer

    def ConvertListToOrder(self, rawlist):
        for item in rawlist:
            item.sort()
        return rawlist

    def MergeLists(self, ListA, ListB):
        s_los = set()
        for key in ListA:
            s_los.add(key)
        for key in ListB:
            s_los.add(key)
        l_los = list(s_los)
        l_los.sort()
        return l_los

    def MergeListGroup(self, ListsA, ListsB):
        i = 0
        MergeBorders = []
        for i in range(len(ListsA)):
            tempBorder = Converter().MergeLists(ListsA[i], ListsB[i])
            MergeBorders.append(tempBorder)
        return MergeBorders


word_converter = Converter()

if __name__ == '__main__':
    redis_cc = redis_deal()
    sys.exit()
    counter = Converter()
    datas = read_datas('/home/wxw/data/iec104', 'single')
    datas = get_puredatas(datas)
    counter.ConvertRawToDict(datas)
    #datas = read_datas('/home/wxw/data/modbustest', 'single')
    #datas = get_puredatas(datas)
    #datas = get_data_bylo(datas, 2, 5)
    #datas = counter.convert_raw_to_count(datas)
    #print(datas)



