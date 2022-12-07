import streamlit as st
import mysql.connector

def Print_PDF():
    genre = st.radio(
    "PRINT SALDO NASABAH",
    ('Semua Nasabah', 'By No Rekening', 'By PIN ATM'))

    if genre == 'Semua Nasabah':
        st.write('You selected comedy.')
    elif genre == 'By No Rekening': 
        st.write("You didn't select comedy.")
    else:
        st.write("You didn't select comedy.")