import sqlite3

# Connect to database
conn = sqlite3.connect('backend/mindtrack.db')
cursor = conn.cursor()

# PHQ-9 questions
phq9_questions = [
    ('PHQ-9', 'Little interest or pleasure in doing things', 1),
    ('PHQ-9', 'Feeling down, depressed, or hopeless', 2),
    ('PHQ-9', 'Trouble falling or staying asleep, or sleeping too much', 3),
    ('PHQ-9', 'Feeling tired or having little energy', 4),
    ('PHQ-9', 'Poor appetite or overeating', 5),
    ('PHQ-9', 'Feeling bad about yourself or that you are a failure or have let yourself or your family down', 6),
    ('PHQ-9', 'Trouble concentrating on things, such as reading the newspaper or watching television', 7),
    ('PHQ-9', 'Moving or speaking so slowly that other people could have noticed, or being so fidgety or restless that you have been moving around a lot more than usual', 8),
    ('PHQ-9', 'Thoughts that you would be better off dead, or thoughts of hurting yourself in some way', 9)
]

options_json = '''[
    {"text": "Not at all", "score": 0},
    {"text": "Several days", "score": 1},
    {"text": "More than half the days", "score": 2},
    {"text": "Nearly every day", "score": 3}
]'''

print("Adding PHQ-9 questions...")

# Insert PHQ-9 questions
for q_type, q_text, q_order in phq9_questions:
    cursor.execute(
        'INSERT OR IGNORE INTO assessment_questions (assessment_type, question_text, question_order, options, is_active) VALUES (?, ?, ?, ?, 1)',
        (q_type, q_text, q_order, options_json)
    )

conn.commit()

print("Checking question counts:")
cursor.execute('SELECT assessment_type, COUNT(*) FROM assessment_questions GROUP BY assessment_type')
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} questions")

conn.close()
print("\n✅ PHQ-9 questions added successfully!")
