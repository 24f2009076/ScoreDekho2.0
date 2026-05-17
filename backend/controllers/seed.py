from sqlalchemy import text

from controllers.database import engine, Base, SessionLocal
from controllers.models import User
from controllers.auth import hash_password


def seed_database():
    print("🔄 Connecting to Supabase, dropping old tables, and creating clean ones...")
    # Recreate the schema so stale tables / foreign keys from older models do not block seeding.
    with engine.begin() as connection:
        connection.execute(text("DROP SCHEMA IF EXISTS public CASCADE"))
        connection.execute(text("CREATE SCHEMA public"))

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        print("✅ Database tables successfully built and initialized (Empty)!")
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        db.rollback()
    finally:
        db.close()

def seed_users():
    db = SessionLocal()
    try:
        if db.query(User).first():
            print("Users already seeded.")
            return

        users = [
            User(email="admin@example.com", full_name="Admin User", password_hash=hash_password("admin123")),
            User(email="alice@example.com", full_name="Alice Doe", password_hash=hash_password("alice123")),
        ]
        db.add_all(users)
        db.commit()
        print("Seeded users successfully.")
    finally:
        db.close()
        
if __name__ == '__main__':
    seed_database()