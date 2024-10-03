use employee_management;
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2),
    mobile_no INT(20)
);

select * from employees;

DESCRIBE employees;
SELECT employee_id, name, position, salary, department FROM employees;