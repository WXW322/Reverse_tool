from treef_loc import treefL
import sys
sys.path.append("../common/Model")
sys.path.append("../splitter/")
from canf import prime_b
from VE_splitter import splitter

def get_format_by_voting_expert(messages, h, combine, model, v_way, T, r):
    message_splitter = splitter()
    message_split = message_splitter.split_by_ve(messages, h, combine, model, v_way, T, r)
    tree_builder = treefL(message_split, int(0.1 * len(message_split)), 0.2)
    t_result = tree_builder.generate_T()
    t_result.depth_traverse()
    for f in t_result.result:
        print("format start")
        for node_i in f:
            print(node_i.loc)




def do_init():
    t_temp = []
    t_temp.append(prime_b([0,1,3,5,7]))
    t_temp.append(prime_b([0,1,3,5,9]))
    t_temp.append(prime_b([0,1,3,5,10]))
    t_temp.append(prime_b([0,2,4,6,7]))
    t_temp.append(prime_b([0,2,4,6,8]))
    t_temp.append(prime_b([0,2,4,6,10]))
    t_keys = {}
    for i, item in enumerate(t_temp):
        t_keys[i] = item
    tree_builder = treefL(t_keys, 3, 0.2)
    t_result = tree_builder.generate_T()
    t_result.depth_traverse()
    for f in t_result.result:
        print("format start")
        for node_i in f:
            print(node_i.loc)

def do_format_T(path, r_way, h, combine, model, v_way, T, r):
    datas = read_datas(data_path, r_way)
    datas = get_puredatas(datas)
    messages = add_tail(datas, h)
    get_format_by_voting_expert(messages, h, combine, model, v_way, T, r)

do_format_T("/home/wxw/data/iec104_test", "single", 4, "yes", "abs", "normal", 0, 0)


