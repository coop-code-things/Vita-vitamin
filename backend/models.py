# backend/models.py

from sqlalchemy import Column, String, Integer, Float, JSON, Text, TIMESTAMP, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class UserSession(Base):
    __tablename__ = "user_sessions"

    id = Column(String, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    name = Column(Text)
    age = Column(Integer)
    sex = Column(Text)
    weight_kg = Column(Float)
    height_cm = Column(Float)
    diet_type = Column(Text)
    food_allergies = Column(ARRAY(Text))
    activity_level = Column(Text)
    sleep_hours = Column(Float)
    smoking = Column(JSON)
    alcohol = Column(Text)
    goals = Column(ARRAY(Text))
    symptoms = Column(ARRAY(Text))
    current_stack = Column(ARRAY(Text))
    urgency = Column(Text)
