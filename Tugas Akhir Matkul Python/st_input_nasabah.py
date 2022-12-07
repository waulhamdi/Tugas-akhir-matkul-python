import streamlit as st
import mysql.connector
import st_koneksi

def Input():
    st.info('INPUT NASABAH')
    norek = st.text_input('NO REKENING')
    nama = st.text_input('NAMA NASABAH')
    pin = st.text_input('PIN ATM')
    saldo = st.number_input('SALDO',0)
    alamat = st.text_input('ALAMAT')
        
    #tombol
    cek = st.button('SAVE')
    if(cek):
        if (norek == ''):
            st.error('NO REKENING BELUM DI INPUT')
        else:
            # buka koneksi
            conn = st_koneksi.koneksi()
            sql = "select * from tb_nasabah where no_rekening = '%s'" %norek
            mycursor = conn.cursor()    #siapkan data
            mycursor.execute(sql)     #jalankan var sql 
            dataku = mycursor.fetchall()    #ambil data 

            jika_ada = len(dataku)
            if(jika_ada > 0 ):
                st.error('NO REKENING SUDAH ADA')
            else:
                # save data
                sql = 'insert into tb_nasabah \
                (no_rekening,nama_nasabah,pin_atm,saldo,alamat) \
                    value (%s, %s, %s, %s, %s)'
                dt = (norek, nama, pin, saldo, alamat)
                mycursor = conn.cursor()
                mycursor.execute (sql, dt) #jalankan sql
                conn.commit()   #save transaksi
                conn.close()    #tutup koneksi

            # message
                st.header('DATA TELAH DI SIMPAN')
                st.balloons()