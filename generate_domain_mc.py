# encoding:utf-8
"""
使用马尔可夫链生成域名
"""
import numpy as np
from pandas import DataFrame


def get_char_transition(first_char,next_char):
    """
    获取字符的转移概率
    :return:
    """
    print "nihao"


def get_first_char():
    pass


def get_next_char(f):
    pass
n = 5
m = 36*37
data = np.zeros((m,n))
char = ['a', 'b', 'c', 'd', 'e']

def generate_domains(char,n):
    if n == 0:
        return
    get_next_char(char)


def main():
    generate_domains('a',7)


if __name__ == '__main__':
    main()
