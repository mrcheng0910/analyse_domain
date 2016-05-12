#!/usr/bin/python
# encoding:utf-8
"""
统计域名字母出现的频率与字母频率之间的关系
"""

from data_base import MySQL
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'  # 支持中文字体


def create_data_array():
    """
    根据获取的基础数据，建立对应的测试数据集合
    :return: 数据集合
    """

    # chars_data = fetch_data()  # tld基础数据
    # chars = []  # 完整顶级后缀
    digits = []
    # for line in chars_data:
    #     chars.append(list(eval(line[0])))
    # chars = np.array(chars)
    # return chars.mean(axis=0)


def draw():
    """
    绘制柱装图
    :param digits_chars:
    """

    x_labels = ['1K','10K','100K','200K','500K','1000K','2000K','5000K']
    # x_label = [1,2,3,4,5,6,7]
    data = np.array([[36,718,158,0,0,0,0,0],
                    [36,1070,6385,1489,0,0,0,0],
                    [36,1296,18894,58542,12306,2,0,0],
                    [36,1296,23080,103083,53688,455,0,0],
                    [36,1296,28887,180850,226485,16420,0,0],
                    [36,1296,33595,103083,252200,104164,239,0],
                    [36,1296,38177,333791,1001466,432194,7157,0],
                    [36,1296,42821,464702,2017262,1857306,155181,78]],dtype=np.float64

        )
    # print data

    data_sum = data.sum(axis=1)
    # print data_sum

    test = []
    for i in range(8):
        test.append(data[i]/data_sum[i])
    x = np.arange(1,9)
    df = DataFrame(test)
    df = df.T
    plt.bar(x,df.ix[0],color='r',label="1",align='center')
    bottom = df.ix[0]
    plt.bar(x,df.ix[1],color='b',label="2",bottom=bottom,align='center')
    bottom = df.ix[0]+df.ix[1]
    plt.bar(x,df.ix[2],color='y',label="3",bottom=bottom,align='center')
    bottom = df.ix[0]+df.ix[1]+df.ix[2]
    plt.bar(x,df.ix[3],color='m',label="4",bottom=bottom,align='center')
    bottom = df.ix[0]+df.ix[1]+df.ix[2]+df.ix[3]
    plt.bar(x,df.ix[4],color='g',label="5",bottom=bottom,align='center')
    bottom = df.ix[0]+df.ix[1]+df.ix[2]+df.ix[3]+df.ix[4]
    plt.bar(x,df.ix[5],color='c',label="6",bottom=bottom,align='center')
    bottom = df.ix[0]+df.ix[1]+df.ix[2]+df.ix[3]+df.ix[4]+df.ix[5]
    plt.bar(x,df.ix[6],color='k',label="7",bottom=bottom,align='center')
    bottom = df.ix[0]+df.ix[1]+df.ix[2]+df.ix[3]+df.ix[4]+df.ix[5]+df.ix[6]
    plt.bar(x,df.ix[7],color='r',label="8",bottom=bottom,align='center')

    plt.xticks(x,x_labels)
    plt.xlabel(u"生成域名数量")
    plt.ylabel(u"不同长度域名所占比例(%)")
    plt.legend(prop={'size': 10})
    plt.tight_layout()
    plt.show()

def draw2():
    """
    绘制整体验证成功率
    :return:
    """
    plt.subplot(121)
    x_labels = ['1K','10K','100K','200K','500K','1000K']
    # plt.yticks(np.arange(0,110,10))
    # plt.yticks(np.arange(100))
    plt.ylim(50,100)
    y = [100.0,100.0,99.07,96.73,88.35,77.86]
    x = range(len(x_labels))
    # plt.bar(x,y,align='center')
    plt.plot(x,y)
    plt.xticks(x,x_labels)
    plt.xlabel(u"生成域名数量")
    plt.ylabel(u"准确率(%)")

    plt.subplot(122)

    legend_labels = ['1K','10K','100K','200K','500K','1000K']
    source_data = np.array([[36,718,158,0,0,0,0],
                    [36,1070,6385,1489,0,0,0],
                    [36,1296,18894,58542,12306,2,0],
                    [36,1296,23080,103083,53688,455,0],
                    [36,1296,28887,180850,226485,16420,0],
                    [36,1296,33595,252200,515163,104164,239]],dtype=np.float64
    )

    verify_data = np.array([[36,718,158,0,0,0,0],
                    [36,1070,6385,1489,0,0,0],
                    [36,1296,18894,57986,12021,2,0],
                    [36,1296,23080,101008,49893,387,0],
                    [36,1296,28887,174083,184144,12658,0],
                    [36,1296,33595,239691,363735,67541,80]],dtype=np.float64

    )
    test = verify_data/source_data
    where = np.isnan(test)
    test[where]=0
    # test[test]=0
    # test[test=='nan']=0
    # print np.isnan(test)
    bar_width = 0.3
    # x = range(1,8)
    x=np.arange(6)
    # plt.bar(x,test[0],bar_width,color='b',label='1K')
    # plt.bar(x+bar_width,test[1],bar_width,color='r',label="10K")
    # plt.bar(x+bar_width,test[1],bar_width,color='r',label="10K")
    # plt.bar(x+bar_width,test[1],bar_width,color='r',label="10K")
    # plt.bar(x+bar_width,test[1],bar_width,color='r',label="10K")
    # plt.bar(x+bar_width,test[1],bar_width,color='r',label="10K")
    # plt.plot(x,test[0])
    # plt.plot(x,test[1])
    # plt.plot(x,test[2])
    plt.plot(x,test[3][:6],'b.-',label="20K")
    plt.plot(x,test[4][:6],'c^-',label="50K")
    plt.plot(x,test[5][:6],'y>-',label="100K")
    # plt.plot(x,test[1])
    plt.xticks(x,['1','2','3','4','5','6'])
    # plt.xticks(x+0.9,['1','2','3','4','5','6','7'])
    # plt.bar(x,test[0],bar_width,color='r',align='center',label="1K")
    # plt.bar(x+bar_width,test[1],bar_width,color='m',align='center',label="10K")
    # plt.bar(x+2*bar_width,test[2],bar_width,color='y',align='center',label="100K")
    # plt.bar(x+3*bar_width,test[3],bar_width,color='k',align='center',label="200K")
    # plt.bar(x+4*bar_width,test[4],bar_width,color='c',align='center',label="500K")
    # plt.bar(x+5*bar_width,test[5],bar_width,color='b',align='center',label="1000K")
    plt.legend(prop={'size': 10})
    plt.xlabel(u"域名长度")
    plt.ylabel(u"准确率(%)")
    plt.show()


def main():
    draw2()

if __name__ == '__main__':
    main()

