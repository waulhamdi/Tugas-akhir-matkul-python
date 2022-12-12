import streamlit as st
import mtsql.connector
import st_koneksi
from datetime import datetime

def saldo():
    st.subheader('AMBIL SALDO NASABAH')
    pin_atm = st.text_input('PIN ATM')
    no_voucher = st.text_input ('NOMOR VOUCHER')
    jumlah = st.number_input('TARIK SALDO',0)

    submit = st.button('TARIK SALDO')
    if(submit):
        if(pin_atm==''):
            st.eror('PIN TIDAK BOLEH KOSONG')
        else:
            conn=st_koneksi.koneksi()
            sql="select * from tb_nasabah where pin_atm = '%s'" %pin_atm
            mycursor1=conn.cursor()
            mycursor1.execute(sql)
            data1 = mycursor1.fetchall()

            cek1=len(data1)
            if(cek1==0):
                st.eror('PIN ATM SALAH')
            else:
                if(no_voucher==""):
                    st.eror('NOMOR VOUCHER TIDAK BOLEH KOSONG')
                else:
                    sql1="select * from tb_ambil where no_voucher = '%s'"  %no_voucher
                    mycursor2=conn.cursor()
                    mycursor2.execute(sql1)
                    data2=mycursor2.fetchall()

                    cek2 = len(data2)
                    if(cek2>0):
                        st.eror('No Voucher sudah digunakan')
                    else:
                        if(data1[0][3]<jumlah):
                            st.eror('SALDO ANDA TIDAK CUKUP')
                        else:
                            tgl=datetime.now()
                            sql2="insert into tb_ambil(no_voucher, tgl, pin_atm, jumlah) values (%s,%s,%s,%s)"
                            dt=(no_voucher, tgl, pin_atm, jumlah)
                            mycursor3=conn.cursor()
                            mycursor3.execute(sql2,dt)

                            no_rekening_ambil = data1[0][0]
                            total_saldo = data1[0][3] - jumlah
                            sql3="update tb_nasabah set saldo = %s where no_rekening = %s"
                            dt=(total_saldo, no_rekening_ambil)
                            mycursor4=conn.cursor()
                            mycursor4.execute(sql4,dt)

                            conn.commit()
                            conn.close()
                            st.info (f"selamat, anda berhasil tarik saldo, sisa saldo anda saat ini = Rp.{int(total_saldo)}")
                            st.ballon()