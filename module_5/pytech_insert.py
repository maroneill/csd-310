import pymongo

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.ftrlqqg.mongodb.net/?retryWrites=true&w=majority")

db = client["pytech"]

collection = db["students"]

matt = {
    "first_name": "Matt", "last_name": "Lastly", "student_id": 1007
}
collection.insert_one(matt)

joe = {
    "first_name": "Joe", "last_name": "Langly", "student_id": 1008
}
collection.insert_one(joe)

susan = {
    "first_name": "Susan", "last_name": "Lamby", "student_id": 1009
}
collection.insert_one(susan)

matt_student_id = collection.insert_one(matt).inserted_id
joe_student_id = collection.insert_one(joe).inserted_id
susan_student_id = collection.insert_one(susan).inserted_id

print(matt_student_id)
print(joe_student_id)
print(susan_student_id)
