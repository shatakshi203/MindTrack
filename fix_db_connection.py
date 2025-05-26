#!/usr/bin/env python3

import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

def fix_database_connection():
    """Fix the database connection issue"""
    try:
        print("=== FIXING DATABASE CONNECTION ===")
        
        from app.database import engine, Base
        from app.models.assessment import AssessmentQuestion, MentalHealthAssessment, ChatSession, ChatMessage
        from app.models.user import User
        from sqlalchemy.orm import sessionmaker
        
        # Create all tables
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created successfully")
        
        # Test connection
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        # Test query
        questions = db.query(AssessmentQuestion).all()
        print(f"Total questions found: {len(questions)}")
        
        # Test specific query
        phq9_questions = db.query(AssessmentQuestion).filter(
            AssessmentQuestion.assessment_type == "PHQ-9"
        ).all()
        print(f"PHQ-9 questions: {len(phq9_questions)}")
        
        if phq9_questions:
            print(f"First PHQ-9 question: {phq9_questions[0].question_text}")
        
        db.close()
        print("✅ Database connection working!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_database_connection()
