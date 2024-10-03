import mysql.connector

# Establishing connection to MySQL database
db = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="Shivam@2003", 
    database="employee_management"
)

cursor = db.cursor()

def add_employee():
    name = input("Enter Name: ")
    Email = input("Enter email: ")
    department = input("Enter Department: ")
    position = input("Enter position: ")
    salary = float(input("Enter Salary: "))
    mobile_no = input("Enter mobile no.")

    query = "INSERT INTO employees (name, Email, department, position, salary, mobile_no) VALUES (%s, %s, %s, %s, %s,%s)"
    values = (name, Email, department, position, salary, mobile_no)
    cursor.execute(query, values)
    db.commit()
    print("Employee added successfully!\n")

    
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    print("1. Update Name")
    print("2. Update Email")
    print("3. Update Department")
    print("4. Update positon")
    print("5. Update Salary")
    print("6. Update mobile_no")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        new_value = input("Enter new Name: ")
        cursor.execute("UPDATE employees SET first_name = %s WHERE emp_id = %s", (new_value, emp_id))
    elif choice == 2:
        new_value = float(input("Enter new Email: "))
        cursor.execute("UPDATE employees SET Email = %s WHERE emp_id = %s", (new_value, emp_id))
    elif choice == 3:
        new_value = input("Enter new Department: ")
        cursor.execute("UPDATE employees SET department = %s WHERE emp_id = %s", (new_value, emp_id))
    elif choice == 4:
        new_value = float(input("Enter new position: "))
        cursor.execute("UPDATE employees SET positon = %s WHERE emp_id = %s", (new_value, emp_id))
    elif choice == 5:
        new_value = float(input("Enter new Salary: "))
        cursor.execute("UPDATE employees SET salary = %s WHERE emp_id = %s", (new_value, emp_id))
    elif choice == 6:
        new_value = float(input("Enter new Mobile number: "))
        cursor.execute("UPDATE employees SET mobile_no = %s WHERE emp_id = %s", (new_value, emp_id))
    db.commit()
    print("Employee updated successfully!\n")

def view_employee():
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    
    print("Employee List:")
    for row in result:
        print("ID:", row[0], "Name:", row[1], "Email:", row[2], "Department:", row[3], "Position:", row[4], "Salary:", row[5], "Mobile no.", row[6])
    print()

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
    db.commit()
    print("Employee deleted successfully!\n")

while True:
    print("Employee Management System")
    print("1. Add Employee")
    print("2. update Employees")
    print("3. view Employee")
    print("4. Delete Employee")
    print("5. Exit")
    
    # Input validation: Loop until a valid choice is entered
    
    try:
        choice = int(input("Enter your choice: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue  # Ask for input again if invalid
    

    if choice == 1:
        add_employee()
    elif choice == 2:
        update_employee()
    elif choice == 3:
        view_employee()
    elif choice == 4:
        delete_employee()
    elif choice == 5:
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please choose a valid option between 1 and 5.\n")
    
