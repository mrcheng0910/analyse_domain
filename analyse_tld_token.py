#!/usr/bin/python
# encoding:utf-8
"""
统计分析domain的长度
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
    sql = 'SELECT tld_token_count FROM domain_features'
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
        domain_length.append(int(line[0]))
    domain_length = np.array(domain_length)
    return domain_length


def draw(domain_length):
    """
    绘制柱装图
    :param domain_length:
    """
    x = []
    y = []
    domain_count = np.bincount(domain_length)
    ii = np.nonzero(domain_count)[0]
    print zip(ii,domain_count[ii])
    for i,j in zip(ii,domain_count[ii]):
        x.append(i)
        y.append(j)
    x = np.array(x)
    y = np.array(y)/1000.0
    print x
    x_min,x_max = x.min(),x.max()
    plt.bar(x[:2],y[:2],align='center')
    plt.xticks(x[:2])
    plt.xlim(x_min-1,x_max+0.5)

    plt.xlabel(u'顶级域名级数')
    plt.ylabel(u'域名数量（K）')
    plt.show()


def main():
    df = create_data_array()
    draw(df)

if __name__ == '__main__':
    main()

