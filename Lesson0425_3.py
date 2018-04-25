"""
邮校学习
0425
调用C
"""
from ctypes import *

msvcrt = cdll.LoadLibrary("msvcrt")  # Python3
# msvcrt = cdll.msvcrt  # Python2
msg = b"hello\n"
msvcrt.printf(b"astr:%s", msg)

import sqlite3

