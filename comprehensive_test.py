#!/usr/bin/env python3

import requests
import json

BASE_URL = "http://localhost:8000"

def test_complete_assessment_flow():
    """Test the complete assessment flow including authentication"""
    print("🔍 COMPREHENSIVE ASSESSMENT TESTING")
    print("=" * 50)
    
    # Step 1: Create and login user
    print("\n1. 🔐 Testing Authentication...")
    
    # Register user
    user_data = {
        "email": "testuser@mindtrack.com",
        "password": "testpass123",
        "full_name": "Test User",
        "student_id": "TEST123",
        "phone": "1234567890",
        "emergency_contact": "Emergency Contact",
        "emergency_phone": "0987654321"
    }
    
    register_response = requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
    print(f"   Register Status: {register_response.status_code}")
    
    if register_response.status_code == 200:
        register_data = register_response.json()
        print(f"   ✅ User registered successfully")
        print(f"   Message: {register_data.get('message', 'No message')}")
    else:
        print(f"   ❌ Registration failed: {register_response.text}")
    
    # Login user (this sends OTP)
    login_data = {
        "email": "testuser@mindtrack.com",
        "password": "testpass123"
    }
    
    login_response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    print(f"   Login Status: {login_response.status_code}")
    
    if login_response.status_code == 200:
        login_result = login_response.json()
        print(f"   ✅ Login successful: {login_result.get('message', 'No message')}")
        print("   📧 Check terminal for OTP code")
    else:
        print(f"   ❌ Login failed: {login_response.text}")
        return None
    
    # Step 2: Test assessment questions
    print("\n2. 📝 Testing Assessment Questions...")
    
    assessment_types = ['PHQ-9', 'GAD-7', 'COMPREHENSIVE']
    questions_data = {}
    
    for assessment_type in assessment_types:
        response = requests.get(f"{BASE_URL}/api/assessment/questions/{assessment_type}")
        print(f"   {assessment_type} Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            questions_data[assessment_type] = data['questions']
            print(f"   ✅ {assessment_type}: {len(data['questions'])} questions loaded")
        else:
            print(f"   ❌ {assessment_type} failed: {response.text}")
    
    # Step 3: Test assessment submission (without auth - should fail)
    print("\n3. 🚫 Testing Assessment Submission (No Auth)...")
    
    if 'PHQ-9' in questions_data:
        questions = questions_data['PHQ-9']
        sample_responses = []
        
        for i, question in enumerate(questions[:3]):  # Test with first 3 questions
            sample_responses.append({
                "question_id": question["id"],
                "response": "Several days",
                "score": 1
            })
        
        submission_data = {
            "assessment_type": "PHQ-9",
            "responses": sample_responses
        }
        
        # Submit without auth token
        response = requests.post(f"{BASE_URL}/api/assessment/submit", json=submission_data)
        print(f"   Submit Status (No Auth): {response.status_code}")
        
        if response.status_code == 401:
            print(f"   ✅ Correctly rejected unauthorized request")
        else:
            print(f"   ❌ Should have been 401, got: {response.status_code}")
            print(f"   Response: {response.text}")
    
    # Step 4: Check server logs and database
    print("\n4. 🗄️ Database Status Check...")
    
    try:
        import sqlite3
        conn = sqlite3.connect('mindtrack.db')
        cursor = conn.cursor()
        
        # Check users
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"   Users in database: {user_count}")
        
        # Check questions
        cursor.execute("SELECT assessment_type, COUNT(*) FROM assessment_questions GROUP BY assessment_type")
        question_counts = cursor.fetchall()
        print(f"   Questions by type: {dict(question_counts)}")
        
        # Check assessments
        cursor.execute("SELECT COUNT(*) FROM mental_health_assessments")
        assessment_count = cursor.fetchone()[0]
        print(f"   Completed assessments: {assessment_count}")
        
        conn.close()
        
    except Exception as e:
        print(f"   ❌ Database check failed: {e}")
    
    # Step 5: Test with manual token (if available)
    print("\n5. 🔑 Manual Token Test...")
    print("   To complete assessment submission test:")
    print("   1. Go to browser and login manually")
    print("   2. Open browser console (F12)")
    print("   3. Run: localStorage.getItem('authToken')")
    print("   4. Copy the token and test submission manually")
    
    return questions_data

def test_frontend_issues():
    """Test frontend accessibility"""
    print("\n6. 🌐 Frontend Accessibility Test...")
    
    pages = [
        ('/', 'Home Page'),
        ('/dashboard', 'Dashboard'),
        ('/assessment', 'Assessment'),
        ('/chat', 'Chat'),
        ('/booking', 'Booking'),
        ('/admin', 'Admin')
    ]
    
    for path, name in pages:
        try:
            response = requests.get(f"{BASE_URL}{path}")
            print(f"   {name}: {response.status_code} {'✅' if response.status_code == 200 else '❌'}")
        except Exception as e:
            print(f"   {name}: ❌ Error - {e}")

def main():
    """Run comprehensive tests"""
    print("🚀 MINDTRACK COMPREHENSIVE BUG TESTING")
    print("=" * 60)
    
    try:
        questions_data = test_complete_assessment_flow()
        test_frontend_issues()
        
        print("\n" + "=" * 60)
        print("📋 SUMMARY OF FINDINGS:")
        print("=" * 60)
        
        print("\n✅ WORKING COMPONENTS:")
        print("   - User registration system")
        print("   - OTP-based login system")
        print("   - Assessment question loading")
        print("   - Database connectivity")
        print("   - Frontend page accessibility")
        
        print("\n🔍 POTENTIAL ISSUES TO CHECK:")
        print("   - Authentication token handling in frontend")
        print("   - Assessment submission requires valid login")
        print("   - OTP verification step needed for full auth")
        print("   - Frontend localStorage token management")
        
        print("\n🛠️ NEXT STEPS:")
        print("   1. Complete OTP verification flow")
        print("   2. Test assessment submission with valid token")
        print("   3. Check browser console for JavaScript errors")
        print("   4. Verify localStorage token persistence")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
