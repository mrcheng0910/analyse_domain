#!/usr/bin/python
# encoding:utf-8

"""
整合里alexa和dmoz的数据
"""

import tldextract
from pandas import DataFrame

# ext = tldextract.extract('http://forums.bbc.co.uk')
from data_base1 import MySQL1
from data_base import MySQL


def tuple_to_list(urls):
    """
    to format the type of tuple to list
    """
    urlts = []
    no_fetch_extract = tldextract.TLDExtract(suffix_list_urls=None)
    for url in urls:
        domain = no_fetch_extract(url[0]).domain
        tld = no_fetch_extract(url[0]).suffix
        urlts.append(str((domain+'.'+tld)).strip())
    # print len(urlts)
    return list(set(urlts))


def fetch_domains():
    """
    To fetch urls from the database, and return urls
    """
    db1 = MySQL1()
    sql = 'SELECT url FROM benign_urls'
    db1.query(sql)
    urls1 = db1.fetch_all_rows()
    db2 = MySQL()
    sql = 'SELECT domain FROM domain_white_list'
    db2.query(sql)
    urls2 = db2.fetch_all_rows()
    db1.close()
    db2.close()

    urls1 = tuple_to_list(urls1)
    urls2 = tuple_to_list(urls2)
    urls = urls1+urls2
    print len(urls)
    urls = list(set(urls))
    print len(urls)
    return urls


def extract_domains(source_domains):
    """
    插入新的域名到数据库中
    :param domains:
    :return:
    """
    no_fetch_extract = tldextract.TLDExtract(suffix_list_urls=None)

    domain_set = []
    # db = MySQL()
    for src_domain in source_domains:
        # print no_fetch_extract(src_domain)
        domain = {}
        try:

            domain['domain']=no_fetch_extract(src_domain).domain
            domain['tld'] = no_fetch_extract(src_domain).suffix
            domain['tld_token_count'] = len(domain['tld'].split('.'))
            domain['domain_length'] = len(domain['domain'])
            domain['character'] = character_frequencies(domain['domain'])
            domain['digit'] = digit_frequencies(domain['domain'])
            domain_set.append(domain)
        except:
            continue

    # 列表中字典去重的方法
    # f = lambda x,y:x if y in x else x + [y]
    # domain_set = reduce(f, [[], ] + domain_set)
    return domain_set

def insert_domains(domain_set):
    """
    更新数据库中词汇特征
    :param url_feature:
    :return:
    """
    db = MySQL()
    for domain in domain_set:
        sql = 'Insert into domain_features(domain,tld,tld_token_count,domain_length,domain_characters,domain_digit)VALUES ("%s","%s","%s","%s","%s","%s")' \
              %(domain['domain'],domain['tld'],domain['tld_token_count'],domain['domain_length'],domain['character'],domain['digit'])

        db.insert_no_commit(sql)
    db.commit()
    db.close()


def character_frequencies(domain):
    """
    计算域名中各个字符所占比例
    :param domain: 域名
    :return: 字符比例列表
    """
    total_length = len(domain)
    char_freq = []
    char_freq.extend([0] * 26)  # init 0
    special_char_count = 0

    for char in domain:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:  # To find occurrences of [a-z]
            char_freq[ascii_value - 97] += 1
        elif 65 <= ascii_value <= 90:  # To find occurrences of [A-Z]
            char_freq[ascii_value - 65] += 1
        elif char in "!@#$%^&*()-_=+{}[]|\':;><,?":  # To find occurrences of special characters
            special_char_count += 1
    char_freq.insert(0, special_char_count)
    for i in range(0, len(char_freq)):
        char_freq[i] = char_freq[i] * 100 / total_length
    return char_freq


def digit_frequencies(domain):
    """
    计算domain中含有各个数字的比例
    :param domain: 域名
    :return: 各个数字所占比例
    """
    total_length = len(domain)
    digit_freq = []
    digit_freq.extend([0] * 10)  # init 0

    for sp_dm in domain:
        ascii_value = ord(sp_dm)
        if 48 <= ascii_value <= 57:
            digit_freq[ascii_value-48] += 1
    for i in range(0, len(digit_freq)):
        digit_freq[i] = digit_freq[i] * 100 / total_length
    return digit_freq



def main():
    """
    主函数
    :return:
    """
    # results = []
    domains = fetch_domains()
    insert_domains(extract_domains(domains))

if __name__ == '__main__':
    # analysis_url('http://wwW.baid-u.com/baid')

    main()