#!/usr/bin/python
# encoding:utf-8

"""
遍历生成域名，并存入数据库
"""

DBCONFIG1 = {'host':'172.26.253.3',
                'port': 3306,
                'user':'root',
                'passwd':'platform',
                'db':'analyse_domain',
                'charset':'utf8'}


from data_base import MySQL


def fetch_domains():
    """
    To fetch urls from the database, and return urls
    """
    domain_char = []
    domains = []
    for i in range(97,123):
        domain_char.append(chr(i))
    for i in range(10):
        domain_char.append(str(i))

    domain_char.append('-')
    domain_char.append('')
    for first in domain_char:
        for second in domain_char:
            for third in domain_char:
                # domain = ""
                domain = first+second+third

                domain = domain.strip()
                if len(domain) == 0:
                    continue
                if domain[0] == '-' or domain[len(domain)-1] == '-':
                    # print domain
                    continue

                domains.append(domain)
    domains = list(set(domains))
    print len(domains)
    # db1 = MySQL(DBCONFIG1)
    # for i in domains:
    #     sql = 'insert into cn_domain (domain) VALUES ("%s")' % (str(i)+'.cn')
    #     print sql
        # db1.insert_no_commit(sql)
    #
    # db1.commit()
    # db1.query(sql)
    # db1.close()







def main():
    """
    主函数
    :return:
    """
    # results = []
    domains = fetch_domains()
    # insert_domains(extract_domains(domains))

if __name__ == '__main__':
    # analysis_url('http://wwW.baid-u.com/baid')

    main()