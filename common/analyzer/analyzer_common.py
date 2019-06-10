from Data_base.Data_redis.redis_deal import redis_deal
import sys

redis_read = redis_deal()
class base_analyzer:
    def __init__(self):
        pass


    def rank_words(self, key, min_num, top):
        raw_words = redis_read.read_from_redis(key)
        t_dic = {}
        t_dic[1] = []
        t_dic[2] = []
        t_dic[3] = []
        t_dic[4] = []
        t_dic[5] = []
        for word in raw_words:
            t_dic[len(word.split(' '))].append((word, raw_words[word]))
        for i in range(1, 5):
            t_dic[i] = sorted(t_dic[i], key = lambda key: key[1], reverse=True)
            print(len(t_dic[i]))
        t_result = {}
        for i in range(1, 5):
            t_result[i] = t_dic[i][0:top]
            t_last_items = [item[1] for item in t_dic[i][top:]]
            t_result[i].append(('left', sum(t_last_items)))
        return t_result

    def get_ith_word(self, t_words, word):
        t_candidate_words = t_words[len(word.split(' '))]
        i = 0
        for c_word in t_candidate_words:
            if(word == c_word):
                break
            i = i + 1
        print(i)

    def get_frequent(self, key, querys):
        raw_frequent = redis_read.read_from_redis(key)
        for query in querys:
            print('%s: %f' %(query, raw_frequent[query]))

    def get_topk(self, elements):
        t_result = {}
        for elem in elements:
            if elem not in t_result:
                t_result[elem] = 1
            else:
                t_result[elem] = t_result[elem] + 1
        t_result = sorted(t_result.items(), key = lambda key:key[1], reverse=True)
        return t_result








if __name__ == '__main__':
    analyzer = base_analyzer()
    t_results = analyzer.rank_words('correct_raw_words', 1, 1000)
    analyzer.get_ith_word(t_results, '104')
    analyzer.get_ith_word(t_results, '104 90')
    #analyzer.rank_words('raw_words', 1, 100)
    #analyzer.get_frequent("normal_correct_words", ['104', '104 90'])


