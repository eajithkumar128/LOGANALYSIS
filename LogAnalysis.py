'''
    Author: Ajithkumar
    Description: To analyse the logs from the web server and database and create stats
    This program include pyscopg2 module which is used to connect database
'''

import psycopg2 as db



if __name__ == '__main__':

    conn = db.connect(database="news")
