# Udacity Full Stack Web Developer Nanodegree

## Logs Analysis Project
By Patrick Roche | [github.com/plr108](https://github.com/plr108) | [patrick.l.roche@gmail.com](mailto:patrick.l.roche@gmail.com)

### Project Overview
This repository contains my submission for the Logs Analysis project of the
[Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

### Installation Prerequisites
The following software is required to run this project.  
See the provided links for download and install instructions
* Python 3.6.2: https://www.python.org/downloads/
* Vagrant: https://www.vagrantup.com/
* VirtualBox: https://www.virtualbox.org/wiki/Downloads

### Installing the Repository and the News Database
This repository must be cloned to a subdirectory of the vagrant install folder.  
The news database also must be installed in the same directory as this repository.  
If you are reviewing my project I assume you have this database;
I could not find the database online and the project instructions indicated
that the database was not to be included in this repository :)

### Starting the Virtual Machine
In your console run the following commands:
1. vagrant up
2. vagrant ssh
3. cd /vagrant

### Required Database Views
Several database views must be created prior to running the reporting tool.
After starting the virtual machine, navigate to the folder containing this
repository (and the news database) and run `psql news` to access the database.
Enter the following commands to create the required views:

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
