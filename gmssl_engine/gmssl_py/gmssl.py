#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import *
import os
import sys


engine_path = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
GmSSL_path = os.path.join(engine_path, 'GmSSL')
bin_path = os.path.join(GmSSL_path, 'bin')
dll_path = os.path.join(bin_path, 'gmssl.dll')

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


def main_test():
    rand = rand_bytes(1)
    print(rand)
    print(type(rand))

if __name__ == '__main__':
    main_test()

