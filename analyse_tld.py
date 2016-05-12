#!/usr/bin/python
# encoding:utf-8
"""
统计分析domain的长度
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
    sql = 'SELECT tld FROM domain_features'
    sql = 'SELECT SUBSTRING_INDEX(tld,".",-1) as a FROM domain_features'
    db.query(sql)
    domains_length = db.fetch_all_rows()
    db.close()
    return domains_length


def create_data_array():
    """
    根据获取的基础数据，建立对应的测试数据集合
    :return: 数据集合
    """
    domains = fetch_data()  # domain基础数据
    domain_length = []  # domain的长度
    for line in domains:
        domain_length.append(line[0])
    domain_length = np.array(domain_length)
    return domain_length


def draw(domain_length):
    """
    绘制柱装图
    :param domain_length:
    """
    x_label = []
    x = pd.value_counts(pd.Series(domain_length)).index[:25]
    y = pd.value_counts(pd.Series(domain_length)).values[:25]/1000.0
    for label in x:
        x_label.append(str(label))
    x = np.arange(len(y))
    fig = plt.figure()
    fig.add_subplot(111)
    plt.bar(x,y,align='center')
    x_min,x_max = x.min(), x.max()
    y_min,y_max = y.min(), y.max()
    plt.xlabel(u'顶级域名')
    plt.ylabel(u'域名个数(K)')
    plt.xlim(x_min-1, x_max+1)
    plt.ylim(y_min, y_max+10)
    plt.xticks(x,x_label,rotation=50)
    # plt.grid(axis='y')
    plt.subplots_adjust(top=0.95,bottom=0.15,left=0.08,right=0.97)
    plt.savefig(u"各个顶级域名含有的域名数量",dpi=140)
    plt.show()


def main():
    df = create_data_array()
    draw(df)

if __name__ == '__main__':
    main()

