from treef_loc import treefL
import sys
sys.path.append("../common/Model")
from canf import prime_b

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

do_init()
