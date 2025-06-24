from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import (
    create_engine,
)

DB_PATH = "sqlite:///my_survey_bot.db"

Base = declarative_base()

engine = create_engine(DB_PATH, echo=False)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)