from app.db.session import SessionLocal
from app.db.seeds.initial import seed_initial_data


def run_all_seeds():
    db = SessionLocal()
    try:
        seed_initial_data(db)
        print("Seeding completed successfully.")
    except Exception as e:
        print(f"Seeding failed: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    run_all_seeds()
