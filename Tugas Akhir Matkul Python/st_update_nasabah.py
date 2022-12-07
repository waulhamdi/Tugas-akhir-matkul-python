import streamlit as st
import mysql.connector
import st_koneksi

def Update():
    # buka koneksi
    conn = st_koneksi.koneksi()

    st.info('UPDATE DATA NASABAH')
    norek = st.text_input('NO REKENING')
    nama = st.text_input('NAMA NASABAH')
    pin = st.text_input('PIN ATM')
    saldo = st.number_input('SALDO',0)
    alamat = st.text_input('ALAMAT')

    cek=st.button('UPDATE')
    if(cek):
        if(norek ==''):
            st.error('NO REKENING BELUM DIINPUT')
        else:
            sql = "select * from tb_nasabah where no_rekening = '%s'" %norek
            mycursor = conn.cursor()    #siapkan data
            mycursor.execute(sql)     #jalankan var sql 
            dataku = mycursor.fetchall()    #ambil data

            jika_ada = len(dataku)
            if(jika_ada == 0 ):
                st.error('NO REKENING SUDAH ADA')
            else:
                # save data
                sql = "update tb_nasabah set\
                nama_nasabah = %s\
                ,pin_atm =  %s \
                ,saldo = %s \
                ,alamat = %s \
                where no_rekening = %s "
                dt = (nama, pin, saldo, alamat, norek)
                mycursor = conn.cursor()
                mycursor.execute (sql, dt) #jalankan sql
                conn.commit()   #save transaksi
                conn.close()    #tutup koneksi

            # message
                st.header('DATA TELAH DI UPDATE')
                st.snow()