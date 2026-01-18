from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Enum
from sqlalchemy.sql import func
from database import Base
import enum

class FastPassTier(str, enum.Enum):
    STANDARD = "standard"
    EXPRESS = "express"
    PREMIUM = "premium"

class Ride(Base):
    __tablename__ = "rides"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    location = Column(String(100), nullable=False)
    description = Column(String(500))
    min_height = Column(Float)
    queue_time = Column(Integer, default=0)  # in minutes
    park_area = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class FastPass(Base):
    __tablename__ = "fastpasses"
    
    id = Column(Integer, primary_key=True, index=True)
    ride_id = Column(Integer, nullable=False, index=True)
    visitor_name = Column(String(100), nullable=False)
    visitor_email = Column(String(100), index=True)
    tier = Column(Enum(FastPassTier), default=FastPassTier.STANDARD)
    times_used = Column(Integer, default=0)
    max_uses = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    valid_from = Column(DateTime(timezone=True), nullable=False)
    valid_until = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

