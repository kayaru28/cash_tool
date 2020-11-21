# login
mysql --user=root --password=mypass 

# DB = rps
CREATE DATABASE rps;

## table
create table rps.battle_history(
    time timestamp,
    id int,
    name varchar(10), 
    choice_id int,
    result varchar(10) 
);
alter table rps.battle_history add primary key (time,id); 


alter table rps.battle_history DROP PRIMARY KEY,add primary key (time,id); 


create table rps.id_choice(
    choice_id int,
    choice varchar(10)
);


# command
show tables from rps;
drop table rps.battle_history;
SELECT * FROM rps.battle_history;

# install

## mysql
yum localinstall http://dev.mysql.com/get/mysql57-community-release-el7-7.noarch.rpm 
cd /etc/yum.repos.d/
ls -l | grep mysql
yum info mysql-community-server
yum install -y mysql-community-server
mysqld --version

## mysqlclient
sudo yum install -y mysql-community-devel
yum install -y gcc

pip install mysqlclient

## option
pip show mysqlclient
export PATH=$PATH:/usr/local/lib64/python3.6/site-packages


## setup
pip install sqlalchemy






