#!/usr/bin/python
# encoding:utf-8
"""
统计分析各个字母（a-z）、数字（0-9）和特殊字符'-'出现的频率和次数
"""

from data_base import MySQL
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'  # 支持中文字体
def fetch_data():
    """
    从数据库中获取域名长度(domain_length)基础数据
    :return: 返回基础数据
    """
    db = MySQL()
    sql = 'SELECT domain_characters,domain_digit FROM domain_features limit 500000'
    db.query(sql)
    tlds = db.fetch_all_rows()
    db.close()
    return tlds


def create_data_array():
    """
    根据获取的基础数据，建立对应的测试数据集合
    :return: 数据集合
    """
    chars_data = fetch_data()  # tld基础数据
    chars = []  # 完整顶级后缀
    digits = []
    for line in chars_data:
        chars.append(list(eval(line[0])))
        digits.append(list(eval(line[1])))
    chars = np.array(chars)
    digits = np.array(digits)

    digit_char_count = []
    for i in range(10):
        digit_char_count.append(np.count_nonzero(digits.T[i]))
    for i in range(27):
        digit_char_count.append(np.count_nonzero(chars.T[i]))

    return chars.mean(axis=0)/100,digits.mean(axis=0)/100,digit_char_count

def get_digit_char_count(digits_chars):
    digit_char_counts = []
    for i in range(37):
        digit_char_counts.append(np.count_nonzero(digits_chars.T[i]))
    return digit_char_counts


def draw(digits_chars,digit_char_count):
    """
    绘制柱装图
    :param digits_chars:
    """
    fig =plt.figure()
    y = digits_chars
    y1 = digit_char_count
    x = np.arange(len(y))
    x_label_digit = [i for i in range(10)]
    x_label_char = [chr(i) for i in range(97,123)]
    x_label_char.insert(0,'-')
    x_label = x_label_digit+x_label_char
    ax1 = fig.add_subplot(111)
    ax1.plot(x,y,'r',label=u"频率")
    ax1.legend(loc=1)
    ax1.set_xticks(x)
    ax1.set_xticklabels(x_label)
    ax2 = ax1.twinx()
    ax2.plot(x,y1,'k--',label=u"次数")
    ax2.legend(loc=2)
    # plt.legend()
    plt.grid()


    # ax2 = fig.add_subplot(122)
    # ax2.plot(x,y1)
    # ax2.set_xticks(x)
    # ax2.set_xticklabels(x_label)
    # # plt.legend()
    # plt.grid()

    plt.show()


def main():
    chars,digits,digit_char_count = create_data_array()
    draw(np.concatenate((digits,chars)),digit_char_count)

if __name__ == '__main__':
    main()

