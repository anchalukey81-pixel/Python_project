import streamlit as st
import pandas as pd

from Database.mongodb import (
    students_collection,
    marks_collection
)

from utils.grade import calculate_grade

st.title("Marks Management")

# Students लोड करना
students = list(students_collection.find())

if not students:
    st.warning("कोई student नहीं मिला")
    st.stop()

# Student नामों की लिस्ट बनाना
student_names = []
for student in students:
    # ध्यान दें: आपके DB में "Frist_name" और "Last_name" हैं
    full_name = student["Frist_name"] + " " + student["Last_name"]
    student_names.append(full_name)

# Student चुनना
selected_student = st.selectbox("Select Student", student_names)

# Marks input
python_marks = st.number_input("Python Marks", min_value=0, max_value=100)
sql_marks = st.number_input("SQL Marks", min_value=0, max_value=100)
excel_marks = st.number_input("Excel Marks", min_value=0, max_value=100)

# Save button
if st.button("Save Marks"):
    percentage = (python_marks + sql_marks + excel_marks) / 3
    grade = calculate_grade(percentage)

    # Duplicate से बचने के लिए update_one + upsert
    marks_collection.update_one(
        {"student_name": selected_student},
        {
            "$set": {
                "python": python_marks,
                "sql": sql_marks,
                "excel": excel_marks,
                "percentage": round(percentage, 2),
                "grade": grade,
            }
        },
        upsert=True
    )

    st.success("Marks Saved Successfully")
    st.write("Percentage:", round(percentage, 2))
    st.write("Grade:", grade)

# सभी marks दिखाना
st.subheader("All Marks")
all_marks = list(marks_collection.find())

if all_marks:
    df = pd.DataFrame(all_marks)
    st.dataframe(df[["student_name", "python", "sql", "excel", "percentage", "grade"]])
