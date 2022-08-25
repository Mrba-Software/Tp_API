DROP DATABASE IF EXISTS plants;
CREATE DATABASE plants;
DROP USER IF EXISTS student;
CREATE USER student WITH ENCRYPTED PASSWORD 'student';
GRANT ALL PRIVILEGES ON DATABASE plants TO student;
ALTER USER student CREATEDB;
ALTER USER student WITH SUPERUSER;