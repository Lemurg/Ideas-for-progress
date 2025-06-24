from database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text
)
import datetime


class Ideas(Base):
    __tablename__ = "ideas"

    id = Column(Integer, primary_key=True)
    text_idea = Column(String, nullable=True)
    chat_id = Column(String, nullable=True)
    user_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default='На модерации')
    moderator_comment = Column(Text, nullable=True)


class AnalysisLog(Base):
    __tablename__ = "analysis_logs"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # место хранения JSON ответа от YandexGPT
    analysis_result = Column(Text, nullable=True)


class AdminUser(Base):
    __tablename__ = "admin_user"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=True)
    user_chat_id = Column(Integer, nullable=True)