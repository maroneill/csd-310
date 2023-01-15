import pymongo

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.ftrlqqg.mongodb.net/?retryWrites=true&w=majority")

db = client["pytech"]

students = db["students"]

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

found_students = students.find()

for student in found_students:
    print(student)
