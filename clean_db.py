import sqlite3

# Connect to database
conn = sqlite3.connect('backend/mindtrack.db')
cursor = conn.cursor()

print("Before cleanup:")
cursor.execute('SELECT assessment_type, COUNT(*) FROM assessment_questions GROUP BY assessment_type')
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} questions")

# Delete all questions first
cursor.execute('DELETE FROM assessment_questions')

# Insert the correct questions
comprehensive_questions = [
    ('COMPREHENSIVE', 'Over the last 2 weeks, how often have you been bothered by feeling nervous, anxious, or on edge?', 1),
    ('COMPREHENSIVE', 'Over the last 2 weeks, how often have you felt little interest or pleasure in doing things?', 2),
    ('COMPREHENSIVE', 'How often have you had trouble falling or staying asleep, or sleeping too much?', 3),
    ('COMPREHENSIVE', 'How often have you felt tired or had little energy?', 4),
    ('COMPREHENSIVE', 'How often have you felt bad about yourself — or that you are a failure or have let yourself or your family down?', 5),
    ('COMPREHENSIVE', 'How often have you had trouble concentrating on things, such as reading or watching television?', 6),
    ('COMPREHENSIVE', 'How often have you moved or spoken so slowly that other people noticed? Or the opposite – being restless or fidgety?', 7),
    ('COMPREHENSIVE', 'How often have you felt afraid, as if something awful might happen?', 8),
    ('COMPREHENSIVE', 'Do you currently feel overwhelmed or unable to manage academic or personal responsibilities?', 9),
    ('COMPREHENSIVE', 'Have you ever had thoughts of self-harm or that you would be better off dead?', 10)
]

gad7_questions = [
    ('GAD-7', 'Feeling nervous, anxious, or on edge', 1),
    ('GAD-7', 'Not being able to stop or control worrying', 2),
    ('GAD-7', 'Worrying too much about different things', 3),
    ('GAD-7', 'Trouble relaxing', 4),
    ('GAD-7', 'Being so restless that it is hard to sit still', 5),
    ('GAD-7', 'Becoming easily annoyed or irritable', 6),
    ('GAD-7', 'Feeling afraid, as if something awful might happen', 7)
]

options_json = '''[
    {"text": "Not at all", "score": 0},
    {"text": "Several days", "score": 1},
    {"text": "More than half the days", "score": 2},
    {"text": "Nearly every day", "score": 3}
]'''

# Insert COMPREHENSIVE questions
for q_type, q_text, q_order in comprehensive_questions:
    cursor.execute(
        'INSERT INTO assessment_questions (assessment_type, question_text, question_order, options, is_active) VALUES (?, ?, ?, ?, 1)',
        (q_type, q_text, q_order, options_json)
    )

# Insert GAD-7 questions
for q_type, q_text, q_order in gad7_questions:
    cursor.execute(
        'INSERT INTO assessment_questions (assessment_type, question_text, question_order, options, is_active) VALUES (?, ?, ?, ?, 1)',
        (q_type, q_text, q_order, options_json)
    )

conn.commit()

print("\nAfter cleanup:")
cursor.execute('SELECT assessment_type, COUNT(*) FROM assessment_questions GROUP BY assessment_type')
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} questions")

conn.close()
print("\n✅ Database cleaned up successfully!")
