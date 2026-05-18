from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    full_name: str

class LoginRequest(BaseModel):
    full_name: str
    password: str
    

# ──────────────────────────────────────────────────────────────
# TOURNAMENT SCHEMAS
# ──────────────────────────────────────────────────────────────

class Player(BaseModel):
    id: UUID
    full_name: str
    phone: str | None
    skill_type: str
    created_by: UserResponse | None
    
    

class Team(BaseModel):
    id: UUID
    name: str
    players: list[Player]

    class Config:
        from_attributes = True

class TournamentResponse(BaseModel):
    id: UUID
    name: str
    created_by_user: UserResponse | None = None
    season_year: str
    status: str
    
    team_purse: int
    
    starts_at: datetime | None = None
    ends_at: datetime | None = None
    
    teams: list[Team]

    class Config:
        from_attributes = True

class TournamentCreate(BaseModel):
    name : str
    season_year : str
    status : str
    
    team_purse : int