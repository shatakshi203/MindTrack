#!/usr/bin/env python3

import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

def debug_database_path():
    """Debug the database path issue"""
    try:
        print("=== DATABASE PATH DEBUG ===")
        
        from app.database import DATABASE_URL, engine
        print(f"Database URL: {DATABASE_URL}")
        
        # Extract the actual file path
        if DATABASE_URL.startswith("sqlite:///"):
            db_file_path = DATABASE_URL[10:]  # Remove "sqlite:///"
            print(f"Database file path: {db_file_path}")
            print(f"Database file exists: {os.path.exists(db_file_path)}")
            
            if os.path.exists(db_file_path):
                print(f"Database file size: {os.path.getsize(db_file_path)} bytes")
            
        # Check current working directory
        print(f"Current working directory: {os.getcwd()}")
        
        # Check for database files in different locations
        possible_paths = [
            "mindtrack.db",
            "backend/mindtrack.db",
            "./mindtrack.db",
            "./backend/mindtrack.db"
        ]
        
        print("\nChecking for database files:")
        for path in possible_paths:
            exists = os.path.exists(path)
            size = os.path.getsize(path) if exists else 0
            print(f"  {path}: {'EXISTS' if exists else 'NOT FOUND'} ({size} bytes)")
        
        # Test SQLAlchemy connection
        from sqlalchemy.orm import sessionmaker
        from app.models.assessment import AssessmentQuestion
        
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        questions = db.query(AssessmentQuestion).all()
        print(f"\nSQLAlchemy query result: {len(questions)} questions")
        
        db.close()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_database_path()
