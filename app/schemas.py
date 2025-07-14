from pydantic import BaseModel, Field, root_validator, validator
from typing import Optional, Dict, Any, List
from datetime import datetime

class Metadata(BaseModel):
    action: Optional[str] = Field(None, max_length=50)
    context: Optional[str] = Field(None, max_length=100)
    class Config:
        extra = "allow"

class EventCreate(BaseModel):
    event_type: str = Field(..., min_length=3, max_length=32, example="login")
    description: Optional[str] = Field(None, max_length=255)
    metadata: Optional[Metadata] = None

    @validator("event_type")
    def validate_event_type(cls, v):
        if not v.isidentifier():
            raise ValueError("event_type must be a valid identifier (letters, underscore, digits), no spaces")
        return v

class EventRead(BaseModel):
    id: int
    user_id: int
    event_type: str
    description: Optional[str]
    metadata: Optional[Dict[str, Any]]
    created_at: datetime

    class Config:
        orm_mode = True

class EventListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: List[EventRead]

class ErrorResponse(BaseModel):
    detail: str