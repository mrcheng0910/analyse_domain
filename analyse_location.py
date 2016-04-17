#!/usr/bin/python
# encoding:utf-8
"""
每个位置出现字母/数字/特殊字符的频率
"""

from data_base import MySQL
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'  # 支持中文字体


def fetch_data():
    """
    从数据库中获取域名(domain)基础数据
    :return: 返回基础数据
    """
    db = MySQL()
    sql = 'SELECT domain FROM domain_features limit 50000'
    db.query(sql)
    tlds = db.fetch_all_rows()
    db.close()
    return tlds


def create_data_array():
    """
    根据获取的基础数据，建立对应数据集合
    :return: 数据集合
    """
    domains_data = fetch_data()  # tld基础数据
    domain_length = 15
    domains = np.zeros((37,70))


    for line in domains_data:
        for index_char,char in enumerate(line[0]):
            char_num = judge_char_num(char)
            domains[char_num][index_char] += 1

    return domains

def judge_char_num(char):

    ascii_value = ord(char)
    if 48 <= ascii_value <=57:
        return ascii_value-48
    elif 97 <= ascii_value <= 122:  # To find occurrences of [a-z]
        return ascii_value-97+11
    elif 65 <= ascii_value <= 90:  # To find occurrences of [A-Z]
        return ascii_value - 65 + 11
    else :
        return 11


def draw(domains):
    """
    绘制柱装图
    :param digits_chars:
    """
    fig =plt.figure()
    y = domains
    x = np.arange(10)
    ax1 = fig.add_subplot(111)
    for i in range(11,15):
        ax1.plot(x,y[i][:10],label=str(i))

    # ax1.plot(x,y,'r')
    # ax1.set_xticks(x)
    # ax1.set_xticklabels(x_label)
    plt.legend()
    plt.grid()
    plt.show()


def main():
    domains = create_data_array()
    draw(domains)

if __name__ == '__main__':
    main()

