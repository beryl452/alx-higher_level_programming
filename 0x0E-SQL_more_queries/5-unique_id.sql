-- Creates the table unique_id

CREATE TABLE IF NOT EXISTS unique_id(
id INTEGER DEFAULT 1,
name VARCHAR(256),
UNIQUE(id));

