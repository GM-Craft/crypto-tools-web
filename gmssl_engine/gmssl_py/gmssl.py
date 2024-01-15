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

def main_test():
    version = gmssl_version()
    print(version)

if __name__ == '__main__':
    main_test()

