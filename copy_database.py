#!/usr/bin/env python3

import sqlite3
import shutil
import os

def copy_database():
    """Copy the database with data to the location SQLAlchemy is using"""
    try:
        source_db = "backend/mindtrack.db"
        target_db = "mindtrack.db"
        
        print(f"Copying database from {source_db} to {target_db}")
        
        if os.path.exists(source_db):
            # Backup the target if it exists
            if os.path.exists(target_db):
                backup_name = f"{target_db}.backup"
                shutil.copy2(target_db, backup_name)
                print(f"Backed up existing database to {backup_name}")
            
            # Copy the source to target
            shutil.copy2(source_db, target_db)
            print("✅ Database copied successfully!")
            
            # Verify the copy
            source_size = os.path.getsize(source_db)
            target_size = os.path.getsize(target_db)
            print(f"Source size: {source_size} bytes")
            print(f"Target size: {target_size} bytes")
            
            if source_size == target_size:
                print("✅ File sizes match - copy successful!")
            else:
                print("❌ File sizes don't match - copy may have failed!")
            
            # Test the data
            conn = sqlite3.connect(target_db)
            cursor = conn.cursor()
            cursor.execute("SELECT assessment_type, COUNT(*) FROM assessment_questions GROUP BY assessment_type")
            counts = cursor.fetchall()
            print(f"Questions in target database: {counts}")
            conn.close()
            
        else:
            print(f"❌ Source database {source_db} not found!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    copy_database()
