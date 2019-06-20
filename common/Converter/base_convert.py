from common.readdata import *

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

if __name__ == '__main__':
    counter = Converter()
    datas = read_datas('/home/wxw/data/modbustest', 'single')
    datas = get_puredatas(datas)
    datas = get_data_bylo(datas, 2, 5)
    datas = counter.convert_raw_to_count(datas)
    print(datas)



