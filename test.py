#!pip install streamlit
import streamlit as st
st.title('Hitung Luas Persegi')
panjang = st.number_input ("Masukan Nilai Panjang",0)
lebar =st.number_input ("Masukan Nilai Lebar", 0)
hitung =st.button("Hitung Luas")

if hitung:
    Luas = panjang * lebar
    st.write ("Luas Persegi Panjang = ", Luas)
#st.success (f"Luas Persegi Panjang = (luas}")