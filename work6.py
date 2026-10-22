students = [
    {
        "ID":101,
        "Name":"Alice Johnson",
        "Department":"Computer Science",
        "Age":20,
        "Grade":"A",
        "Courses":"Python, Web Dev",
    },
    {
        "ID":102,
        "Name":"Bob Smith",
        "Department":"Mathematics",
        "Age":21,
        "Grade":"B+",
        "Courses":"Calculus, Linear Algebra",
    },
    {
        "ID":103,
        "Name":"Charlie Brown",
        "Department":"Physics",
        "Age":19,
        "Grade":"A-",
        "Courses":"Mechanics, Optics",
    },
    {
        "ID":104,
        "Name":"Diana Prince",
        "Department":"Computer Science",
        "Age":22,
        "Grade":"A",
        "Courses":"Data Structures, DBMS",
    },
    {  
        "ID":105,
        "Name":"Evan Davis",
        "Department":"chemistry",
        "Age":20,
        "Grade":"B",
        "Courses":"organic Chemistry, Lab",
    },
    {
        "ID":106,
        "Name":"Fiona Garcia",
        "Department":"English",
        "Age":21,
        "Grade":"A-",
        "Courses":"Literature, Communication",
    },
    {
        "ID":107,
        "Name":"george Harris",
        "Department":"Mechanical Eng.",
        "Age":22,
        "Grade":"B+",
        "Courses":"Thermodynamics, CAD",
    },

    {
        "ID":108,
        "Name":"Hannah Lee",
        "Department":"Computer Science",
        "Age":19,
        "Grade":"A",
        "Courses":"Algorithms, web Dev",
    },
]

print("Student Details")
print("-" * 101)
print(f"| {"ID": ^5} | {"Name": ^15} | {"Department": ^20} | {"Age": ^5} | {"Grade": ^7} | {"Courses": ^30} |")
print("-" * 101)
for s in students:
    print(f"| {s.get('ID'): <5} | {s.get('Name'): <15} | {s.get('Department'): <20} | {s.get('Age'): ^5} | {s.get('Grade'): <7} | {s.get('Courses'): <30} |")
print("-" * 101)
print("Total students:", len(students))