from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from controllers.database import get_db
import controllers.models as models

app = FastAPI(title="ScoreDekho API")

@app.get("/")
def home():
    return {"message": "Welcome to the ScoreDekho API! Explore the endpoints to manage teams and players."}


@app.get("/players")
def get_all_players(db: Session = Depends(get_db)):
    # Query all players from the database
    players = db.query(models.Player).all()
    
    # Format the data cleanly into a list of dictionaries for our Vue frontend
    return [
        {
            "id": p.id,
            "name": p.name,
            "role": p.role,
            "base_price": p.base_price,
            "is_sold": p.is_sold,
            "team_id": p.team_id
        }
        for p in players
    ]