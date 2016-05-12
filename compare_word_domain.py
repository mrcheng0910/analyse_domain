#!/usr/bin/python
# encoding:utf-8
"""
统计域名字母出现的频率与字母频率之间的关系
"""

from data_base import MySQL
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'  # 支持中文字体


def fetch_data():
    """
    从数据库中获取域名长度(domain_length)基础数据
    :return: 返回基础数据
    """
    db = MySQL()
    sql = 'SELECT domain_characters FROM domain_features'
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
    chars = np.array(chars)
    return chars.mean(axis=0)


def draw(chars):
    """
    绘制柱装图
    :param digits_chars:
    """
    fig = plt.figure()
    y_niu = [8.4966,2.0720,4.5388,3.3844,11.1607,1.8121,2.4705,3.0034,7.5448,0.1965,1.1016,5.4893,3.0129,6.6544,7.1635,3.1671,0.1962,7.5809,
         5.7351,6.9509,3.6308,1.0074,1.2899,0.2902,1.7779,0.2722]
    y_domain = chars[1:]
    x = np.arange(26)
    x_label = [chr(i) for i in range(97, 123)]

    y_domain_series = Series(y_domain,index=x_label)
    y_niu_series = Series(y_niu,index=x_label)
    # 设置子图2格式
    fig.add_subplot(121)
    plt.plot(x, y_domain_series.values, 'b^-', label=u"域名字母频率")
    plt.plot(x, y_niu_series.values, 'r.-', label=u"牛津英语字典字母频率")
    plt.xticks(x,x_label)
    plt.xlabel(u"字母")
    plt.ylabel(u"所占比例(%)")
    plt.legend(prop={'size': 10})

    fig.add_subplot(122)
    bar_width = 0.3
    x_min,x_max = x.min(),x.max()

    plt.xlim(x_min,x_max+0.5)
    plt.bar(x,y_domain,bar_width,color='b',label=u'域名字母频率')
    plt.bar(x+bar_width,y_niu,bar_width,color='r',label=u"牛津英语字典字母频率")
    plt.xticks(x+bar_width,x_label)
    plt.xlabel(u"字母")
    plt.ylabel(u"所占比例(%)")
    plt.legend(prop={'size': 10})
    # plt.tight_layout()
    plt.show()


def main():
    chars = create_data_array()
    draw(chars)

if __name__ == '__main__':
    main()

