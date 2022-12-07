import streamlit as st


import st_lihat_saldo_nasabah
import st_saldo_nasabah_pdf
import st_lihat_transaksi

def menu_home():
    st.image('image/logo.jpg')
    st.header('PROGRAM ATM TARIK SALDO NASABAH')
def menu_programmer():
    st.info('KELOMPOK 3')
    st.subheader('Afif Vito Fadlurohman')
    st.subheader('Muhammad Taufik Hidayat')
    st.subheader('Muhammad Liwaul Hamdi')
    st.subheader('Ricki Agustin')
def menu():
	
	with st.sidebar:
		st.image('image/computer.png', width=100)
		pilih = st.selectbox('MENU ATM TARIK SALDO',['Home','Programmer'\
			,'Input Nasabah','Edit Nasabah','Delete Nasabah','-----Transaksi------'\
			,'ATM ambil uang','ATM hapus transaksi','----Laporan----','Lihat saldo nasabah'\
			,'Print saldo nasabah PDF','Lihat transaksi tarik saldo'])

	if (pilih=='Home'):
		menu_home()
	elif (pilih=='Programmer'):
		menu_programmer()
	elif (pilih=='Lihat saldo nasabah'):
		st_lihat_saldo_nasabah.Lihat()
	elif (pilih=='Print saldo nasabah PDF'):
		st_saldo_nasabah_pdf.Print_PDF()
	else:
		st_lihat_transaksi.Lihat_Transaksi()


def main():
  menu()


if __name__ == '__main__':
  main()