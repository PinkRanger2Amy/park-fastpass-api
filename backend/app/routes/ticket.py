from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.ticket import Ride, FastPass, FastPassTier
from schemas.ticket import RideCreate, RideUpdate, RideResponse, FastPassCreate, FastPassUpdate, FastPassResponse, FastPassCheckIn, FastPassCheckInResponse
from datetime import datetime

router = APIRouter(prefix="/api", tags=["fastpass"])

# ===== RIDES MANAGEMENT =====

@router.get("/rides", response_model=list[RideResponse])
async def list_rides(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all available rides in the park."""
    rides = db.query(Ride).offset(skip).limit(limit).all()
    return rides

@router.get("/rides/{ride_id}", response_model=RideResponse)
async def get_ride(ride_id: int, db: Session = Depends(get_db)):
    """Get details of a specific ride."""
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    return ride

@router.post("/rides", response_model=RideResponse, status_code=status.HTTP_201_CREATED)
async def create_ride(ride: RideCreate, db: Session = Depends(get_db)):
    """Create a new ride."""
    db_ride = Ride(**ride.dict())
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

@router.put("/rides/{ride_id}", response_model=RideResponse)
async def update_ride(ride_id: int, ride: RideUpdate, db: Session = Depends(get_db)):
    """Update a ride's information."""
    db_ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if not db_ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    
    update_data = ride.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_ride, field, value)
    
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

# ===== FASTPASS MANAGEMENT =====

@router.get("/fastpasses", response_model=list[FastPassResponse])
async def list_fastpasses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all fast passes."""
    fastpasses = db.query(FastPass).offset(skip).limit(limit).all()
    return fastpasses

@router.get("/fastpasses/{fastpass_id}", response_model=FastPassResponse)
async def get_fastpass(fastpass_id: int, db: Session = Depends(get_db)):
    """Get details of a specific fast pass."""
    fastpass = db.query(FastPass).filter(FastPass.id == fastpass_id).first()
    if not fastpass:
        raise HTTPException(status_code=404, detail="Fast pass not found")
    return fastpass

@router.post("/fastpasses", response_model=FastPassResponse, status_code=status.HTTP_201_CREATED)
async def purchase_fastpass(fastpass: FastPassCreate, db: Session = Depends(get_db)):
    """Purchase a new fast pass for a ride."""
    # Verify ride exists
    ride = db.query(Ride).filter(Ride.id == fastpass.ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    
    # Check validity dates
    if fastpass.valid_from >= fastpass.valid_until:
        raise HTTPException(status_code=400, detail="Valid from date must be before valid until date")
    
    db_fastpass = FastPass(**fastpass.dict())
    db.add(db_fastpass)
    db.commit()
    db.refresh(db_fastpass)
    return db_fastpass

@router.get("/fastpasses/visitor/{visitor_email}", response_model=list[FastPassResponse])
async def get_visitor_fastpasses(visitor_email: str, db: Session = Depends(get_db)):
    """Get all fast passes for a visitor by email."""
    fastpasses = db.query(FastPass).filter(FastPass.visitor_email == visitor_email).all()
    if not fastpasses:
        raise HTTPException(status_code=404, detail="No fast passes found for this visitor")
    return fastpasses

@router.post("/fastpasses/{fastpass_id}/checkin", response_model=FastPassCheckInResponse)
async def checkin_fastpass(fastpass_id: int, db: Session = Depends(get_db)):
    """Check in a visitor for a ride using their fast pass."""
    fastpass = db.query(FastPass).filter(FastPass.id == fastpass_id).first()
    if not fastpass:
        raise HTTPException(status_code=404, detail="Fast pass not found")
    
    # Check if active
    if not fastpass.is_active:
        raise HTTPException(status_code=400, detail="Fast pass is not active")
    
    # Check validity dates
    now = datetime.utcnow()
    if now < fastpass.valid_from or now > fastpass.valid_until:
        raise HTTPException(status_code=400, detail="Fast pass is outside valid date range")
    
    # Check remaining uses
    if fastpass.times_used >= fastpass.max_uses:
        raise HTTPException(status_code=400, detail="Fast pass has no remaining uses")
    
    # Update usage
    fastpass.times_used += 1
    if fastpass.times_used >= fastpass.max_uses:
        fastpass.is_active = False
    
    db.add(fastpass)
    db.commit()
    db.refresh(fastpass)
    
    return FastPassCheckInResponse(
        success=True,
        message=f"Successfully checked in to ride. {fastpass.max_uses - fastpass.times_used} uses remaining.",
        remaining_uses=fastpass.max_uses - fastpass.times_used,
        fastpass_id=fastpass_id
    )

@router.put("/fastpasses/{fastpass_id}", response_model=FastPassResponse)
async def update_fastpass(fastpass_id: int, fastpass_update: FastPassUpdate, db: Session = Depends(get_db)):
    """Update a fast pass."""
    db_fastpass = db.query(FastPass).filter(FastPass.id == fastpass_id).first()
    if not db_fastpass:
        raise HTTPException(status_code=404, detail="Fast pass not found")
    
    update_data = fastpass_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_fastpass, field, value)
    
    db.add(db_fastpass)
    db.commit()
    db.refresh(db_fastpass)
    return db_fastpass

@router.delete("/fastpasses/{fastpass_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_fastpass(fastpass_id: int, db: Session = Depends(get_db)):
    """Cancel a fast pass."""
    db_fastpass = db.query(FastPass).filter(FastPass.id == fastpass_id).first()
    if not db_fastpass:
        raise HTTPException(status_code=404, detail="Fast pass not found")
    
    db.delete(db_fastpass)
    db.commit()
    return None

