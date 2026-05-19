from controllers.database import get_db
from controllers.models import User, Player, Tournament, Team, TournamentPlayer, Match, Innings, Delivery, MatchState
from controllers.auth import get_current_user
from controllers.schemas import Player as PlayerSchema, Team as TeamSchema, TournamentResponse, TournamentCreate

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

router = APIRouter(prefix="/api", tags=["api"])



# ────────────────────────────────────────────────────────────── 
# TOURNAMENT ROUTES
# ──────────────────────────────────────────────────────────────

@router.get('/tournaments')
def get_tournaments(currentUser : User = Depends(get_current_user), db : Session = Depends(get_db)):
    active_tournaments = db.query(Tournament).filter(Tournament.created_by == currentUser.id, Tournament.status == 'ongoing').all()
    upcoming_tournaments = db.query(Tournament).filter(Tournament.created_by == currentUser.id,Tournament.status.in_(['draft', 'auction'])).all()    
    return {
        "active": active_tournaments,
        "active_count": len(active_tournaments),
        "upcoming": upcoming_tournaments,
        "upcoming_count": len(upcoming_tournaments)
    }

@router.get('/tournaments/{tournament_id}', response_model=TournamentResponse)
def get_tournament(tournament_id: UUID, currentUser : User = Depends(get_current_user), db : Session = Depends(get_db)):
    tournament = db.query(Tournament).filter(Tournament.id == tournament_id, Tournament.created_by == currentUser.id).first()
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return tournament

@router.post('/tournaments/create')
def create_tournament(tournament_data : TournamentCreate, currentUser : User = Depends(get_current_user), db : Session = Depends(get_db)):
    tournament = Tournament(
        name=tournament_data.name,
        created_by=currentUser.id,
        season_year=tournament_data.season_year,
        status=tournament_data.status,
        team_purse=tournament_data.team_purse  # default purse
    )
    db.add(tournament)
    db.commit()
    db.refresh(tournament)
    return {
        "message": "Tournament created successfully", 
        "tournament_id": tournament.id
    }
    
# ────────────────────────────────────────────────────────────── 
# MATCHES API
# ──────────────────────────────────────────────────────────────

@router.get('/matches/live')
def get_live_matches(currentUser : User = Depends(get_current_user), db : Session = Depends(get_db)):
    live_matches = db.query(Match).filter(Match.status == "live").all()
    my_live_matches = [match for match in live_matches if match.tournament_id in [t.id for t in db.query(Tournament).filter(Tournament.created_by == currentUser.id).all()]]
    return {
        "live_matches": my_live_matches,
        "count": len(my_live_matches)
    }
    

# ──────────────────────────────────────────────────────────────
# PLAYERS API
# ──────────────────────────────────────────────────────────────

@router.get('/players')
def get_players(currentUser : User = Depends(get_current_user), db : Session = Depends(get_db)):
    players = db.query(Player).filter(Player.created_by == currentUser.id).all()
    return {
        "players": players,
        "count": len(players)
    }

