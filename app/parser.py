import os
import json
import httpx
from dotenv import load_dotenv
from app.database import init_db, get_session
from app.models import Vacancy

load_dotenv()

SECRET_KEY = os.getenv('SUPERJOB_SECRET_KEY')
API_URL = 'https://api.superjob.ru/2.0/vacancies/'

def fetch_vacancies(keyword: str = 'Python', count: int = 100, page: int = 0):
    headers = {'X-Api-App-Id': SECRET_KEY}
    params = {'keyword': keyword, 'count': count, 'page': page}
    response = httpx.get(API_URL, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    return response.json()

def save_vacancies(data: dict):
    session = get_session()
    saved = 0

    print(f'[DEBUG] Получено объектов: {len(data.get('objects', []))}')

    for item in data.get('objects', []):
        try:
            existing = session.query(Vacancy).filter_by(id=item['id']).first()
            if existing:
                continue

            vacancy = Vacancy(
                id = item['id'],
                title = item.get('profession', 'Без названия'),
                company = item.get('firm_name', ''),
                town = item.get('town', {}).get('title', '') if item.get('town') else '',
                salary_from = item.get('payment_from', 0) or 0,
                salary_to = item.get('payment_to', 0) or 0,
                currency = item.get('currency', 'rub'),
                experience = item.get('experience', {}).get('title', ''),
                employment = item.get('type_of_work', {}).get('title', ''),
                description = item.get('candidat', ''),
                link = item.get('link', ''),
                skills = json.dumps([s['title'] for s in item.get('professionalskills', [])]),
            )
            session.add(vacancy)
            saved += 1

        except Exception as e:
            print(f'[ERROR] Не удалось сохранить вакансию {item.get('id')}: {e}')
            session.rollback()
            continue

    session.commit()
    session.close()
    print(f'[DEBUG] Сохранено в БД: {saved}')
    return saved

def parse_all(keyword: str = 'Python', pages: int = 5):
    init_db()
    total_saved = 0

    for page in range(pages):
        print(f'Страница {page + 1}...')
        data = fetch_vacancies(keyword=keyword, page=page)
        saved = save_vacancies(data)
        total_saved = saved
        print(f'Сохранено: {saved}')

        if not data.get('more'):
            break

    print(f'\nВсего сохранено: {total_saved}')

if __name__ == '__main__':
    parse_all(keyword='Python', pages=5)