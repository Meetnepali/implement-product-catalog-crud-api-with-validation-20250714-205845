from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import EventCreate, EventRead, EventListResponse, ErrorResponse
from app.db import get_db_session
from app.models import Event
from app.auth import get_current_user
from sqlalchemy.future import select
from sqlalchemy import desc
from typing import Optional

router = APIRouter()

@router.post("/", response_model=EventRead, responses={400: {"model": ErrorResponse}, 401: {"model": ErrorResponse}})
async def log_event(
    payload: EventCreate,
    db: AsyncSession = Depends(get_db_session),
    user_id: int = Depends(get_current_user)
):
    event = Event(
        user_id=user_id,
        event_type=payload.event_type,
        description=payload.description,
        metadata=payload.metadata.dict() if payload.metadata else None
    )
    db.add(event)
    try:
        await db.commit()
        await db.refresh(event)
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Could not create event.")
    return EventRead.from_orm(event)

@router.get("/", response_model=EventListResponse, responses={401: {"model": ErrorResponse}})
async def list_events(
    db: AsyncSession = Depends(get_db_session),
    user_id: int = Depends(get_current_user),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    event_type: Optional[str] = Query(None)
):
    stmt = select(Event).where(Event.user_id == user_id)
    if event_type:
        stmt = stmt.where(Event.event_type == event_type)
    stmt = stmt.order_by(desc(Event.created_at))
    total = (await db.execute(select([Event.id]).where(Event.user_id == user_id))).rowcount
    q = await db.execute(stmt.offset((page - 1) * page_size).limit(page_size))
    events = q.scalars().all()
    return EventListResponse(
        total=total if total is not None else 0,
        page=page,
        page_size=page_size,
        items=[EventRead.from_orm(evt) for evt in events]
    )
