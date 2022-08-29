-- script that creates a table users

CREATE TABLE if not exists users (
    id INT NOTNULL AUTOINCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    UNIQUE (email)
);
