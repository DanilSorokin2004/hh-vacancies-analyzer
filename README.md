# 📊 Анализатор вакансий Python (SuperJob API)

Сервис для сбора, анализа и визуализации вакансий с платформы SuperJob. Проект демонстрирует навыки работы с API, базами данных, аналитикой данных и созданием интерактивных дашбордов.

## 🎯 Возможности

- **Сбор данных** — парсинг вакансий через API SuperJob (с фильтрацией по ключевому слову).
- **Хранение** — сохранение вакансий в PostgreSQL (SQLAlchemy ORM).
- **Анализ** — топ компаний, средние зарплаты по городам, топ навыков.
- **Визуализация** — интерактивный дашборд на Streamlit с графиками Plotly.
- **Docker** — запуск PostgreSQL одной командой.

## 🏗 Архитектура

```
[SuperJob API] → [parser.py] → [PostgreSQL] → [analyzer.py] → [Streamlit Dashboard]
```

## 🛠 Стек технологий

- **Python 3.12**
- **httpx** — HTTP-клиент для API
- **SQLAlchemy 2.x** — ORM
- **PostgreSQL** — база данных
- **Streamlit** — дашборд
- **Plotly** — интерактивные графики
- **Pandas** — обработка данных
- **Docker** — контейнеризация

## 🚀 Запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/DanilSorokin2004/hh-vacancies-analyzer.git
cd hh-vacancies-analyzer
```

### 2. Создать виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Создать `.env`

```
SUPERJOB_SECRET_KEY=ваш_ключ_от_superjob
DATABASE_URL=postgresql+psycopg2://user:password@127.0.0.1:5432/hh_db
```

### 5. Запустить PostgreSQL (Docker)

```bash
docker compose up -d
```

### 6. Загрузить вакансии

```bash
python -m app.parser
```

### 7. Запустить дашборд

```bash
python -m streamlit run app/dashboard.py
```

**Дашборд:** http://localhost:8501

## 📸 Скриншоты

*(добавь сюда скриншоты дашборда, когда они будут готовы)*

## 📄 Лицензия

MIT License — см. файл [LICENSE](LICENSE)

## 👤 Автор

**Данил Сорокин**
- GitHub: [@DanilSorokin2004](https://github.com/DanilSorokin2004)
