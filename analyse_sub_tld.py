#!/usr/bin/python
# encoding:utf-8
"""
统计
"""

from data_base import MySQL
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def fetch_data():
    """
    从数据库中获取域名长度(domain_length)基础数据
    :return: 返回基础数据
    """
    db = MySQL()
    sql = 'SELECT tld FROM domain_features WHERE tld_token_count = "2" limit 20000'
    db.query(sql)
    tlds = db.fetch_all_rows()
    db.close()
    return tlds


def create_data_array():
    """
    根据获取的基础数据，建立对应的测试数据集合
    :return: 数据集合
    """
    tlds = fetch_data()  # tld基础数据
    entire_tlds = []  # 完整顶级后缀
    first_tlds = []  # 顶级二级后缀
    sub_tlds = []  # 次级二级后缀
    for line in tlds:
        entire_tlds.append(line[0])
        sub_tlds.append(line[0].split('.')[0])
        first_tlds.append(line[0].split('.')[1])

    entire_tlds = np.array(entire_tlds)
    sub_tlds = np.array(sub_tlds)
    first_tlds = np.array(first_tlds)
    return entire_tlds,sub_tlds,first_tlds


def draw(entire_tlds,sub_tlds,first_tlds):
    """
    绘制柱装图
    :param entire_tlds:
    """
    fig =plt.figure()

    x_label = []
    x = pd.value_counts(pd.Series(entire_tlds)).index[:20]
    y = pd.value_counts(pd.Series(entire_tlds)).values[:20]
    for label in x:
        x_label.append(str(label))
    x = np.arange(len(y))

    ax = fig.add_subplot(221)
    ax.bar(x,y)
    ax.set_xticks(x)
    ax.set_xticklabels(x_label,rotation=50)
    plt.grid()

    x_label = []
    x = pd.value_counts(pd.Series(sub_tlds)).index[:20]
    y = pd.value_counts(pd.Series(sub_tlds)).values[:20]
    for label in x:
        x_label.append(str(label))
    x = np.arange(len(y))
    ax2 = fig.add_subplot(222)
    ax2.bar(x,y)
    ax2.set_xticks(x)
    ax2.set_xticklabels(x_label,rotation=50)
    plt.grid()

    x_label = []
    x = pd.value_counts(pd.Series(first_tlds)).index[:20]
    y = pd.value_counts(pd.Series(first_tlds)).values[:20]
    for label in x:
        x_label.append(str(label))
    x = np.arange(len(y))
    ax3 = fig.add_subplot(223)
    ax3.bar(x,y)
    ax3.set_xticks(x)
    ax3.set_xticklabels(x_label,rotation=50)
    plt.grid()

    plt.show()


def main():
    entire_tlds, sub_tlds, first_tlds = create_data_array()
    draw(entire_tlds, sub_tlds,first_tlds)


if __name__ == '__main__':
    main()

