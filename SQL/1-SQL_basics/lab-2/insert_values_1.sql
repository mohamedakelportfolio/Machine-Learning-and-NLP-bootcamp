-- insert multiple records into customers
USE packt_online_shop;
INSERT INTO Customers (
        FirstName,
        MiddleName,
        LastName,
        HomeAddress,
        Email,
        Phone,
        Notes
    )
VALUES(
        'Joe',
        'Greg',
        'Smith',
        '2356 Elm St.',
        'joesmith@sfghwert.com',
        '(310) 
555-1212',
        'Always gets products home delivered'
    ),
    (
        'Grace',
        'Murray',
        'Hopper',
        '123 Compilation Street',
        'gmhopper@ftyuw46.com',
        '(818) 555-3678',
        'Compiler pioneer'
    ),
    (
        'Ada',
        NULL,
        'Lovelace',
        '22 Algorithm Way',
        'adalovelace@fgjw54af.gov',
        '(717) 
555-3457',
        'First software engineer'
    ),
    (
        'Joseph',
        'Force',
        'Crater',
        '1313 Mockingbird Lane',
        'judgecrater@ev56gfwrty.com',
        '(212) 555-5678',
        'Works everyday'
    ),
    (
        'Jacqueline',
        'Jackie',
        'Cochran',
        '1701 Flightspeed Avenue',
        'jackiecochrane@
jryuwp8qe4w.gov',
        '(717) 555-3457',
        'Researcher'
    ),
    (
        NULL,
        'Paul',
        'Jones',
        '126 Bonhomme Richard Ave.',
        'jpjones@bonhommerichard.edu',
        '(216) 555-6232',
        'Admiral'
    );