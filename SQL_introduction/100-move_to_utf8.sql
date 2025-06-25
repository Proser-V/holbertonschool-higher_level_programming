-- A script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

DROP DATABASE IF EXISTS btn_0c_0;
CREATE DATABASE btn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
DROP TABLE IF EXISTS first_table;
CREATE TABLE first_table(
    id INT DEFAULT NULL,
    name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    score INT DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
