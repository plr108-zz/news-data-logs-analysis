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
    articles_query = '''select articles.title, concat(count(*),' views') as
    views from articles, log where log.path like concat('%',articles.slug,'%')
    group by articles.title order by count(*) desc limit 3;'''
    rows = select(articles_query)
    print("The three most popular articles of all time:")
    print_rows(rows)


def report_most_popular_authors():
    authors_query = '''select authors.name, concat(author_views.article_views,
    ' views') as views from authors, (select articles.author, count(*) as
    article_views from articles, log where log.path like
    concat('%',articles.slug,'%') group by articles.author) as author_views
    where authors.id = author_views.author group by authors.name, views,
    author_views.article_views order by author_views.article_views desc;'''
    rows = select(authors_query)
    print("The most popular authors of all time:")
    print_rows(rows)


def report_high_error_days():
    high_error_days_query = '''select to_char(date,'FMMonth FMDD, YYYY') as
    date, concat(round(fail_percentage*100,1),'% errors') as errors from
    daily_fail_percentage where fail_percentage > .01 order by
    daily_fail_percentage.date;'''
    rows = select(high_error_days_query)
    print("Days where over 1% of requests failed:")
    print_rows(rows)


report_most_popular_articles()
report_most_popular_authors()
report_high_error_days()
