#!/usr/bin/python
# encoding:utf-8
"""
统计
"""

from data_base import MySQL
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'  # 支持中文字体


def fetch_data():
    """
    从数据库中获取域名长度(domain_length)基础数据
    :return: 返回基础数据
    """
    db = MySQL()
    sql = 'SELECT tld FROM domain_features WHERE tld_token_count = "2"'
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
    x = pd.value_counts(pd.Series(entire_tlds)).index[:25]
    y = pd.value_counts(pd.Series(entire_tlds)).values[:25]/1000.0
    for label in x:
        x_label.append(str(label))
    x = np.arange(len(y))

    ax = fig.add_subplot(121)
    ax.bar(x,y)
    ax.set_xticks(x)
    ax.set_xticklabels(x_label,rotation=50)
    plt.grid(axis='y')
    plt.ylabel(u'域名数量(K)')
    plt.xlabel(u'二级顶级域名')

    x_label = []
    x = pd.value_counts(pd.Series(sub_tlds)).index[:20]  # 去重
    y = pd.value_counts(pd.Series(sub_tlds)).values[:20]/1000.0  # 去重
    for label in x:
        x_label.append(str(label))
    x = np.arange(len(y))
    ax2 = fig.add_subplot(122)
    ax2.bar(x,y)
    ax2.set_xticks(x)
    ax2.set_xticklabels(x_label,rotation=50)
    plt.grid(axis='y')
    plt.xlabel(u'第二级顶级域名')

    plt.subplots_adjust(top=0.96,bottom=0.15,left=0.06,right=0.98,wspace=0.10)
    plt.savefig(u"二级顶级域名",dpi=140)


    # x_label = []
    # x = pd.value_counts(pd.Series(first_tlds)).index[:20]
    # y = pd.value_counts(pd.Series(first_tlds)).values[:20]
    # for label in x:
    #     x_label.append(str(label))
    # x = np.arange(len(y))
    # ax3 = fig.add_subplot(223)
    # ax3.bar(x,y)
    # ax3.set_xticks(x)
    # ax3.set_xticklabels(x_label,rotation=50)
    # plt.grid()

    plt.show()


def main():
    entire_tlds, sub_tlds, first_tlds = create_data_array()
    draw(entire_tlds, sub_tlds,first_tlds)


if __name__ == '__main__':
    main()

