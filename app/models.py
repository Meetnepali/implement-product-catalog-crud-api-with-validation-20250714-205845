from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.dialects.postgresql import JSONB
import datetime

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    event_type = Column(String(32), nullable=False, index=True)
    description = Column(String(255))
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), default=datetime.datetime.utcnow)
