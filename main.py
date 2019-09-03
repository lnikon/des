from des import DES

if __name__ == '__main__':
    des = DES()

    msg = "hello"
    msg = des.initial_permutation(msg)
    print(msg)
    