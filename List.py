students=[
    {"name":"Anu","marks":[99, 98, 95]},
    {"name":"Mani","marks":[70, 88, 80]},
    {"name":"Meena","marks":[60, 75, 83]}
]
highest_total=0
topper=""
for student in students:
    total=0
    for mark in student["marks"]:
        total+=mark
    average = total/len(student["marks"])
    if average >= 90:
        grade="A"
    elif average >= 75:
        grade="B"
    else:
        grade="C" 
    print("Name:",student["name"])
    print("Total:",total)
    print("Average:",average)
    print("Grade:",grade)
    print("-----------")
    if total>highest_total:
        highest_total=total
        topper=student["name"]
print("Topper is:",topper)