import pyrebase
import streamlit as st
from datetime import datetime

firebaseConfig = {
  'apiKey': "AIzaSyAoSi4C4T65EZs0dCJCzjXXadYduAvzT_w",
  'authDomain': "final-year-project-e6e81.firebaseapp.com",
  'databaseURL': "https://final-year-project-e6e81-default-rtdb.firebaseio.com",
  'projectId': "final-year-project-e6e81",
  'storageBucket': "final-year-project-e6e81.appspot.com",
  'messagingSenderId': "36719237646",
  'appId': "1:36719237646:web:b483b05c2a84fea25e3a5f",
  'measurementId': "G-MCWKJSPV8F"
}

# Initialize Firebase
firebase    = pyrebase.initialize_app(firebaseConfig)
auth        = firebase.auth()
db          = firebase.database()
storage     = firebase.storage()

#sign up
def signup():
    #st.title("Final Year Project")
    st.title("Sign Up")
    email = st.text_input("Email")
    #check if email is valid email
    if email:
        if "@" not in email:
            st.error("Invalid Email")
        elif "." not in email:
            st.error("Invalid Email")
        elif " " in email:
            st.error("Invalid Email")
        elif len(email) < 5:
            st.error("Invalid Email")
        else:
            st.success("Valid Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("User Created")
            st.balloons()
            login()
        except:
            st.error("Email already exists")


# Login Page
def login():
    #st.title("Final Year Project")
    st.title("Login")
    email    = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            auth.sign_in_with_email_and_password(email, password)
            st.success("Logged In")
            main()
        except:
            st.error("Invalid Email or Password")

def update_cat1On(value):
    ref = db.child("OVERRIDE").child('CATEGORY1').child("setOn")
    ref.set(value)
    #st.write("Fog!!")
def update_cat1Off(value):
    ref = db.child("OVERRIDE").child("CATEGORY1").child('setOff')
    ref.set(value)
    

def update_cat2On(value):
    ref = db.child("OVERRIDE").child("CATEGORY2").child('setOn')
    ref.set(value)
    
def update_cat2Off(value):
    ref = db.child("OVERRIDE").child("CATEGORY2").child('setOff')
    ref.set(value)
    

def update_cat3On(value):
    ref = db.child("OVERRIDE").child("CATEGORY3").child('setOn')
    ref.set(value)
    
def update_cat3Off(value):
    ref = db.child("OVERRIDE").child("CATEGORY3").child('setOff')
    ref.set(value)

# Main Page
def main():
    st.title("PARAMETERS")
    #st.subheader("Main")

    # Get data from Firebase Realtime Database
    amp1         = db.child("CATEGORY1"    ).child("Current(A)"        ).get()
    volt1        = db.child("CATEGORY1"    ).child("Voltage(V)"        ).get()
    power1       = db.child("CATEGORY1"    ).child("Power(W)"          ).get()
    amp2         = db.child("CATEGORY2"    ).child("Current(A)"        ).get()
    volt2        = db.child("CATEGORY2"    ).child("Voltage(V)"        ).get()
    power2       = db.child("CATEGORY2"    ).child("Power(W)"          ).get()
    amp3         = db.child("CATEGORY3"    ).child("Current(A)"        ).get()
    volt3        = db.child("CATEGORY3"    ).child("Voltage(V)"        ).get()
    power3       = db.child("CATEGORY3"    ).child("Power(W)"          ).get()
    fuel         =db.child("FUEL").get()

    # Display data
    st.subheader("CATEGORY 1")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Current: ", amp1.val())
    with col2:
        st.write("Voltage: ", volt1.val())
    with col3:
        st.write("Power: ",   power1.val())
    
    st.subheader("CATEGORY 2")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Current: ", amp2.val())
    with col2:
        st.write("Voltage: ", volt2.val())
    with col3:
        st.write("Power: ",   power2.val())
    
    st.subheader("CATEGORY 3")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Current: ", amp3.val())
    with col2:
        st.write("Voltage: ", volt3.val())
    with col3:
        st.write("Power: ",   power3.val())
    
    st.subheader("FUEL")
    st.write("Fuel: ",fuel.val())
    
    st.title("MANUAL OVERRIDE")
    st.subheader("CATEGORY 1")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("TURN ON 1(ON)"):
            update_cat1On(True)
            st.success("Manual ON  activated")
    with col2:
        if st.button("TURN ON 1(OFF)"):
            update_cat1On(False)
            st.success("Manual ON deactivated")
    with col3:
        if st.button("TURN OFF 1(ON)"):
            update_cat1Off(True)
            st.success("Manual OFF  activated")
    with col4:
        if st.button("TURN OFF 1(OFF)"):
            update_cat1Off(False)
            st.success("Manual OFF deactivated")
            
    st.subheader("CATEGORY 2")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("TURN ON 2(ON)"):
            update_cat2On(True)
            st.success("Manual ON  activated")
    with col2:
        if st.button("TURN ON 2(OFF)"):
            update_cat2On(False)
            st.success("Manual ON deactivated")
    with col3:
        if st.button("TURN OFF 2(ON)"):
            update_cat2Off(True)
            st.success("Manual OFF  activated")    
    with col4:
        if st.button("TURN OFF 2(OFF)"):
            update_cat2Off(False)
            st.success("Manual OFF deactivated")
    
    st.subheader("CATEGORY 3")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("TURN ON 3(ON)"):
            update_cat3On(True)
            st.success("Manual ON  activated")
    with col2:
        if st.button("TURN ON 3(OFF)"):
            update_cat3On(False)
            st.success("Manual ON deactivated")
    with col3:
        if st.button("TURN OFF 3(ON)"):
            update_cat3Off(True)
            st.success("Manual OFF  activated")
    
    with col4:
        if st.button("TURN OFF 3(OFF)"):
            update_cat3Off(False)
            st.success("Manual OFF deactivated")
    
    


if __name__ == "__main__":
    st.sidebar.title("ESSENTIAL ELECTRICAL SYSTEM")
    menu = st.sidebar.radio("Menu", ["Login", "SignUp"])
    if menu == "Login":
        login()
    elif menu == "SignUp":
        signup()

#I hope this helps you to get started with Firebase and Streamlit. If you have any questions, please let me know in the comments below.
