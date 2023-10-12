-- Active: 1696997922748@@127.0.0.1@3306
-- SQLBook: Code
CREATE DATABASE IF NOT EXISTS taqueria_db;
USE taqueria_db;

CREATE TABLE IF NOT EXISTS products(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS type_order (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO type_order (name) VALUES
    ('domicilio'),
    ('comenzal');

CREATE TABLE IF NOT EXISTS status_order (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS tables(
   id INT NOT NULL,
   table_number INT NOT NULL
);

INSERT INTO status_order (name) VALUES
    ('pendiente'),
    ('cancelada'),
    ('pagada');

CREATE TABLE IF NOT EXISTS orders (
    id INT NOT NULL AUTO_INCREMENT,
    created_date DATETIME NOT NULL DEFAULT (NOW()),
    client_name VARCHAR(50) NOT NULL,
    adress VARCHAR(50),
    status_id INT NOT NULL DEFAULT (1),
    type_id INT NOT NULL,
    table_number INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (status_id) REFERENCES status_order(id),
    FOREIGN KEY (type_id) REFERENCES type_order(id),
    FOREIGN KEY (table_number) REFERENCES tables(id)
);

CREATE TABLE IF NOT EXISTS order_products (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY(order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    CHECK (quantity > 0)
);



