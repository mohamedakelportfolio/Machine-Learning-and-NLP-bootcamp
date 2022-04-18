-- create new table
-- student table
USE studentdemo;
CREATE TABLE student (
    Student_ID CHAR(4),
    StudentName VARCHAR(30),
    grade CHAR(1),
    age INT,
    course VARCHAR(50),
    PRIMARY KEY(Student_ID)
);