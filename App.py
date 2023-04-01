import streamlit as st 
#Shakira Fairuz Putri 120140217 UTS KSI
st.title('Hitung Skor SUS')

#meminta masukan berupa skor dari masing-masing pertanyaan
q1 = st.slider("Masukkan Skor Pertanyaan 1 ", 0, 5)
q1 = q1 - 1

q2 = st.slider("Masukkan Skor Pertanyaan 2 ", 0, 5)
q2 = 5 - q2

q3 = st.slider("Masukkan Skor Pertanyaan 3 ", 0, 5)
q3 = q3 - 1

q4 = st.slider("Masukkan Skor Pertanyaan 4 ", 0, 5)
q4 = 5 - q4

q5 = st.slider("Masukkan Skor Pertanyaan 5 ", 0, 5)
q5 = q5 - 1

q6 = st.slider("Masukkan Skor Pertanyaan 6 ", 0, 5)
q6 = 5 - q6

q7 = st.slider("Masukkan Skor Pertanyaan 7 ", 0, 5)
q7 = q7 - 1

q8 = st.slider("Masukkan Skor Pertanyaan 8 ", 0, 5)
q8 = 5 - q8

q9 = st.slider("Masukkan Skor Pertanyaan 9 ", 0, 5)
q9 = q9 - 1

q10 = st.slider("Masukkan Skor Pertanyaan 10 ", 0, 5)
q10 = 5 - q10

#tombol untuk menghitung
hitung = st.button("Hitung SUS")
#perulangan untuk menghitung
if hitung:
    sus = (q1+q2+q3+q4+q5+q6+q7+q8+q9+q10)*2.5
    st.success (f"Nilai SUS adalah = {sus}")

st.header('Hitung Rata-rata SUS')

n = st.number_input("Masukkan Banyak Responden", 0)
data = []
jum = 0
#menghitung rata-rata
for i in range(0, n):
    temp = int(st.number_input("Masukkan data ke %d: " % (i+1)))
    data.append(temp)
    jum+= data[i]
    rata2 = jum/n

hitung2 = st.button("Hitung Rata-rata")
#menghitung grade
if hitung2:
    st.success(f"Nilai Rata-rata SUS adalah = {rata2}")
    if rata2 >= 80.3:
        st.success("Grade A")
    elif rata2 >= 74.0 and rata2 < 80.3:
        st.success("Grade B")
    elif rata2 >= 68.0 and rata2 < 74.0:
        st.success("Grade C")
    elif rata2 >= 51.0 and rata2 < 68.0:
        st.success("Grade D")
    elif rata2 < 51.0:
        st.success("Grade F")