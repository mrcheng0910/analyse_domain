#!/usr/bin/python
# encoding:utf-8
"""
统计域名前六个位置出现各个字符的频率,
该程序可优化
"""

import numpy as np
from pandas import Series
import matplotlib.pyplot as plt
from matplotlib import rcParams

from data_base import MySQL

rcParams['font.family'] = 'SimHei'  # 支持中文字体


def fetch_data():
    """
    从数据库中获取域名(domain)基础数据
    :return: 返回基础数据
    """
    db = MySQL()
    sql = 'SELECT domain FROM domain_features limit 500000'
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
    # 域名前六位
    first_loc = {}
    second_loc = {}
    third_loc = {}
    fourth_loc = {}
    fifth_loc = {}
    sixth_loc = {}

    for line in domains_data:
        try:
            # 第一个位置
            if line[0][0] in first_loc.keys():
                first_loc[line[0][0]] += 1
            else:
                first_loc[line[0][0]] = 1
            # 第二个位置
            if line[0][1] in second_loc.keys():
                second_loc[line[0][1]] += 1
            else:
                second_loc[line[0][1]] = 1
            # 第三个位置
            if line[0][2] in third_loc.keys():
                third_loc[line[0][2]] += 1
            else:
                third_loc[line[0][2]] = 1
            # 第四个位置
            if line[0][3] in fourth_loc.keys():
                fourth_loc[line[0][3]] += 1
            else:
                fourth_loc[line[0][3]] = 1
            # 第五个位置
            if line[0][4] in fifth_loc.keys():
                fifth_loc[line[0][4]] += 1
            else:
                fifth_loc[line[0][4]] = 1
            # 第四个位置
            if line[0][5] in sixth_loc.keys():
                sixth_loc[line[0][5]] += 1
            else:
                sixth_loc[line[0][5]] = 1
        except:
            continue  # 域名长度小于4的，直接跳过

    first_loc = Series(first_loc).sort_values(ascending=False)
    second_loc = Series(second_loc).sort_values(ascending=False)
    third_loc = Series(third_loc).sort_values(ascending=False)
    fourth_loc = Series(fourth_loc).sort_values(ascending=False)
    fifth_loc = Series(fifth_loc).sort_values(ascending=False)
    sixth_loc = Series(sixth_loc).sort_values(ascending=False)
    return first_loc,second_loc,third_loc,fourth_loc,fifth_loc,sixth_loc


def draw(first_loc,second_loc,third_loc,fourth_loc,fifth_loc,sixth_loc):
    """
    绘制柱装图
    :param domains:
    """
    fig = plt.figure()

    fig.add_subplot(231)
    y = first_loc.values
    x_label =  first_loc.index
    x = np.arange(len(x_label))
    plt.plot(x,y/1000.0,'k--',linewidth='2.0',label=u"趋势")
    plt.bar(x,y/1000.0,color='g',align='center',label=u"次数")
    plt.xticks(x,x_label)
    x_min,x_max = x.min(),x.max()
    plt.xlim(x_min-1,x_max+1)
    # plt.grid()
    plt.legend()
    # plt.xlabel(u"字符")
    plt.ylabel(u"出现次数(K)")

    fig.add_subplot(232)
    y = second_loc.values
    x_label = second_loc.index
    x = np.arange(len(x_label))
    plt.plot(x,y/1000.0,'k--',linewidth='2.0',label=u"趋势")
    plt.bar(x,y/1000.0,color='g',align='center',label=u"次数")
    plt.xticks(x,x_label)
    x_min,x_max = x.min(), x.max()
    plt.xlim(x_min-1,x_max+1)
    # plt.grid()
    plt.legend()
    # plt.xlabel(u"字符")
    # plt.ylabel(u"出现次数")

    fig.add_subplot(233)
    y = third_loc.values
    x_label = third_loc.index
    x = np.arange(len(x_label))
    plt.plot(x, y/1000.0,'k--',linewidth='2.0',label=u"趋势")
    plt.bar(x, y/1000.0,color='g',align='center',label=u"次数")
    plt.xticks(x,x_label)
    x_min, x_max = x.min(), x.max()
    plt.xlim(x_min-1,x_max+1)
    # plt.grid()
    plt.legend()
    # plt.xlabel(u"字符")
    # plt.ylabel(u"出现次数")

    fig.add_subplot(234)
    y = fourth_loc.values
    x_label = fourth_loc.index
    x = np.arange(len(x_label))
    plt.plot(x, y/1000.0,'k--',linewidth='2.0',label=u"趋势")
    plt.bar(x,y/1000.0,color='g',align='center',label=u"次数")
    plt.xticks(x,x_label)
    x_min,x_max = x.min(),x.max()
    plt.xlim(x_min-1,x_max+1)
    # plt.grid()
    plt.legend()
    plt.xlabel(u"字符")
    plt.ylabel(u"出现次数(K)")

    fig.add_subplot(235)
    y = fifth_loc.values
    x_label = fifth_loc.index
    x = np.arange(len(x_label))
    plt.plot(x, y/1000.0, 'k--',linewidth='2.0',label=u"趋势")
    plt.bar(x, y/1000.0, color='g',align='center',label=u"次数")
    plt.xticks(x,x_label)
    x_min,x_max = x.min(), x.max()
    plt.xlim(x_min-1,x_max+1)
    # plt.grid()
    plt.legend()
    plt.xlabel(u"字符")
    # plt.ylabel(u"出现次数")

    fig.add_subplot(236)
    y = sixth_loc.values
    x_label = sixth_loc.index
    x = np.arange(len(x_label))
    plt.plot(x, y/1000.0,'k--',linewidth='2.0',label=u"趋势")
    plt.bar(x, y/1000.0,color='g',align='center',label=u"次数")
    plt.xticks(x,x_label)
    x_min,x_max = x.min(),x.max()
    plt.xlim(x_min-1,x_max+1)
    # plt.grid()
    plt.legend()
    plt.xlabel(u"字符")
    # plt.ylabel(u"出现次数")

    plt.subplots_adjust(wspace=0.1,hspace=0.1,left=0.05,right=0.97)
    plt.show()


def main():
    first_loc, second_loc, third_loc,fourth_loc,fifth_loc,sixth_loc = create_data_array()
    draw(first_loc, second_loc, third_loc,fourth_loc,fifth_loc,sixth_loc)

if __name__ == '__main__':
    main()

