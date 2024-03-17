import streamlit as st

def app():
    st.write('Account')

    st.title('Welcome to :blue[Citasi]')

    choice = st.selectbox('Login/signup', ['Login', 'Sign Up'])
    if choice=='Login':
        email = st.text_input('Email Addres')
        password = st.text_input('password', type='password')

        st.button ('Login')

    else:
        email = st.text_input('Email Addres')
        password = st.text_input('password', type='password')
        username = st.text_input('Enter Your Username')

        st.button ('Login')
