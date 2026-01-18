from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional
from enum import Enum

class FastPassTier(str, Enum):
    STANDARD = "standard"
    EXPRESS = "express"
    PREMIUM = "premium"

class RideBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    location: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    min_height: Optional[float] = None
    queue_time: int = Field(default=0, ge=0)
    park_area: Optional[str] = None

class RideCreate(RideBase):
    pass

class RideUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    min_height: Optional[float] = None
    queue_time: Optional[int] = None
    park_area: Optional[str] = None

class RideResponse(RideBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class FastPassBase(BaseModel):
    ride_id: int = Field(..., gt=0)
    visitor_name: str = Field(..., min_length=1, max_length=100)
    visitor_email: EmailStr
    tier: FastPassTier = FastPassTier.STANDARD
    max_uses: int = Field(default=1, ge=1)
    valid_from: datetime
    valid_until: datetime

class FastPassCreate(FastPassBase):
    pass

class FastPassUpdate(BaseModel):
    times_used: Optional[int] = None
    is_active: Optional[bool] = None
    tier: Optional[FastPassTier] = None

class FastPassResponse(FastPassBase):
    id: int
    times_used: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class FastPassCheckIn(BaseModel):
    fastpass_id: int = Field(..., gt=0)

class FastPassCheckInResponse(BaseModel):
    success: bool
    message: str
    remaining_uses: int
    fastpass_id: int

