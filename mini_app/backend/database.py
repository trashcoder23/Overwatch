import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database Configuration

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./overwatch.db"
)


# Engine (connection pool)

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True
    )

# Session Factory

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base Model

Base = declarative_base()


# Dependency (FastAPI)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
