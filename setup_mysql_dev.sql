-- script that prepares a MySQL server for the project
-- DB name hbnb_dev_db, user hbnb_dev in localhost, passwd hbnb_dev_pwd
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating user now
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
-- Giving passwd
IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
