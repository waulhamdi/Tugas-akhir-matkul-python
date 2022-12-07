import streamlit as st
import mysql.connector
import st_koneksi

def Delete():
    st.info ('DELETE DATA NASABAH')
    norek = st.text_input ('NO REKENING')

    #Tombol
    cek = st.button ('DELETE')
    if (cek):

        # cek kode sudah diinput
        if (norek==''):
            st.error ('NO REKENING BELUM DI INPUT')

        else:
            #cek apakah kode ada

            conn = st_koneksi.koneksi()
            sql = "select * from tb_nasabah where no_rekening = '%s'" % norek
            mycursor = conn.cursor()      #Siapkan data
            mycursor.execute (sql)        #Jalankan SQL
            dataku = mycursor.fetchall()  #Ambil data

            #cek data, jika NOL = kode salah
            ada = len(dataku)             #Ambil banyak data
            if (ada == 0):
                st.error ('NO REKENING SALAH')

            else:
                #Save data
                sql = "DELETE FROM tb_nasabah WHERE no_rekening = '%s'" % norek
                
                mycursor = conn.cursor()
                mycursor.execute (sql)           #Jalankan SQL
                conn.commit()                       #Save transaksi
                conn.close()                        #Tutup Koneksi

                st.header ('DATA TELAH DI HAPUS')
                st.balloons()