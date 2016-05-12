#!/usr/bin/python
# encoding:utf-8

"""
整合里alexa和dmoz的数据
"""

DBCONFIG1 = {'host':'172.26.253.3',
                'port': 3306,
                'user':'root',
                'passwd':'platform',
                'db':'analyse_domain',
                'charset':'utf8'}

DBCONFIG2 = {'host':'172.26.253.3',
                'port': 3306,
                'user':'root',
                'passwd':'platform',
                'db':'DomainWhois',
                'charset':'utf8'}


from data_base import MySQL


def fetch_domains():
    """
    To fetch urls from the database, and return urls
    """
    tld ={}
    db1 = MySQL(DBCONFIG1)
    db2 = MySQL(DBCONFIG2)
    sql = 'SELECT SUBSTRING_INDEX(tld,".",-1) as a,count(*) FROM domain_features GROUP BY a'
    db1.query(sql)
    tld_count = db1.fetch_all_rows()
    for i in tld_count:
        print i
        if len(i[0])==0:
            continue
        sql = 'SELECT type FROM tld_details WHERE tld="%s"' % ('.'+i[0])
        db2.query(sql)
        urls2 = db2.fetch_all_rows()
        try:
            if urls2[0][0] in tld.keys():
                tld[urls2[0][0]] += i[1]
            else:
                tld[urls2[0][0]] = i[1]
        except:
            continue
    print tld
    db1.close()
    db2.close()







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