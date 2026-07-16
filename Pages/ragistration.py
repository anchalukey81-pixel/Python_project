import streamlit as st

from Database.mongodb import students_collection 

st.title("student registration")

first_name = st.text_input(
    "First Name"
)

last_name = st.text_input(
     "Last Name"
)

email = st.text_input(
    "Email"
)

course = st.text_input(
    "Course"
)

if st.button("Registration Student"):

    students_collection.insert_one({
        
        "Frist_name":first_name,

        "Last_name":last_name,

        "email":email,

        "course":course

    })

    st.success(
        "Students Registration Successfully"
    )
    


