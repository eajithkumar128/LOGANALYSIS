'''
    Author: Ajithkumar
    Description: To analyse the logs from the web server and database
    and create stats
    This program include pyscopg2 module which is used to connect database
'''

import psycopg2 as db


def createDB():
    return db.connect(database="news")


def printData(data):
    for results in data:
        print("\t\t* {} -- {} VIEWS".format(results[0], results[1]))
    print()


def mostPopularArticle():
    conn = createDB()
    curs = conn.cursor()
    FetchQuery = """
        select ar.title,count(lo.path) as views from articles ar, log lo
               where substring(lo.path,10) = ar.slug
               group by ar.title
               order by views desc limit 5
    """
    curs.execute(FetchQuery)
    popularArticles = curs.fetchall()
    printData(popularArticles)
    conn.close()


def mostPopularAuthor():
    conn = createDB()
    curs = conn.cursor()
    FetchQuery = """
        select au.name, count(lo.path) as views from log lo
               join articles ar on substring(lo.path,10) = ar.slug
               join authors au on ar.author = au.id
               group by name
               order by views desc
    """
    curs.execute(FetchQuery)
    popularAuthors = curs.fetchall()
    printData(popularAuthors)
    conn.close()


def mostErroredDays():
    conn = createDB()
    curs = conn.cursor()
    FetchQuery = """
        select trim(to_char(a.loo::date,'Month'))||
                    to_char(a.loo::date,' DD,YYYY'),
               round(((a.count::decimal*100)/b.count::decimal),2)::text||'%'
                from
               errorrequest a, requestcount b where a.loo = b.loo and
               round(((a.count::decimal*100)/b.count::decimal),2) > 1
    """
    curs.execute(FetchQuery)
    ErrorPercentage = curs.fetchall()
    printData(ErrorPercentage)
    conn.close()


if __name__ == '__main__':
    print("\t***************************************************************")
    print("\t*************************LOGS ANALYSIS*************************")
    print("\t***************************************************************")
    print()
    print("\tMOST POPULAR ARTICLES:")
    mostPopularArticle()
    print("\tMOST POPULAR ARTIST:")
    mostPopularAuthor()
    print("\tREQUEST ERRORS MORE THAN A PERCENTAGE:")
    mostErroredDays()
