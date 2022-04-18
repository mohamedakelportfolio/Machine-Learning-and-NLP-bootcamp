/* drop and then create table with specifying default values*/
USE employee;
DROP TABLE IF EXISTS department;
CREATE TABLE department (
 departmentNo INT PRIMARY KEY AUTO_INCREMENT,
 departmentName VARCHAR(20) NOT NULL,
 departmentLoc VARCHAR(50) DEFAULT 'NJ',
 departmentEstDate DATETIME DEFAULT NOW()
);
