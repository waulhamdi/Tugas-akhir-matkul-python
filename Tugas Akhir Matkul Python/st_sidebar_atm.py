import streamlit as st




def menu_home():
    st.header('PROGRAM ATM TARIK SALDO NASABAH')
def programmer():
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


    

def main():
  menu()


if __name__ == '__main__':
  main()