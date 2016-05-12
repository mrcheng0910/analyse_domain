#!/usr/bin/python
# encoding:utf-8
"""
统计分析各个字母（a-z）、数字（0-9）和特殊字符'-'出现的频率和次数
"""

from data_base import MySQL
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'  # 支持中文字体


def fetch_data():
    """
    从数据库中获取域名长度(domain_length)基础数据
    :return: 返回基础数据
    """
    db = MySQL()
    sql = 'SELECT domain_characters,domain_digit FROM domain_features'
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
        digits.append(list(eval(line[1])))
    chars = np.array(chars)
    digits = np.array(digits)

    return chars.mean(axis=0),digits.mean(axis=0)


def draw(digits_chars):
    """
    绘制柱装图
    :param digits_chars:
    """
    fig = plt.figure()
    y = digits_chars
    x = np.arange(len(y))
    x_label_digit = [i for i in range(10)]
    x_label_char = [chr(i) for i in range(97,123)]
    x_label_char.insert(0, '-')
    x_label = x_label_digit + x_label_char
    series_data = Series(y,x_label)
    fig.add_subplot(121)
    plt.plot(x, series_data.values, 'k-o', label=u"字符频率")
    plt.legend(prop={'size':11})
    x_min,x_max = x.min(), x.max()
    plt.xlim(x_min-1,x_max+1)
    plt.xticks(x,series_data.index)  # x坐标显示内容
    # plt.grid()
    plt.xlabel(u"字符")
    plt.ylabel(u"所占比例(%)")

    fig.add_subplot(122)
    series_data = series_data.sort_values(ascending=False)
    plt.bar(x,series_data.values,label=u'字符频率', align='center')
    plt.legend(prop={'size':11})
    x_min,x_max = x.min(), x.max()
    plt.xlim(x_min-1,x_max+1)
    plt.xticks(x,series_data.index)  # x坐标显示内容
    # plt.grid()
    plt.xlabel(u"字符")
    plt.ylabel(u"所占比例(%)")

    plt.subplots_adjust(top=0.96, bottom=0.09, left=0.06, right=0.96)
    # plt.savefig(u'字符频率.png')

    plt.show()


def main():
    chars,digits = create_data_array()
    draw(np.concatenate((digits,chars)))
if __name__ == '__main__':
    main()

