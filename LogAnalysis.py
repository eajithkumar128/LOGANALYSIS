'''
    Author: Ajithkumar
    Description: To analyse the logs from the web server and database and create stats
    This program include pyscopg2 module which is used to connect database
'''

import psycopg2 as db


def createDB():
    return db.connect(database="news")


def mostPopularArticle():
    conn = createDB()
    print(conn);
    conn.close();

if __name__ == '__main__':

    mostPopularArticle()
