/* create new tabel*/
USE employee;
CREATE TABLE department (
 departmentNo INT PRIMARY KEY,
 departmentName VARCHAR(20) NOT NULL,
 departmentLoc VARCHAR(50) NOT NULL
);