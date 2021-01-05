CREATE USER djuser WITH PASSWORD 'djuser' CREATEDB;
CREATE DATABASE marketplace
    WITH
    OWNER = djuser
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = 10;