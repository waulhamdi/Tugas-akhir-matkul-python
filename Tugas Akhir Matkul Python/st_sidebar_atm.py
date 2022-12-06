import streamlit as st


import st_lihat_saldo_nasabah

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
    pilih = st.selectbox('Menu Barang',['Home','Programmer'\
        ,'Input Nasabah','Edit Nasabah','Delete Nasabah','-----Transaksi------'\
        ,'ATM ambil uang','ATM hapus transaksi','----Laporan----','Lihat saldo nasabah'\
        ,'Print saldo nasabah PDF','Lihat transaksi tarik saldo'])

  if (pilih=='Home'):
    menu_home()
  elif (pilih=='Programmer'):
    menu_programmer()
  elif (pilih=='Lihat saldo nasabah'):
    st_lihat_saldo_nasabah.Lihat()


def main():
  menu()


if __name__ == '__main__':
  main()