#!/usr/bin/python
# encoding:utf-8
"""
统计域名某个长度内，每个位置出现字母/数字/特殊字符的频率
"""

import numpy as np
from pandas import DataFrame
from data_base import MySQL

def fetch_data():
    """
    从数据库中获取域名(domain)基础数据
    :return: 返回基础数据
    """
    db = MySQL()
    sql = 'SELECT domain FROM domain_features'
    db.query(sql)
    domains = db.fetch_all_rows()
    db.close()
    return domains


def create_data_array():
    """
    根据获取的基础数据，建立对应数据集合
    :return: 数据集合
    """
    domains_data = fetch_data()  # tld基础数据
    domain_length = 70   # 该长度根据测试数据集的最长域名来设置
    loc_char_count = np.zeros((37, domain_length))  # 初始化二维列表，域名位置字符计数

    for line in domains_data:
        for index_char,char in enumerate(line[0]):
            char_num = judge_char_num(char)  # 获得域名组成字符编号
            loc_char_count[char_num][index_char] += 1

    return loc_char_count


def judge_char_num(char):

    ascii_value = ord(char)
    if 48 <= ascii_value <= 57:
        return ascii_value-48
    elif 97 <= ascii_value <= 122:  # To find occurrences of [a-z]
        return ascii_value-97+11
    elif 65 <= ascii_value <= 90:  # To find occurrences of [A-Z]
        return ascii_value - 65 + 11
    else :
        return 11


def main():
    loc_char_count = create_data_array()
    # print loc_char_count
    count_sum = loc_char_count.sum(axis=0)
    # print count_sum
    count_sum[count_sum==0] = 1
    # print count_sum

    test =  loc_char_count/count_sum
    df=  DataFrame(test)
    df.to_csv('./data/char_loc_freq.csv')
    print df.head(4)
    print df.ix(3)[2]
    # for i in range(5):
    #     print test[i][:10]df[(df["0"] == 11) & (df["second_char"] == 13)]
    # for i in test:
    #     print i[:15]
    # draw(loc_char_count)

if __name__ == '__main__':
    main()

