create database vsearchlogDB;

CREATE USER 'vsearch'@'%' IDENTIFIED BY 'welcome1';

GRANT ALL PRIVILEGES ON vsearchlogDB.* TO 'vsearch'@'%';

FLUSH PRIVILEGES;