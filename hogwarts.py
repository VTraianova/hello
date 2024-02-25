students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


#students = {
#    "Hermione": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin"
#}

#for student in (students):
#    print(student, students[student], sep=", ")

#print(students["Hermione"])

#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#for i in range(len(students)):
#    print(i + 1, students[i])

#for students in students:
#    print(students)

#print (students[0])
    
# name = "Harry"
# for character in name:
#    print(character)    