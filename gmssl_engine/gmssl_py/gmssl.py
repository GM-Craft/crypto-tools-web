#!/usr/bin/env python3
# -*- coding: utf-8 -*-


################################################################################
from ctypes import *
import os
import sys


################################################################################
engine_path = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
GmSSL_path = os.path.join(engine_path, 'GmSSL')
bin_path = os.path.join(GmSSL_path, 'bin')
dll_path = os.path.join(bin_path, 'gmssl.dll')


################################################################################
SM4_KEY_SIZE = 16
SM4_BLOCK_SIZE = 16
_SM4_NUM_ROUNDS = 32
DO_ENCRYPT = True
DO_DECRYPT= False


################################################################################
class NativeError(Exception):
    """
    GmSSL libraray inner error
    """

try:
    GmSSL_dllHandle = cdll.LoadLibrary(dll_path)
except FileNotFoundError:
    raise

def gmssl_version():
    """
    return version num of GmSSL
    """

    return GmSSL_dllHandle.gmssl_version_num()


def rand_bytes(size):
    """
    generate a random number(Type:bytes) of a specified length
    """

    buf = create_string_buffer(size)
    GmSSL_dllHandle.rand_bytes(buf, c_size_t(size)) #write random number into buffer
    return buf.raw

def rand_int(size):
    """
    generate a random number(Type:int) of a specified length, byteorder='big'
    """

    radnint = int.from_bytes(rand_bytes(size), byteorder='big')
    return radnint



class Sm4(Structure):
    """
    Sm4 encryption and decryption
    """

    _fields_ = [
        ("rk", c_uint32 * _SM4_NUM_ROUNDS)
    ]

    def __init__(self, key:bytes):
        if len(key) != SM4_KEY_SIZE:
            raise ValueError('Invalid key length')
        self._key = key

    def encrypt(self, block:bytes):
        GmSSL_dllHandle.sm4_set_encrypt_key(byref(self), self._key)
        if len(block) != SM4_BLOCK_SIZE:
            raise ValueError('Invalid block size')
        outbuf = create_string_buffer(SM4_BLOCK_SIZE)
        GmSSL_dllHandle.sm4_encrypt(byref(self), block, outbuf)
        return outbuf.raw
    
    def decrypt(self, block:bytes):
        GmSSL_dllHandle.sm4_set_decrypt_key(byref(self), self._key)
        if len(block) != SM4_BLOCK_SIZE:
            raise ValueError('Invalid block size')
        outbuf = create_string_buffer(SM4_BLOCK_SIZE)
        GmSSL_dllHandle.sm4_encrypt(byref(self), block, outbuf)
        return outbuf.raw


class Sm4Cbc(Structure):
    """
    Sm4Cbc encryption and decryption
    """

    _fields_ = [
        ("sm4_key", Sm4),
        ("iv", c_uint8 * SM4_BLOCK_SIZE),
        ("block", c_uint8 * SM4_BLOCK_SIZE),
        ("block_nbytes", c_size_t)
    ]

    def __init__(self, key, iv):
        
        if len(key) != SM4_KEY_SIZE:
            raise ValueError('Invalid key length')
        if len(iv) != SM4_BLOCK_SIZE:
            raise ValueError('Invalid IV size')

        self._iv = iv
        self._key = key

    def update(self, data):
        outbuf = create_string_buffer(len(data) + SM4_BLOCK_SIZE)
        outlen = c_size_t()
        if self._encrypt == DO_ENCRYPT:
            if GmSSL_dllHandle.sm4_cbc_encrypt_update(byref(self), data, c_size_t(len(data)),
                outbuf, byref(outlen)) != 1:
                raise NativeError('libgmssl inner error')
        else:
            if GmSSL_dllHandle.sm4_cbc_decrypt_update(byref(self), data, c_size_t(len(data)),
                outbuf, byref(outlen)) != 1:
                raise NativeError('libgmssl inner error')
        return outbuf[0:outlen.value]

    def finish(self):
        outbuf = create_string_buffer(SM4_BLOCK_SIZE)
        outlen = c_size_t()
        if self._encrypt == True:
            if GmSSL_dllHandle.sm4_cbc_encrypt_finish(byref(self), outbuf, byref(outlen)) != 1:
                raise NativeError('libgmssl inner error')
        else:
            if GmSSL_dllHandle.sm4_cbc_decrypt_finish(byref(self), outbuf, byref(outlen)) != 1:
                raise NativeError('libgmssl inner error')
        return outbuf[:outlen.value]

    def encrypt(self, data:bytes):
        """
        for sm4_cbc encryption
        """

        self._encrypt = True
        if GmSSL_dllHandle.sm4_cbc_encrypt_init(byref(self), self._key, self._iv):
            ciphertext = self.update(data)
            ciphertext += self.finish()
            return ciphertext
        else:
            raise NativeError('libgmssl inner error')
    
    def decrypt(self, data:bytes):
        """
        for sm4_cbc decryption
        """

        self._encrypt = False
        if GmSSL_dllHandle.sm4_cbc_decrypt_init(byref(self), self._key, self._iv):
            plaintext = self.update(data)
            plaintext += self.finish()
            return plaintext
        else:
            raise NativeError('libgmssl inner error')


def main_test():

    key = b'1234567812345678'
    iv = b'1234567812345678'
    plaintext = b'0123456789abcdefg'

    sm4cbc = Sm4Cbc(key, iv)

    ret = sm4cbc.encrypt(plaintext)
    print(ret)

    ret1 = sm4cbc.decrypt(ret)
    print(ret1)


if __name__ == '__main__':
    main_test()

