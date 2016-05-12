#!/usr/bin/python
# encoding:utf-8
"""
生成转移矩阵
"""

import numpy as np
from pandas import DataFrame
from matplotlib import rcParams

from data_base import MySQL

rcParams['font.family'] = 'SimHei'  # 支持中文字体


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
    domains_data = fetch_data()  #
    first_sec_count = np.zeros((37, 37))  #
    first_sec_probability = np.zeros((37,37))
    for line in domains_data:
        for i in range(1, len(line[0])):
            first_num = judge_char_num(line[0][i-1])
            second_num = judge_char_num(line[0][i])
            first_sec_count[first_num][second_num] += 1

    char_sum = first_sec_count.sum(axis=1)

    for i in range(37):
        for j in range(37):
            first_sec_probability[i][j] = first_sec_count[i][j]/float(char_sum[i])

    data = {'first_char': [],
            'second_char': [],
            'probability': []
            }
    for i in range(37):
        for j in range(37):
            data['first_char'].append(i)
            data['second_char'].append(j)
            data['probability'].append(first_sec_probability[i][j])

    df = DataFrame(data)
    # print df[(df["first_char"] == 0) & (df["second_char"] == 1)]["probability"]
    # print df[(df["first_char"] == 12)][["probability","second_char"]]
    df.to_csv('./data/transition_matrix.csv')
    print df

def judge_char_num(char):

    ascii_value = ord(char)
    if 48 <= ascii_value <= 57:
        return ascii_value-48
    elif 97 <= ascii_value <= 122:  # To find occurrences of [a-z]
        return ascii_value-97+11
    elif 65 <= ascii_value <= 90:  # To find occurrences of [A-Z]
        return ascii_value - 65 + 11
    else:
        return 11


def main():
    create_data_array()
    # df = DataFrame.from_csv('hmm.csv')
    # data =  df[(df["first_char"] == 11) & (df["second_char"] == 13)]["probability"]
    # print data.values
    # first_loc, second_loc, third_loc,fourth_loc,fifth_loc,sixth_loc = create_data_array()
    # draw(first_loc, second_loc, third_loc,fourth_loc,fifth_loc,sixth_loc)

if __name__ == '__main__':
    main()

