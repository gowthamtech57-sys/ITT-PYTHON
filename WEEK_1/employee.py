employees = []

def add_employee():
    name = input("Name: ")
    emp_id = input("ID: ")
    rate = float(input("Hourly Rate: "))
    employees.append([name, emp_id, rate, 0, 0])
    print("Added.\n")

def calculate_pay():
    emp_id = input("ID to pay: ")
    hours = float(input("Hours worked: "))
    for emp in employees:
        if emp[1] == emp_id:
            emp[3] = hours
            emp[4] = emp[2] * hours
            print("Pay calculated: $", emp[4], "\n")
            return
    print("Not found.\n")

def display_payroll():
    print("\nID  Name        Hours  Rate  Pay")
    for emp in employees:
        print(emp[1], emp[0], emp[3], emp[2], emp[4])
    print()

def main():
    while True:
        print("1.Add 2.Pay 3.Show 4.Exit")
        choice = input("Choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            calculate_pay()
        elif choice == '3':
            display_payroll()
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("Try again.\n")

if __name__ == "__main__":
    main()