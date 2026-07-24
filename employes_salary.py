# Employee Salary Management System

employees = [
    {"id": "EMP001", "name": "Rahul naik ", "department": "IT", "designation": "Software Engineer", "salary": 45000},
    {"id": "EMP002", "name": "Priya Reddy", "department": "HR", "designation": "HR Executive", "salary": 38000},
    {"id": "EMP003", "name": "Arjun Kumar", "department": "Finance", "designation": "Accountant", "salary": 42000},
    {"id": "EMP004", "name": "Sneha Patel", "department": "Sales", "designation": "Sales Executive", "salary": 36000},
    {"id": "EMP005", "name": "Vikram Singh", "department": "IT", "designation": "Senior Developer", "salary": 68000},
    {"id": "EMP006", "name": "Anjali Verma", "department": "Marketing", "designation": "Marketing Executive", "salary": 40000},
    {"id": "EMP007", "name": "Kiran Rao", "department": "Operations", "designation": "Operations Manager", "salary": 75000},
    {"id": "EMP008", "name": "Meena Nair", "department": "Customer Support", "designation": "Support Executive", "salary": 32000},
    {"id": "EMP009", "name": "Rohit Gupta", "department": "IT", "designation": "System Administrator", "salary": 50000},
    {"id": "EMP010", "name": "Pooja Das", "department": "Finance", "designation": "Finance Manager", "salary": 82000}
]

print("========== Employee Salary Details ==========\n")

total_salary = 0

for emp in employees:
    print(f"Employee ID   : {emp['id']}")
    print(f"Name          : {emp['name']}")
    print(f"Department    : {emp['department']}")
    print(f"Designation   : {emp['designation']}")
    print(f"Salary        : ₹{emp['salary']:,}")
    print("-" * 40)
    total_salary += emp["salary"]

average_salary = total_salary / len(employees)

highest_paid = max(employees, key=lambda x: x["salary"])
lowest_paid = min(employees, key=lambda x: x["salary"])

print("\n========== Salary Summary ==========")
print(f"Total Employees : {len(employees)}")
print(f"Total Salary    : ₹{total_salary:,}")
print(f"Average Salary  : ₹{average_salary:,.2f}")
print(f"Highest Paid    : {highest_paid['name']} (₹{highest_paid['salary']:,})")
print(f"Lowest Paid     : {lowest_paid['name']} (₹{lowest_paid['salary']:,})")