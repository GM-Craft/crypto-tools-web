from gmssl import gmssl_version, rand_bytes, rand_int, Sm4, Sm4Cbc


DO_ENCRYPT=True
DO_DECRYPT = False

def versiontest():
    version = gmssl_version()
    print(version)

def random_byte_test():
    randnum = rand_bytes(1)
    print(randnum)

def random_int_test():
    randnum = rand_int(1)
    print(randnum)

def sm4_test():
    key = b'1234567812345678'
    plaintext = b'block of message'

    sm4 = Sm4(key)
    encrypted = sm4.encrypt(plaintext)
    decrypted = sm4.decrypt(encrypted)

    print('原文是：{}， \n密文是：{}，\n 解密后:{}'.format(plaintext, encrypted, decrypted))

def sm4cbc_test():
    key = b'1234567812345678'
    iv = b'1234567812345678'
    plaintext = b'1234567812345678'

    sm4cbc = Sm4Cbc(key, iv)
    encrypted = sm4cbc.encrypt(plaintext)
    decrypted = sm4cbc.decrypt(encrypted)

    print('原文是：{}， \n密文是：{}，\n 解密后:{}'.format(plaintext, encrypted, decrypted))


if __name__ == '__main__':
    sm4_test()
    sm4cbc_test()