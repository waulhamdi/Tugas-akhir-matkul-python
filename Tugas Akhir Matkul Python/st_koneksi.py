import streamlit as st
import mysql.connector
# buat definisi koneksi
def koneksi():
  connect = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'dbatm',
    port = 3306
  )
# return var
  return connect

if __name__ == '__main__':
  koneksi()