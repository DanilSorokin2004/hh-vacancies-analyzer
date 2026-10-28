import json
from collections import Counter
from sqlalchemy import func
from app.database import get_session
from app.models import Vacancy

def top_skills(limit: int = 10):
    """Возвращает топ-N навыков по количеству упоминаний"""
    session = get_session()
    vacancies = session.query(Vacancy).filter(Vacancy.skills.isnot(None)).all()
    session.close()

    counter = Counter()
    for v in vacancies:
        try:
            skills = json.loads(v.skills) if v.skills else []
            for skill in skills: 
                counter[skill] += 1

        except (json.JSONDecoderError, TypeError):
            continue

    return counter.most_common(limit)

def avg_salary_by_city(limit: int = 10):
    """Средняя зарплата по городам."""
    session = get_session()
    avg_expr = func.avg(Vacancy.salary_from + Vacancy.salary_to).label("avg_salary")
    results = (
        session.query(
            Vacancy.town,
            avg_expr,
            func.count(Vacancy.id).label("count"),
        )
        .filter(Vacancy.salary_from > 0)
        .filter(Vacancy.salary_to > 0)
        .filter(Vacancy.town.isnot(None))
        .filter(Vacancy.town != "")
        .group_by(Vacancy.town)
        .order_by(avg_expr.desc())
        .limit(limit)
        .all()
    )
    session.close()

    return [
        {"town": r.town, "avg_salary": int(r.avg_salary), "count": r.count}
        for r in results
    ]

def top_companies(limit: int = 10):
    """Топ-N компаний по количеству вакансий"""
    session = get_session()
    results = (
        session.query(
            Vacancy.company,
            func.count(Vacancy.id).label('count'),
        )
        .filter(Vacancy.company.isnot(None))
        .filter(Vacancy.company != '')
        .group_by(Vacancy.company)
        .order_by(func.count(Vacancy.id).desc())
        .limit(limit)
        .all()
    )
    session.close()

    return [{'company': r.company, 'count': r.count} for r in results]

if __name__ == '__main__':
    print('=== Топ-10 навков ===')
    for skill, count in top_skills(10):
        print(f'    {skill}: {count}')

    print('\n=== Средняя зарплата по городам ===')
    for item in avg_salary_by_city(10):
        print(f"  {item['town']}: {item['avg_salary']} ₽ ({item['count']} вакансий)")

    print('\n=== Топ-10 компаний ===')
    for item in top_companies(10):
        print(f'{item['company']}: {item['count']} вакансий')