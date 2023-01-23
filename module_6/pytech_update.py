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

students.update_one({"student_id": 1007}, {"$set": {"last_name": "UPDATED"}})

print("\n")
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
student = students.find_one({"student_id": 1007})
print("Student ID: ", student["student_id"])
print("First Name: ", student["first_name"])
print("Last Name: ", student["last_name"])
print("\n")
