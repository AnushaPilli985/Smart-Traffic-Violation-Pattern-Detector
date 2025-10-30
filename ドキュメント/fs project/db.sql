CREATE DATABASE attendance_db;

USE attendance_db;

CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT INTO teachers (username, password) VALUES ('admin', 'admin123');

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    status VARCHAR(10),
    date DATE,
    time TIME
);
