import streamlit as st

st.set_page_config(page_title = "Набор данных")

st.title("Описание датасета")

st.markdown(
  '''
  ### Чему посвящён
    Датасет содержит информацию об играх\
    на площадке appstore\

  ### Описание признаков
    - artist_name -  название компании производителя
    - average_user_rating - рэйтинг игры по оценкам пользователей
    - average_user_rating_for_current_version - рэйтинг нынешней версии игры по оценке пользователей
    - content_advisory_rating - возрастной рэйтинг игры
    - description - описание игры в магазине
    - file_size_bytes - размеры игры в байтах
    - is_game_center_enabled - доступен ли игровой центр
    - minimum_os_version - минимальная версия ios для скачивания
    - price - цена игры
    - primary_genre_id - основной id жанра
    - release_date - дата релиза игры
    - track_name - название игры
    - user_rating_count - количество оценок пользователей
    - release_notes - описание к релизу.
    ''')