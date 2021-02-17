CREATE TABLE Department(
	dept_no VARCHAR(3) NOT NULL,
	dept_name VARCHAR(255),
	dept_loc VARCHAR(255),
	PRIMARY KEY(dept_no)
)
INSERT INTO department (dept_no, dept_name, dept_loc) VALUES ('D01','IT', 'Banglore')
INSERT INTO department (dept_no, dept_name, dept_loc) VALUES ('D02','HR', 'Mumbai');
INSERT INTO department (dept_no, dept_name, dept_loc) VALUES ('D03','Sales & Marketing', 'Banglore');
INSERT INTO department (dept_no, dept_name, dept_loc) VALUES ('D04','Life Insurance', 'Mumbai');

SELECT * FROM department

INSERT INTO employee (emp_no, emp_fname, emp_lname, emp_age, emp_dept) VALUES (001,'Nitin','Bakshi',32,'D02');
INSERT INTO employee (emp_no, emp_fname, emp_lname, emp_age, emp_dept) VALUES (002,'Karan','Malhotra',28,'D03');
INSERT INTO employee (emp_no, emp_fname, emp_lname, emp_age, emp_dept) VALUES (003,'Mahesh','Patel',25,'D03');
INSERT INTO employee (emp_no, emp_fname, emp_lname, emp_age, emp_dept) VALUES (004,'Kalpesh','Mehra',29,'D01');
INSERT INTO employee (emp_no, emp_fname, emp_lname, emp_age, emp_dept) VALUES (005,'Nitin','Mundra',35,'D04');
INSERT INTO employee (emp_no, emp_fname, emp_lname, emp_age, emp_dept) VALUES (006,'Riddhi','Agarwal',26,'D02');
INSERT INTO employee (emp_no, emp_fname, emp_lname, emp_age, emp_dept) VALUES (007,'Sanjay','Patel',25,'D01');

SELECT * FROM employee




