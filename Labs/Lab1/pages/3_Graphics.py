import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.set_page_config(page_title = "Визуализация")
st.title('Визуализация зависимостей в наборе данных')

df = pd.read_csv("Labs/Lab1/df_filtered.csv")

########### Круговая диаграмма ###########
st.write(df.head())
if st.button('Круговая диаграмма'):
    fig, ax = plt.subplots()
    
    ax.pie(
        x=list(df['is_game_center_enabled'].value_counts()), 
        labels=['4+','9+','12+','17+'],
        autopct='%1.1f%%',
        colors=['red','green','blue','yellow']
    )

    plt.title('Круговая диаграмма статуса домов')
    
    st.pyplot(fig)

########### Гистограмма ###########
if st.button('Гистограмма веса игр'):
    fig,ax = plt.subplots()

    ax.hist(df['file_size_bytes'])
    
    plt.xlabel('Вес игры')
    
    plt.ylabel('Количество игр')
    
    plt.title('Гистограмма веса мгр')
    
    st.pyplot(fig)

########### Тепловая карта корреляции ###########
if st.button('Тепловая карта корреляции'):
    fig = plt.figure()
    data = df[["average_user_rating", "average_user_rating_for_current_version",
                "file_size_bytes","price","primary_genre_id","user_rating_count"]]
    sns.heatmap(
        data.corr(),
        cmap="YlGnBu", 
        annot=True
    )

    plt.title('Тепловая карта корреляции\n')

    st.pyplot(fig)

########### Зависимость цены от года ###########
def correlation(df,parametr,target):
    sns.lmplot(x=parametr,y=target,data=df)
    plt.title(f'Зависимость {target} от {parametr}')

if st.button('График зависимости рейтинга иры от цены игры'):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(correlation(df,'average_user_rating','price'))
