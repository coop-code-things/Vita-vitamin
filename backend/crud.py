# backend/crud.py

import uuid
from models import UserSession
from sqlalchemy.ext.asyncio import AsyncSession

async def insert_user_session(db: AsyncSession, data: dict):
    new_session = UserSession(
        id=str(uuid.uuid4()),
        name=data.get("name"),
        age=data.get("age"),
        sex=data.get("sex"),
        weight_kg=data.get("weight_kg"),
        height_cm=data.get("height_cm"),
        diet_type=data.get("diet_type"),
        food_allergies=data.get("food_allergies"),
        activity_level=data.get("activity_level"),
        sleep_hours=data.get("sleep_hours"),
        smoking=data.get("smoking"),
        alcohol=data.get("alcohol"),
        goals=data.get("goals"),
        symptoms=data.get("symptoms"),
        current_stack=data.get("current_stack"),
        urgency=data.get("urgency")
    )
    db.add(new_session)
    await db.commit()

def format_protocol_prompt(user_data: dict) -> str:
    return f"""
You're a licensed functional medicine nutritionist. Based on the user data below, create a personalized daily vitamin & supplement protocol.

User Profile:
- Name: {user_data['name']}
- Age: {user_data['age']}
- Sex: {user_data['sex']}
- Weight: {user_data['weight_kg']} kg
- Height: {user_data['height_cm']} cm
- Diet Type: {user_data['diet_type']}
- Allergies: {', '.join(user_data['food_allergies'])}
- Activity Level: {user_data['activity_level']}
- Sleep Hours: {user_data['sleep_hours']}
- Smoking: {user_data['smoking']}
- Alcohol Use: {user_data['alcohol']}
- Health Goals: {', '.join(user_data['goals'])}
- Symptoms: {', '.join(user_data['symptoms'])}
- Current Supplements: {', '.join(user_data['current_stack'])}
- Desired Results Timeframe: {user_data['urgency']}

Instructions:
- Use evidence-based suggestions.
- Mention timing (morning/night), dosage (mg/IU), and form (capsule/powder/etc).
- Note any important interactions or cautions.
- Keep it clean, professional, and useful.
"""
