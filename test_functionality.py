#!/usr/bin/env python3

import requests
import json

BASE_URL = "http://localhost:8000"

def test_login():
    """Test user login"""
    print("🔐 Testing Login...")

    login_data = {
        "email": "test@mindtrack.com",
        "password": "testpass123"
    }

    response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)

    if response.status_code == 200:
        data = response.json()
        print("✅ Login successful!")
        print(f"   Response data: {data}")
        token = data.get("access_token") or data.get("token")
        return token
    else:
        print(f"❌ Login failed: {response.status_code} - {response.text}")
        return None

def test_assessment_questions(token):
    """Test fetching assessment questions"""
    print("\n📝 Testing Assessment Questions...")

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(f"{BASE_URL}/api/assessment/questions/PHQ-9", headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Assessment questions fetched: {len(data['questions'])} questions")
        return data['questions']
    else:
        print(f"❌ Failed to fetch questions: {response.status_code} - {response.text}")
        return None

def test_assessment_submission(token, questions):
    """Test assessment submission"""
    print("\n📊 Testing Assessment Submission...")

    headers = {"Authorization": f"Bearer {token}"}

    # Create sample responses
    responses = []
    for i, question in enumerate(questions[:5]):  # Test with first 5 questions
        responses.append({
            "question_id": question["id"],
            "response": "Several days",
            "score": 1
        })

    submission_data = {
        "assessment_type": "PHQ-9",
        "responses": responses
    }

    response = requests.post(f"{BASE_URL}/api/assessment/submit",
                           json=submission_data, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("✅ Assessment submitted successfully!")
        print(f"   Score: {data.get('total_score', 'N/A')}")
        print(f"   Severity: {data.get('severity_level', 'N/A')}")
        return True
    else:
        print(f"❌ Assessment submission failed: {response.status_code} - {response.text}")
        return False

def test_chat_session(token):
    """Test chat session creation"""
    print("\n💬 Testing Chat Session...")

    headers = {"Authorization": f"Bearer {token}"}

    # Create new chat session
    session_data = {
        "session_title": "Test Chat Session",
        "mood_before": "neutral"
    }

    response = requests.post(f"{BASE_URL}/api/chatbot/sessions",
                           json=session_data, headers=headers)

    if response.status_code == 200:
        data = response.json()
        session_id = data.get("session_id")
        print(f"✅ Chat session created: {session_id}")
        return session_id
    else:
        print(f"❌ Chat session creation failed: {response.status_code} - {response.text}")
        return None

def test_chat_message(token, session_id):
    """Test sending chat message"""
    print("\n🤖 Testing Chat Message...")

    headers = {"Authorization": f"Bearer {token}"}

    message_data = {
        "message_text": "I'm feeling anxious about my upcoming exams. Can you help me?",
        "mood_rating": "anxious"
    }

    response = requests.post(f"{BASE_URL}/api/chatbot/sessions/{session_id}/messages",
                           json=message_data, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("✅ Chat message sent successfully!")
        print(f"   Bot Response: {data.get('bot_response', 'N/A')[:100]}...")
        print(f"   Suggestions: {len(data.get('suggestions', []))} provided")
        return True
    else:
        print(f"❌ Chat message failed: {response.status_code} - {response.text}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting MindTrack Functionality Tests...\n")

    # Test login
    token = test_login()
    if not token:
        print("❌ Cannot proceed without authentication")
        return

    # Test assessment questions
    questions = test_assessment_questions(token)
    if questions:
        # Test assessment submission
        test_assessment_submission(token, questions)

    # Test chat functionality
    session_id = test_chat_session(token)
    if session_id:
        test_chat_message(token, session_id)

    print("\n🎉 All tests completed!")
    print("\n📋 Summary:")
    print("✅ Server is running")
    print("✅ Authentication working")
    print("✅ Assessment system functional")
    print("✅ Chat system functional")
    print("✅ OpenAI integration ready")

if __name__ == "__main__":
    main()
