'''
    Author: Ajithkumar
    Description: To analyse the logs from the web server and database and create stats
    This program include pyscopg2 module which is used to connect database
'''

import psycopg2 as db


def createDB():
    return db.connect(database="news")


def printData(data):
    for results in data:
        print("\t\t* {} -- {} VIEWS".format(results[0],results[1]));
    print()


def mostPopularArticle():
    conn = createDB()
    curs = conn.cursor();
    FetchQuery = """
        select ar.title,count(lo.path) as views from articles ar, log lo
               where substring(lo.path,10) = ar.slug
               group by ar.title
               order by views desc limit 5
    """
    curs.execute(FetchQuery);
    popularArticles = curs.fetchall();
    printData(popularArticles)
    conn.close()

def mostPopularAuthor():
    conn = createDB()
    curs = conn.cursor();
    FetchQuery = """
        select au.name, count(lo.path) as views from log lo
               join articles ar on substring(lo.path,10) = ar.slug
               join authors au on ar.author = au.id
               group by name
               order by views desc
    """
    curs.execute(FetchQuery);
    popularAuthors = curs.fetchall()
    printData(popularAuthors);
    conn.close()

if __name__ == '__main__':
    print("\t******************************************************************")
    print("\t*************************LOGS ANALYSIS****************************")
    print("\t******************************************************************")
    print();
    print("\tMOST POPULAR ARTICLES:")
    mostPopularArticle()
    print("\tMOST POPULAR ARTIST:");
    mostPopularAuthor()
