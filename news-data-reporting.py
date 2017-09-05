#!/usr/bin/env python3
import psycopg2


def select(select_query):
    db = psycopg2.connect(database='news')
    cursor = db.cursor()
    cursor.execute(select_query)
    rows = cursor.fetchall()
    db.close()
    return rows


def print_rows(rows):
    if rows == []:
        print('No results found')
    else:
        for row in rows:
            row_string = None
            for value in row:
                if value == row[0]:
                    row_string = str(value)
                else:
                    row_string = row_string + ' -- ' + str(value)
            print(row_string)
    print('')


def report_most_popular_articles():
    articles_query = '''
    SELECT articles.title, CONCAT(COUNT(*),' views') AS views
    FROM articles, log
    WHERE log.path = CONCAT('/article/',articles.slug)
    GROUP BY articles.title
    ORDER BY count(*) DESC LIMIT 3;'''
    rows = select(articles_query)
    print("The three most popular articles of all time:")
    print_rows(rows)


def report_most_popular_authors():
    authors_query = '''
    SELECT authors.name, CONCAT(author_views.article_views,' views') AS views
    FROM authors, (
      SELECT articles.author, count(*) AS article_views
      FROM articles, log
      WHERE log.path = CONCAT('/article/',articles.slug)
      GROUP BY articles.author
      ) AS author_views
    WHERE authors.id = author_views.author
    GROUP BY authors.name, views, author_views.article_views
    ORDER BY author_views.article_views DESC;'''
    rows = select(authors_query)
    print("The most popular authors of all time:")
    print_rows(rows)


def report_high_error_days():
    high_error_days_query = '''
    SELECT TO_CHAR(date,'FMMonth FMDD, YYYY') AS date,
      CONCAT(ROUND(fail_percentage*100,1),'% errors') AS errors
    FROM daily_fail_percentage
    WHERE fail_percentage > .01
    ORDER BY daily_fail_percentage.date;'''
    rows = select(high_error_days_query)
    print("Days where over 1% of requests failed:")
    print_rows(rows)


report_most_popular_articles()
report_most_popular_authors()
report_high_error_days()
