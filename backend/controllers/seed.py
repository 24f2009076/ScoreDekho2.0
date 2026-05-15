from backend.controllers.database import engine, Base, SessionLocal
import backend.controllers.models as models

def seed_database():
    print("🔄 Connecting to Supabase, dropping old tables, and creating clean ones...")
    # This safely communicates our models.py structure directly to Supabase
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # === MOCK DATA INSERTION COMMENTED OUT ===
        print("🏏 Adding initial KMDA Teams...")
        team1 = models.Team(name="KMDA Warriors", budget=100000)
        team2 = models.Team(name="Stadium Titans", budget=100000)
        db.add_all([team1, team2])
        db.commit() # Commit to generate IDs for relationships

        print("🏃 Adding initial Players for the Auction...")
        player1 = models.Player(name="Amit Sharma", role="Batsman", base_price=15000, team_id=team1.id, is_sold=True)
        player2 = models.Player(name="Rohit Verma", role="Bowler", base_price=12000)
        player3 = models.Player(name="Vikram Singh", role="All-Rounder", base_price=20000)
        db.add_all([player1, player2, player3])
        db.commit()
        # =========================================
        
        print("✅ Database tables successfully built and initialized (Empty)!")
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        db.rollback()
    finally:
        db.close()
        
if __name__ == '__main__':
    seed_database()