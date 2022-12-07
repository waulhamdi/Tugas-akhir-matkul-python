import streamlit as st
import mysql.connector
import st_koneksi
from fpdf import FPDF

def Print_PDF():
    genre = st.radio(
    "PRINT SALDO NASABAH",
    ('Semua Nasabah', 'By No Rekening', 'By PIN ATM'))

    if genre == 'Semua Nasabah':
        st.info ('PRINT DATA NASABAH KE PDF')
        cek = st.button('Print PDF')
        if (cek):

            # PDF
            # LAYOUT('P','L'), UNIY('MM','CM','IN')
            # FORMAT('A3','A4','DEFAULT','A5','LETTER','LEGAL','(100,150) CUSTOM)
            pdf = FPDF ('p','cm','A4')
            pdf.set_auto_page_break(auto=True,margin=1)
            pdf.add_page()

            # warna
            # 0,0,0 = hitam, 220,50,50 = merah 245,250,50 = kuning
            # 90,50,150

            # judul laporan
            pdf.set_font('helvetica','B',20)
            pdf.set_text_color(90,50,150)
            pdf.cell(0,1,'DATA NASABAH',align='C')
            pdf.ln()
            pdf.set_text_color(0,0,0)
            pdf.set_font('helvetica','',10)
            pdf.cell(0,2,'No    No Rekening    Nama Nasabah   Satuan    Stok')
            pdf.ln()

            # ambil konekasi server
            conn=st_koneksi.koneksi()
            mycursor= conn.cursor()
            mycursor.execute('select * from tb_nasabah order by no_rekening')
            dataku= mycursor.fetchall()

            nomer = 0
            tsaldo = 0

            for dt in dataku:
                nomer   = nomer+1
                xnorek   = dt[0]
                xname   = dt[1]
                xpin = dt[2]
                xsaldo   = dt[3]

                tsaldo = tsaldo + xsaldo

                # print PDF
                pdf.cell(0,0.7,f'({nomer}). {xnorek} , {xname} , {xpin} , {xsaldo}')
                pdf.ln()

            # print total
            pdf.set_text_color(220,50,50) #merah
            pdf.cell(0,0.7, f'Total Stok = {tsaldo} ')
            conn.close()
            st.balloons()

            # save PDF
            pdf.output('data_nasabah.pdf')
            st.warning('OK, File sudah diprint, Silahkan buka explorer')
    elif genre == 'By No Rekening':
        st.info ('PRINT DATA NASABAH KE PDF')
        norek = st.text_input('Input No Rekening')
        cek = st.button('Print PDF')
        if(cek):
            
            # PDF
            # LAYOUT('P','L'), UNIY('MM','CM','IN')
            # FORMAT('A3','A4','DEFAULT','A5','LETTER','LEGAL','(100,150) CUSTOM)
            pdf = FPDF ('p','cm','A4')
            pdf.set_auto_page_break(auto=True,margin=1)
            pdf.add_page()

            # warna
            # 0,0,0 = hitam, 220,50,50 = merah 245,250,50 = kuning
            # 90,50,150

            # judul laporan
            pdf.set_font('helvetica','B',20)
            pdf.set_text_color(90,50,150)
            pdf.cell(0,1,'DATA NASABAH',align='C')
            pdf.ln()
            pdf.set_text_color(0,0,0)
            pdf.set_font('helvetica','',10)
            pdf.cell(0,2,'No    No Rekening    Nama Nasabah   Satuan    Stok')
            pdf.ln()


            # ambil konekasi server
            conn=st_koneksi.koneksi()
            mycursor= conn.cursor()
            mycursor.execute("select * from tb_nasabah where no_rekening = '%s'" %norek)
            dataku= mycursor.fetchall()


            nomer = 0
            tsaldo = 0

            for dt in dataku:
                nomer   = nomer+1
                xnorek   = dt[0]
                xname   = dt[1]
                xpin = dt[2]
                xsaldo   = dt[3]

                tsaldo = tsaldo + xsaldo

                # print PDF
                pdf.cell(0,0.7,f'({nomer}). {xnorek} , {xname} , {xpin} , {xsaldo}')
                pdf.ln()

            # print total
            pdf.set_text_color(220,50,50) #merah
            pdf.cell(0,0.7, f'Total Stok = {tsaldo} ')
            conn.close()
            st.balloons()

            # save PDF
            pdf.output('data_nasabah.pdf')
            st.warning('OK, File sudah diprint, Silahkan buka explorer')
    else:
        st.info ('PRINT DATA NASABAH KE PDF')
        pin = st.text_input('Input No Rekening')
        cek = st.button('Print PDF')
        if(cek):
            
            # PDF
            # LAYOUT('P','L'), UNIY('MM','CM','IN')
            # FORMAT('A3','A4','DEFAULT','A5','LETTER','LEGAL','(100,150) CUSTOM)
            pdf = FPDF ('p','cm','A4')
            pdf.set_auto_page_break(auto=True,margin=1)
            pdf.add_page()

            # warna
            # 0,0,0 = hitam, 220,50,50 = merah 245,250,50 = kuning
            # 90,50,150

            # judul laporan
            pdf.set_font('helvetica','B',20)
            pdf.set_text_color(90,50,150)
            pdf.cell(0,1,'DATA NASABAH',align='C')
            pdf.ln()
            pdf.set_text_color(0,0,0)
            pdf.set_font('helvetica','',10)
            pdf.cell(0,2,'No    No Rekening    Nama Nasabah   Satuan    Stok')
            pdf.ln()


            # ambil konekasi server
            conn=st_koneksi.koneksi()
            mycursor= conn.cursor()
            mycursor.execute("select * from tb_nasabah where pin_atm = '%s'" %pin)
            dataku= mycursor.fetchall()


            nomer = 0
            tsaldo = 0

            for dt in dataku:
                nomer   = nomer+1
                xnorek   = dt[0]
                xname   = dt[1]
                xpin = dt[2]
                xsaldo   = dt[3]

                tsaldo = tsaldo + xsaldo

                # print PDF
                pdf.cell(0,0.7,f'({nomer}). {xnorek} , {xname} , {xpin} , {xsaldo}')
                pdf.ln()

            # print total
            pdf.set_text_color(220,50,50) #merah
            pdf.cell(0,0.7, f'Total Stok = {tsaldo} ')
            conn.close()
            st.balloons()

            # save PDF
            pdf.output('data_nasabah.pdf')
            st.warning('OK, File sudah diprint, Silahkan buka explorer')