from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

DATABASE_URL = "sqlite+aiosqlite:///payments.db"

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    username = Column(String)
    amount = Column(Integer)
    payload = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# Создание таблиц
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
