# LOG ANALYSIS

Log Analysis is a command line reporting tool which create report of most viewed articles, authors and error request report of a webpage. Program fetch data from the postgresql database. pyscopg2 module is used to connect and query the database.

## How TO RUN THE PROGRAM

To run the program enter the following command:

>`python3 LogAnalysis.py`

## SUPPORTED VERISON

* PYTHON3, PYTHON2

## VIEWS USED

Following views are created in the database to fetch the results.

```
create view requestcount as SELECT "substring"(to_char(log."time", 'YYYY-MM-DD'::text), 1, 10) AS loo,
    count(log.status) AS count
    FROM log
    GROUP BY ("substring"(to_char(log."time", 'YYYY-MM-DD'::text), 1, 10))
    ORDER BY ("substring"(to_char(log."time", 'YYYY-MM-DD'::text), 1, 10));
```

```
create view errorrequest as SELECT "substring"(to_char(log."time", 'YYYY-MM-DD'::text), 1, 10) AS loo,
    count(log.status) AS count
    FROM log
    WHERE log.status <> '200 OK'::text
    GROUP BY ("substring"(to_char(log."time", 'YYYY-MM-DD'::text), 1, 10))
    ORDER BY ("substring"(to_char(log."time", 'YYYY-MM-DD'::text), 1, 10));
```
