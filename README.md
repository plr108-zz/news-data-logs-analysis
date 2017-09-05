# Udacity Full Stack Web Developer Nanodegree

## Logs Analysis Project
By Patrick Roche | [github.com/plr108](https://github.com/plr108) | [patrick.l.roche@gmail.com](mailto:patrick.l.roche@gmail.com)

### Project Overview
This repository contains my submission for the Logs Analysis project of the
[Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
The project uses psycopg2 to run queries against a mock PostgreSQL database
for a fictional news website.  The queries provide answers to the following
questions about the database:
1. What are the three most popular articles of all time on the news site?
2. Who are the most popular article authors?
3. On what days did over one percent of page requests result in errors?

### Installation Prerequisites
The following software is required to run this project.  
See the provided links for download and install instructions
* Python 3.6.2: https://www.python.org/downloads/
* Vagrant: https://www.vagrantup.com/
* VirtualBox: https://www.virtualbox.org/wiki/Downloads

Download [Udacity's Vagrant Configuration File](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
for this project and unzip the contents to the desired location.

### Installing the Repository
This repository must be cloned to a subdirectory of the vagrant install folder, i.e.,
in the /FSND-Virtual-Machine/vagrant directory created by unizipping the Vagrant configuration file.

### Starting the Virtual Machine
In your console run the following commands:
1. vagrant up
2. vagrant ssh
3. cd /vagrant

### Installing the Database
The news database also must be installed in the same directory as this repository.
A zip file containing the database is available [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  
Unzip the database (newsdata.sql file).  Navigate to the folder containing the
database (and this repository) and run `psql -d news -f newsdata.sql` to run
PostgreSQL and initialize the database.

### Required Database Views
Several database views must be created prior to running the reporting tool.
Enter the following SQL statements in PostgreSQL to create the required views:

`CREATE VIEW responses AS
SELECT status, COUNT(*) AS responses, DATE_TRUNC('day', time) AS date
FROM log
GROUP BY status, date;`

`CREATE VIEW daily_requests AS
SELECT SUM(responses) AS requests, date
FROM responses
GROUP BY date;`

`CREATE VIEW daily_fails AS
SELECT responses AS fails, date
FROM responses
WHERE status NOT LIKE '200%';`

`CREATE VIEW daily_fail_percentage AS
SELECT (fails / requests) AS fail_percentage, daily_requests.date
FROM daily_fails, daily_requests
WHERE daily_fails.date = daily_requests.date
GROUP BY fails, requests, daily_requests.date;`

Running the Reporting Tool
After creating the views, exit the database using the command `\q`.  
Run the command `python3 news-data-reporting.py`.  
The results printed to the console should match the contents of output.txt
in this repository.
