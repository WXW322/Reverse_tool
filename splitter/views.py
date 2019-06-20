from common.readdata import *
from merger.base_merger import base_merger
from protocol_analysis.word_simple import word_infer
from Fields_info.const_field import loc_field
from common.Converter.word_converter import word_convert
from common.analyzer.analyzer_common import base_analyzer
from splitter.vertical_splitter import vertical_splitter

def get_vertical_borders(file_dir):
    ver_split = vertical_splitter()
    datas = read_datas(file_dir, 'single')
    datas = get_puredatas(datas)
    w_result = ver_split.split_by_words_type(datas, 15)
    w_convert = word_convert()
    borders = w_convert.itemtoborder([word.loc for word in w_result])
    print(borders)

if __name__ == '__main__':
    get_vertical_borders('')

