import streamlit as st
from time import sleep
from PIL import Image
import pandas as pd 

st.header(f"Приветствуем на сайте Digital life school!")
st.write("На этом сайте предоставлена краткая информация по всем курсам. Так же вы можете посчитать через калькулятор стоимость курса")
st.image("katana.jpg")

def show_services():
    price1 = 12000
    price2 = 20000
    price3 = 28000
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("⚔️Путь ронина")
        st.write("Самостоятельный путь. Ты учишься в одиночку, следуя гайдам и системе прокачки. Ты сам себе учитель — мы даём только меч и карту.")
        st.write("Цена:",price1)
    with col2:
        st.header("🧠Ментор")
        st.write("Классический путь ученика. Ты получаешь доступ к гайдам, заданиям, трекеру, и ментор ведёт тебя через каждый этап. Раз в неделю — созвон. В любой момент — чат поддержки.")
        st.write("Цена:", price2)
    with col3:
        st.header("🔥Ментор+")
        st.write("Продвинутая версия менторства. Индивидуальная обратная связь, проверка кода, адаптация под твои цели (работа, стартап, собес). Ты не просто учишься — ты готовишься побеждать.")
        st.write("Цена:", price3)
show_services()

st.header("🌊 Ты знаешь, какой путь выбрать.")
st.write("Школа открыта. Меч — у входа.")
col1,col2,col3 = st.columns(3)
with col2:
    st.link_button("Записаться","https://wa.me/message/EJ6TMZ7FAL66B1")

