#!/usr/bin/python
# encoding:utf-8
"""
统计域名某个长度内，每个位置出现字母/数字/特殊字符的频率
"""

import numpy as np
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
    sql = 'SELECT domain FROM domain_features limit 1000000'
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


def draw(domains):
    """
    绘制柱装图
    :param domains:
    """
    domain_location_num = 10  # 统计的域名位置个数
    fig = plt.figure()
    y = domains/1000
    x = np.arange(1,domain_location_num+1)
    symbol = ['-^','-v','->','-.','-<','-x','-d','-.']  # 线类型
    # 第一个图像设置(0-5)
    ax1 = fig.add_subplot(231)
    for i in range(0,6):
        ax1.plot(x,y[i][:10], symbol[i],label=chr(i+48), linewidth='1.0')
    ax1.legend(prop={'size':10})
    # ax1.grid()
    # plt.xlabel(u"域名位置")
    plt.ylabel(u"出现次数")

    #第二个图像设置(6-10,-)
    ax2 = fig.add_subplot(232)
    for i in range(6,10):
        ax2.plot(x,y[i][:10],symbol[i-6],label=chr(i+48),linewidth='1.0')
    ax2.plot(x,y[10][:10],symbol[6],label='-',linewidth='1.5')  # 设置'-'
    ax2.legend(prop={'size':10})
    # ax2.grid()
    # plt.xlabel(u"域名位置")
    # plt.ylabel(u"出现次数")

    # 设置第三个图像(a-f)
    ax3 = fig.add_subplot(233)
    for i in range(11,17):
        ax3.plot(x,y[i][:10],symbol[i-11],label=chr(i+97-11), linewidth='1.0')
    ax3.legend(prop={'size':10})
    # ax3.grid()
    # plt.xlabel(u"域名位置")
    # plt.ylabel(u"出现次数")

    # 设置第四个图像(g-m)
    ax4 = fig.add_subplot(234)
    for i in range(17,24):
        ax4.plot(x,y[i][:10],symbol[i-17],label=chr(i+97-11), linewidth='1.0')
    ax4.legend(prop={'size':9})
    # ax4.grid()
    plt.xlabel(u"域名位置")
    plt.ylabel(u"出现次数")

    # 设置第五个图像(n-t)
    ax5 = fig.add_subplot(235)
    for i in range(24,31):
        ax5.plot(x,y[i][:10],symbol[i-24],label=chr(i+97-11), linewidth='1.0')
    ax5.legend(prop={'size':9})
    # ax5.grid()
    plt.xlabel(u"域名位置")
    # plt.ylabel(u"出现次数")

    # 设置第六个图像(u-z)
    ax6 = fig.add_subplot(236)
    for i in range(31,37):
        ax6.plot(x, y[i][:10], symbol[i-31], label=chr(i+97-11), linewidth='1.0')
    ax6.legend(prop={'size':9})
    # ax6.grid()
    plt.xlabel(u"域名位置")
    # plt.ylabel(u"出现次数")

    plt.subplots_adjust(top=0.96, bottom=0.09, left=0.08, right=0.97,hspace=0.10,wspace=0.16)
    plt.savefig(u'各个字符在域名.png',dpi=140)
    plt.show()


def main():
    loc_char_count = create_data_array()
    draw(loc_char_count)

if __name__ == '__main__':
    main()

