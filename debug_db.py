#!/usr/bin/env python3

import sqlite3
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

def check_database_structure():
    """Check the database structure and data"""
    try:
        conn = sqlite3.connect('backend/mindtrack.db')
        cursor = conn.cursor()
        
        print("=== DATABASE STRUCTURE CHECK ===")
        
        # Check if tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Tables in database: {[table[0] for table in tables]}")
        
        # Check assessment_questions table structure
        if ('assessment_questions',) in tables:
            print("\n=== ASSESSMENT_QUESTIONS TABLE ===")
            cursor.execute("PRAGMA table_info(assessment_questions);")
            columns = cursor.fetchall()
            print("Columns:")
            for col in columns:
                print(f"  {col[1]} ({col[2]})")
            
            # Check data
            cursor.execute("SELECT assessment_type, COUNT(*) FROM assessment_questions GROUP BY assessment_type;")
            counts = cursor.fetchall()
            print(f"\nData counts: {counts}")
            
            # Check sample data
            cursor.execute("SELECT id, assessment_type, question_text FROM assessment_questions LIMIT 3;")
            samples = cursor.fetchall()
            print("\nSample data:")
            for sample in samples:
                print(f"  ID: {sample[0]}, Type: {sample[1]}, Text: {sample[2][:50]}...")
        
        # Test the exact query used by the API
        print("\n=== API QUERY TEST ===")
        test_types = ['PHQ-9', 'GAD-7', 'COMPREHENSIVE']
        for test_type in test_types:
            cursor.execute(
                "SELECT * FROM assessment_questions WHERE assessment_type = ? ORDER BY question_order",
                (test_type,)
            )
            results = cursor.fetchall()
            print(f"{test_type}: {len(results)} questions found")
            if results:
                print(f"  First question: {results[0]}")
        
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

def test_sqlalchemy_connection():
    """Test SQLAlchemy connection"""
    try:
        print("\n=== SQLALCHEMY CONNECTION TEST ===")
        
        from app.database import get_db, engine
        from app.models.assessment import AssessmentQuestion
        from sqlalchemy.orm import sessionmaker
        
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        # Test the exact query from the API
        questions = db.query(AssessmentQuestion).filter(
            AssessmentQuestion.assessment_type == "PHQ-9"
        ).order_by(AssessmentQuestion.question_order).all()
        
        print(f"SQLAlchemy PHQ-9 questions: {len(questions)}")
        if questions:
            print(f"First question: {questions[0].question_text}")
        
        db.close()
        
    except Exception as e:
        print(f"SQLAlchemy Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_database_structure()
    test_sqlalchemy_connection()
