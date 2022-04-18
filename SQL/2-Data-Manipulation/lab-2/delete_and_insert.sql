/* manipulating auto increment values in a table*/
USE packt_online_shop;
DELETE FROM department WHERE departmentNo>2;

/*insert values*/
INSERT INTO department(departmentname,departmentLoc) 
 VALUES('Sales','LV');