# LOG ANALYSIS

Log Analysis is a command line reporting tool which create report of most viewed articles, authors and error request report of a webpage. Program fetch data from the postgresql database. pyscopg2 module is used to connect and query the database.

## Setting up the environment

To run the program the following softwares needs to be installed in the system.

* Virtual Machine
* Vagrant

### Install Virtual Box:

Virtual Box is the software that acts as a virtual machine.  You can download it from [virtualbox.org](LINK), here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

### Install Vagrant:

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

**Windows users**: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

### Download VM Configuration:

You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

You will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

### Starting the Virtual Machine:

From your terminal, inside the vagrant subdirectory, run the command **vagrant up**. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run **vagrant ssh** to log in to your newly installed Linux VM!

## Running the Database:

The PostgreSQL database server will automatically be started inside the VM. You can use the **psql** command-line tool to access it and run SQL statements:

## Data to run the program:

Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).Unzip the folder after downloading it.The file inside is called newsdata.sql. Put this file into the _vagrant_ directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database.

To load the data, cd into the vagrant directory and use the command **psql -d news -f newsdata.sql**.

Here's what this command does:

psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### Create Views in the Database

Following views are created in the database to fetch the results.

To create the views login to database using **psql** command-line tool. Connect to the **news** database with command **\c news**.
Run the below mentioned queries. This query will create views in the database for fetching the results.

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

## How TO RUN THE PROGRAM

To run the program enter the following command:

>`python3 LogAnalysis.py`

## SUPPORTED VERISON

* PYTHON3, PYTHON2
