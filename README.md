# Udacity Full Stack Web Developer Nanodegree

## Logs Analysis Project
By Patrick Roche | [github.com/plr108](https://github.com/plr108) | [patrick.l.roche@gmail.com](mailto:patrick.l.roche@gmail.com)

### Project Overview
This repository contains my submission for the Logs Analysis project of the [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

### Installation Prerequisites
The following software is required to run this project.  See the provided links for download and install instructions
* Python 3.6.2: https://www.python.org/downloads/
* Vagrant: https://www.vagrantup.com/
* VirtualBox: https://www.virtualbox.org/wiki/Downloads
* The news database must be installed.  If you are reviewing my project I assume you have it; I could not find the database online and the project instructions indicated that the database was not to be included in this repository :)

### Install Instructions
After installing the software in the Installation Prerequisites section, clone this repository to your /vagrant directory.

### Running the Reporting Tool
In your console run the following commands:
1. vagrant up
2. vagrant ssh
3. cd /vagrant
Navigate to the subdirectory containing this repo and run the command `python3 news-data-reporting.py`.  The results listed in the output.txt file should be printed to the console.
