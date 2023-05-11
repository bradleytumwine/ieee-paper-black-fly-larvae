import pyrebase
import streamlit as st
from datetime import datetime

firebaseConfig = {
  apiKey: "AIzaSyAoSi4C4T65EZs0dCJCzjXXadYduAvzT_w",
  authDomain: "final-year-project-e6e81.firebaseapp.com",
  databaseURL: "https://final-year-project-e6e81-default-rtdb.firebaseio.com",
  projectId: "final-year-project-e6e81",
  storageBucket: "final-year-project-e6e81.appspot.com",
  messagingSenderId: "36719237646",
  appId: "1:36719237646:web:b483b05c2a84fea25e3a5f",
  measurementId: "G-MCWKJSPV8F"
};

# Initialize Firebase
firebase    = pyrebase.initialize_app(firebaseConfig)
auth        = firebase.auth()
db          = firebase.database()
storage     = firebase.storage()

# sign up
def signup():
    st.title("Final Year Project")
    st.subheader("Sign Up")
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
    st.title("Final Year Project")
    st.subheader("Login")
    email    = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            auth.sign_in_with_email_and_password(email, password)
            st.success("Logged In")
            main()
        except:
            st.error("Invalid Email or Password")

# Main Page
def main():
    st.title("Final Year Project")
    st.subheader("Main")

    # Get data from Firebase Realtime Database
    lux          = db.child("BH1750"    ).child("lux"        ).get()
    temperature  = db.child("DHT"       ).child("temperature").get()
    humidity     = db.child("DHT"       ).child("humidity"   ).get()
    onFog        = db.child("fogMachine").child("isOn"       ).get()
    onShade      = db.child("shadeMotor").child("isOn"       ).get()
    onBulb       = db.child("heaterBulb").child("isOn"       ).get()
    setFog       = db.child("fogMachine").child("setOn"      ).get()
    setShade     = db.child("shadeMotor").child("setOn"      ).get()
    setBulb      = db.child("heaterBulb").child("setOn"      ).get()

    # Display data
    st.write("Lux: ",             lux.val())
    st.write("Temperature: ",     temperature.val())
    st.write("Humidity: ",        humidity.val())
    st.write("Fog Machine: ",     onFog.val())
    st.write("Shade Motor: ",     onShade.val())
    st.write("Heater Bulb: ",     onBulb.val())
    st.write("Set Fog Machine: ", setFog.val())
    st.write("Set Shade Motor: ", setShade.val())
    st.write("Set Heater Bulb: ", setBulb.val())


if __name__ == "__main__":
    st.sidebar.title("Final Year Project")
    menu = st.sidebar.radio("Menu", ["Login", "SignUp"])
    if menu == "Login":
        login()
    elif menu == "SignUp":
        signup()

#I hope this helps you to get started with Firebase and Streamlit. If you have any questions, please let me know in the comments below.
