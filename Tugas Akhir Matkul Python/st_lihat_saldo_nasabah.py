import streamlit as st
import mysql.connector
import st_koneksi

def Lihat():
    genre = st.radio(
        "Lihat Saldo Nasabah",
        ('Semua Nasabah', 'By no rekening', 'By Pin'))

    if genre == 'Semua Nasabah':        
        connect = st_koneksi.koneksi()
        mycrusor = connect.cursor()
        mycrusor.execute('select * from tb_nasabah')
        data = mycrusor.fetchall()

        # looping
        nomor =0
        ttl=0
        st.warning('SEMUA NASABAH')
        st.write('No - No Rekening - Nama Nasabah - PIN ATM - Saldo - Alamat')
        st.write('=================')

        for dt in data:
            nomor = nomor+1
            xnorek = dt[0]
            xname = dt[1]
            xpin = dt[2]
            xsaldo = dt[3]
            xalamat = dt[4]

            st.write(f'{nomor}.{xnorek},{xname},{xpin},{xsaldo},{xalamat}')
    elif genre == 'By no rekening':
        xnorek = st.text_input('Input No rekening')
        view = st.button('Preview')
        if(view):
            if(xnorek==''):
                st.error('Masukan No rekening')
            else:
                conn = st_koneksi.koneksi()
                sql = "select * from tb_nasabah where no_rekening = '%s'" %xnorek
                mycursor = conn.cursor()    #siapkan data
                mycursor.execute(sql)     #jalankan var sql 
                data = mycursor.fetchall()    #ambil data
                
                # looping
                nomor =0
                ttl=0
                st.warning('By no Rekening')
                st.write('No - No Rekening - Nama Nasabah - PIN ATM - Saldo - Alamat')
                st.write('=================')

                for dt in data:
                    nomor = nomor+1
                    xnorek = dt[0]
                    xname = dt[1]
                    xpin = dt[2]
                    xsaldo = dt[3]
                    xalamat = dt[4]

                    st.write(f'{nomor}.{xnorek},{xname},{xpin},{xsaldo},{xalamat}')
                    st.snow()
    else:
        xpin = st.text_input("Input No PIN")
        view = st.button('Preview')
        if(view):
            if(xpin==''):
                st.error('Masukan PIN ATM Anda')
            else:
                conn = st_koneksi.koneksi()
                sql = "select * from tb_nasabah where pin_atm = '%s'" %xpin
                mycursor = conn.cursor()    #siapkan data
                mycursor.execute(sql)     #jalankan var sql 
                data = mycursor.fetchall()    #ambil data
                
                # looping
                nomor =0
                ttl=0
                st.warning('By No Pin')
                st.write('No - No Rekening - Nama Nasabah - PIN ATM - Saldo - Alamat')
                st.write('=================')

                for dt in data:
                    nomor = nomor+1
                    xnorek = dt[0]
                    xname = dt[1]
                    xpin = dt[2]
                    xsaldo = dt[3]
                    xalamat = dt[4]

                    st.write(f'{nomor}.{xnorek},{xname},{xpin},{xsaldo},{xalamat}')
                    st.snow()
        
                conn.close()
        
