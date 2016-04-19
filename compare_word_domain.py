#!/usr/bin/python
# encoding:utf-8
"""
统计域名字母出现的频率与字母频率之间的关系
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
    sql = 'SELECT domain_characters FROM domain_features limit 100000'
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

    digit_char_count = []
    for i in range(1,27):
        digit_char_count.append(np.count_nonzero(chars.T[i]))

    return np.array(digit_char_count),chars.mean(axis=0)


def draw(char_count,chars):
    """
    绘制柱装图
    :param digits_chars:
    """
    fig = plt.figure()
    y = [8.167, 1.492, 2.782, 4.253, 12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,
         1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
    y = [8.4966,2.0720,4.5388,3.3844,11.1607,1.8121,2.4705,3.0034,7.5448,0.1965,1.1016,5.4893,3.0129,6.6544,7.1635,3.1671,0.1962,7.5809,
         5.7351,6.9509,3.6308,1.0074,1.2899,0.2902,1.7779,0.2722]

    y1 = char_count/float(char_count.sum())*100
    x = np.arange(len(char_count))
    x_label = [chr(i) for i in range(97,123)]

    # 设置子图1显示格式
    ax1 = fig.add_subplot(121)
    ax1.plot(x, y1, '-^', label=u"域名中字母次数", linewidth='1.5')
    ax1.plot(x, y, '-d', label=u"字母频率", linewidth='1.5')
    ax1.set_xticks(x)
    ax1.set_xticklabels(x_label)
    plt.xlabel(u"字母")
    plt.ylabel(u"频率(%)")
    plt.legend()
    plt.grid()

    # 设置子图2格式
    ax2 = fig.add_subplot(122)
    ax2.plot(x, chars[1:], '-^', label=u"域名中字母频率", linewidth='1.5')
    ax2.plot(x, y, '-d', label=u"字母频率", linewidth='1.5')
    ax2.set_xticks(x)
    ax2.set_xticklabels(x_label)
    plt.xlabel(u"字母")
    plt.ylabel(u"频率(%)")
    plt.legend()
    plt.grid()

    plt.show()


def main():
    digit_char_count,chars = create_data_array()
    draw(digit_char_count,chars)

if __name__ == '__main__':
    main()

