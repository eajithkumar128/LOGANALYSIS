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
        print("* {} -- {} VIEWS".format(results[0],results[1]));


def mostPopularArticle():
    conn = createDB()
    curs = conn.cursor();
    FetchQuery = """
        select ar.title,count(lo.path) from articles ar, log lo
               where substring(lo.path,10) = ar.slug
               group by lo.path,ar.title
               order by count(lo.path) desc limit 5
    """
    curs.execute(FetchQuery);
    popularArticles = curs.fetchall();
    printData(popularArticles)
    conn.close()

if __name__ == '__main__':
    print("******************************************************************")
    print("*************************LOGS ANALYSIS****************************")
    print("******************************************************************")
    print();
    print("MOST POPULAR ARTICLES:")
    mostPopularArticle()
    print("\nMOST POPULAR ARTIST");
