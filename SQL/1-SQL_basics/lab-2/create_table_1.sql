-- create new table
-- customers table
USE packt_online_shop;
CREATE TABLE customers(
    FirstName VARCHAR(50),
    MiddleName VARCHAR(50),
    LastName VARCHAR(50),
    HomeAddress VARCHAR(250),
    Email VARCHAR(200),
    Phone VARCHAR(50),
    Notes VARCHAR(250)
);