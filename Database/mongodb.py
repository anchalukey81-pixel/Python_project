from pymongo import MongoClient

try:
    MONGO_URI = "mongodb+srv://anchalukey81_db_user:Anchal%4006@cluster0.0pc0lvp.mongodb.net/?appName=Cluster0"

    client = MongoClient(MONGO_URI)

    client.admin.command("ping")

    db = client["ssus"]

    students_collection = db["students"]

    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]

    print("MongoDB Connected Successfully")
except Exception as e:
    print("MongoDB Error:", e)
