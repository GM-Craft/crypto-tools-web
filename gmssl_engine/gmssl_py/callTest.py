from gmssl import gmssl_version, rand_bytes, rand_int

def versiontest():
    version = gmssl_version()
    print(version)

def random_byte_test():
    randnum = rand_bytes(1)
    print(randnum)

def random_int_test():
    randnum = rand_int(1)
    print(randnum)

if __name__ == '__main__':
    random_int_test()