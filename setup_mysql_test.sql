
-- script that prepares a MySQL server for the project
-- DB name hbnb_test_db, user hbnb_test in localhost, passwd hbnb_test_pwd
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creating user now
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Granting privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';