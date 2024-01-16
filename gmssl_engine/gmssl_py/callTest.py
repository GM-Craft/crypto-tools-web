from gmssl import gmssl_version, rand_bytes, rand_int, Sm4


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

def test_sm4():
    key = b'1234567812345678'
    decrypted = b'block of message'
    ciphertext_hex = 'dd99d30fd7baf5af2930335d2554ddb7'
    sm4 = Sm4(key)
    ciphertext = sm4.encrypt(decrypted)
    cipher_hex = ciphertext.hex()
    print(cipher_hex)
    assert(cipher_hex == ciphertext_hex)

    decrypted_text = sm4.decrypt(ciphertext)
    print(decrypted_text)
    assert(decrypted_text == decrypted)



if __name__ == '__main__':
    test_sm4()