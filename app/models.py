from datetime import datetime
from sqlalchemy import String, Integer, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Vacancy(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    title: Mapped[str] = mapped_column(String(500))
    company: Mapped[str] = mapped_column(String(300), nullable = True)
    town: Mapped[str] = mapped_column(String(100), nullable = True)
    salary_from: Mapped[int] = mapped_column(Integer, nullable = True)
    salary_to: Mapped[int] = mapped_column(Integer, nullable = True)
    currency: Mapped[str] = mapped_column(String(10), nullable = True)
    experience: Mapped[str] = mapped_column(String(100), nullable = True)
    employment: Mapped[str] = mapped_column(String(100), nullable = True)
    description: Mapped[str] = mapped_column(Text, nullable = True)
    link: Mapped[str] = mapped_column(String(500), nullable = True)
    skills: Mapped[str] = mapped_column(Text,  nullable = True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'<Vacancy {self.id}: {self.title}>'