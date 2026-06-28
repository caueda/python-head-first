create database vsearchlogDB;

CREATE USER 'vsearch'@'%' IDENTIFIED BY 'welcome1';

GRANT ALL PRIVILEGES ON vsearchlogDB.* TO 'vsearch'@'%';

FLUSH PRIVILEGES;

create table log (
id int auto_increment primary key,
ts timestamp default current_timestamp,
phrase varchar(128) not null,
letters varchar(32) not null,
ip varchar(16) not null,
browser_string varchar(256) not null,
results varchar(64) not null
);

show tables