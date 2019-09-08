import sys
sys.path.insert(0, '/home/nikon/crypto/des/des_python')

from des.des import *
from utils.utils import *

if __name__ == '__main__':
    des = DES()
    utils = Utils()

    msg = "00101010010100101100101010010"
    msg = utils.pad_binary_str(msg)

    key = "011111101010101010011010101010010101010"
    key = utils.pad_to(key, 64)

    msg = list(msg)

    msg = des.encrypt(msg, key)

    print(''.join(msg))
    