import json
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from google import genai
from google.genai import types
from fastapi import HTTPException, status

from app.config import settings
from app.schemas.ai import ParsedTodo

client = genai.Client(api_key=settings.gemini_api_key)

SYSTEM_INSTRUCTION = """You convert a short task description into structured JSON.

The user's current date and time is: {now}
The user's timezone is: {tz}

All relative dates and times in the task description (e.g. "tomorrow", "next Monday", "4 PM", "in 2 hours") refer to THIS timezone, not UTC.

Return ONLY a JSON object, no markdown, no explanation, with exactly these keys:
- title (string, required, short and actionable, with date/time/priority words removed)
- description (string or null, extra detail not already in the title)
- due_date (string or null, ISO 8601 WITH the correct UTC offset for the user's timezone, resolved precisely from any relative date/time mentioned)
- priority (string or null, one of "low", "medium", "high")

If no due date is mentioned, due_date must be null. If no priority is implied, priority must be null.
Be precise with times: "4 PM" means 16:00 in the user's local timezone, not UTC, not a different hour."""


def parse_task(raw_text: str, tz_name: str = "Asia/Kolkata") -> ParsedTodo:
    try:
        tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError:
        tz = ZoneInfo("Asia/Kolkata")

    now = datetime.now(tz).isoformat()
    prompt = f"{SYSTEM_INSTRUCTION.format(now=now, tz=tz_name)}\n\nTask description: \"{raw_text}\""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                response_mime_type="application/json",
            ),
        )
        raw = response.text.strip()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="AI service is unavailable right now"
        )

    raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()

    try:
        data = json.loads(raw)
        return ParsedTodo(**data)
    except (json.JSONDecodeError, TypeError, ValueError):
        return ParsedTodo(title=raw_text, description=None, due_date=None, priority=None)