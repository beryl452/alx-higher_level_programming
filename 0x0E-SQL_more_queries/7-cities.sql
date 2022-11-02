-- Creates the database hbtn_0d_usa and the table cities

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE cities(
id INTEGER UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INTEGER NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (id) REFERENCES hbtn_0d_usa.states(id)
);

