import streamlit as st
import mysql.connector
import st_koneksi

def Lihat_Transaksi():
    connect = st_koneksi.koneksi()
    mycrusor = connect.cursor()
    mycrusor.execute('select * from tb_ambil')
    data = mycrusor.fetchall()

    # looping
    nomor =0
    ttl=0
    st.warning('TRANSAKSI TARIK SALDO')
    st.write('No - No Voucher - Tanggal - PIN ATM - Jumlah')
    st.write('=================')

    for dt in data:
        nomor = nomor+1
        xno_voucher = dt[0]
        stgl = dt[1]
        xpin = dt[2]
        xjumlah = dt[3]
        
        ttl = ttl+xjumlah

        st.write(f'{nomor}.{xno_voucher},{stgl},{xpin},{xjumlah}')

    st.success(f'Total Stok = {ttl}')
    st.snow()
    connect.close()