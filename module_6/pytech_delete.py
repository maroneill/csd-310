import pymongo

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.ftrlqqg.mongodb.net/?retryWrites=true&w=majority")

db = client["pytech"]

students = db["students"]



print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students.find():
    print("Student ID: ", student["student_id"])
    print("First Name: ", student["first_name"])
    print("Last Name: ", student["last_name"])
    print("\n")

new_student = {
    "student_id": 1010,
    "first_name": "John",
    "last_name": "Newby"
}

students.insert_one(new_student)

print("-- INSERT STATEMENTS --")

print("Inserted student record into the students collection with document_ID", student["_id"] )


print("-- DISPLAYING STUDENT DOCUMENT 1010 --")

print("Student ID: ", student["student_id"])
print("First Name: ", student["first_name"])
print("Last Name: ", student["last_name"])

print("-- DELETE STATEMENTS --")

print("Deleted student record into the students collection with document_ID", student["_id"] )

students.delete_one(new_student)

