import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Предобработка данных")
st.title('Фотографии и ссылка на код, где были обработаны взянные данные')

st.image('1.jpg', caption='Считывание датасета')
st.image('2.jpg', caption='Discribe, Info')
st.image('3.jpg', caption='Переименование столбцов')
st.image('4.jpg', caption='Замена пустых значений')
st.image('5.jpg', caption='Приведение типов, сохранение датасета')

st.write('------------------------------------------------------------------------------------------------------------------------------------------')
st.write('ССЫЛКА НА ОБРАБОТКУ ДАННЫХ : https://github.com/RabbiPaw/-/blob/main/Labs/Lab1/Обработка%20данных.ipynb')

    