#!/usr/bin/python
# encoding:utf-8
"""
统计分析各个字母（a-z）、数字（0-9）和特殊字符'-'出现的频率和次数
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
    sql = 'SELECT domain_characters,domain_digit FROM domain_features limit 300'
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

    digit_char_count = []
    for i in range(10):
        digit_char_count.append(np.count_nonzero(digits.T[i]))
    for i in range(27):
        digit_char_count.append(np.count_nonzero(chars.T[i]))
    digit_char_count = np.array(digit_char_count)
    return chars.mean(axis=0),digits.mean(axis=0),digit_char_count/float(digit_char_count.sum())*100


def draw(digits_chars, digit_char_count):
    """
    绘制柱装图
    :param digits_chars:
    """
    fig = plt.figure()
    y = digits_chars
    y1 = digit_char_count
    x = np.arange(len(y))
    x_label_digit = [i for i in range(10)]
    x_label_char = [chr(i) for i in range(97,123)]
    x_label_char.insert(0, '-')
    x_label = x_label_digit + x_label_char
    fig.add_subplot(111)
    plt.plot(x, y, 'k-o', label=u"字符出现次数",linewidth='1.0')
    plt.plot(x, y1, 'r-^', label=u"域名含有字符", linewidth='1.0')
    plt.legend(prop={'size':12})
    x_min,x_max = x.min(), x.max()
    plt.xlim(x_min-1,x_max+1)
    plt.xticks(x,x_label)  # x坐标显示内容
    plt.grid(axis='y')
    plt.xlabel(u"字符")
    plt.ylabel(u"所占比例(%)")
    plt.subplots_adjust(top=0.96, bottom=0.09, left=0.06, right=0.96)
    plt.savefig(u'域名出现次数与频率比较.png')
    plt.show()


def main():
    chars,digits,digit_char_count = create_data_array()
    draw(np.concatenate((digits,chars)),digit_char_count)

if __name__ == '__main__':
    main()

