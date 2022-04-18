/* reset auto increment then insert new values and retrieve them for the explanation*/
ALTER TABLE department AUTO_INCREMENT = 3;
-- DATA INSERT
INSERT INTO department(departmentname,departmentLoc) 
 VALUES('Sales','LV');
SELECT * FROM department;