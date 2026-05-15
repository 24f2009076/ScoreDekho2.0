from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from controllers.database import Base

class Team(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    budget = Column(Integer, default=0)
    players = relationship("Player", back_populates="team")
    

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False) # Batsman, Bowler, All-Rounder
    base_price = Column(Integer, default=10000)
    is_sold = Column(Boolean, default=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=True)

    team = relationship("Team", back_populates="players")