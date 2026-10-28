import streamlit as st
import plotly.express as px
import pandas as pd

from app.analyzer import top_skills, avg_salary_by_city, top_companies
from app.database import get_session
from app.models import Vacancy

st.set_page_config(page_title='Анализ вакансий Python', layout='wide')
st.title('📊 Анализ вакансий Python')

session = get_session()
total = session.query(Vacancy).count()
session.close()

col1, col2, col3 = st.columns(3)
col1.metric('Всего вакансий', total)

skills_data = top_skills(1)
col2.metric('Топ-навык', skills_data[0][0] if skills_data else '—')

cities_data = avg_salary_by_city(1)
col3.metric('Топ-город по зарплате', cities_data[0]['town'] if cities_data else '—')

# Топ-навыки
st.subheader('🔧 Топ-10 навыков')
skills_data = top_skills(10)
if skills_data:
    df = pd.DataFrame(skills_data, columhs=['Навык', 'Количество'])
    fig = px.bar(df, x='Навык', y='Количество', text='Количество')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info('Нет данных по навыкам (API SuperJob не заполняет это поле для многих вакансий)')

# Средняя зарплата по городам
st.subheader('💰 Средняя зарплата по городам')
salary_data = avg_salary_by_city(10)
if salary_data:
    df = pd.DataFrame(salary_data)
    fig = px.bar(df, x = 'town', y = 'avg_salary', text = 'avg_salary',
                 labels = {'town': 'Город', 'avg_salary': 'Средняя зарплата (₽)'})
    st.plotly_chart(fig, use_container_width=True)

# Топ-компаний
st.subheader('🏢 Топ-10 компаний')
companies_data = top_companies(10)
if companies_data:
    df = pd.DataFrame(companies_data)
    fig = px.pie(df, names = 'company', values = 'count')
    st.plotly_chart(fig, use_container_width=True)
