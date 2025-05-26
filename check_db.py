import sqlite3

# Connect to database
conn = sqlite3.connect('backend/mindtrack.db')
cursor = conn.cursor()

# Check assessment questions
cursor.execute('SELECT assessment_type, COUNT(*) FROM assessment_questions GROUP BY assessment_type')
print("Assessment types and counts:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} questions")

print("\nSample COMPREHENSIVE questions:")
cursor.execute('SELECT question_text FROM assessment_questions WHERE assessment_type = "COMPREHENSIVE" LIMIT 3')
for row in cursor.fetchall():
    print(f"  - {row[0][:80]}...")

print("\nSample GAD-7 questions:")
cursor.execute('SELECT question_text FROM assessment_questions WHERE assessment_type = "GAD-7" LIMIT 3')
for row in cursor.fetchall():
    print(f"  - {row[0][:80]}...")

conn.close()
