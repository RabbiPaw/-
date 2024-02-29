import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.set_page_config(page_title = "Как создавались модели")
st.title('Показ создания моделей')

st.image('2.1.jpg', caption='Подготовка данных, разделение на тестовую и обучающую выборки')
st.image('2.2.jpg', caption='Nearest Neighbors Classification')
st.image('2.3.jpg', caption='Подбор гиперпараметра')
st.image('2.4.jpg', caption='Конечная модель, выгрузка модели')
st.image('2.5.jpg', caption='Полиномиальная регрессия, выгрузка модели')


st.write('------------------------------------------------------------------------------------------------------------------------------------------')
st.write('ССЫЛКА НА СОЗДАНИЕ МОДЕЛЕЙ : https://github.com/RabbiPaw/-/blob/main/Labs/Lab1/Обучение%20моделей.ipynb')