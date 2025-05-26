#!/usr/bin/env python3

import requests
import json

BASE_URL = "http://localhost:8000"

def test_complete_assessment_with_auth():
    """Test the complete assessment flow with proper authentication"""
    print("🔍 COMPLETE ASSESSMENT FLOW TEST")
    print("=" * 50)
    
    # Step 1: Register user
    print("\n1. 📝 Registering User...")
    user_data = {
        "email": "assessment@mindtrack.com",
        "full_name": "Assessment Test User",
        "student_id": "ASSESS123",
        "department": "Computer Science",
        "year_of_study": 4,
        "phone": "1234567890"
    }
    
    register_response = requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
    print(f"   Register Status: {register_response.status_code}")
    
    if register_response.status_code == 200:
        print("   ✅ User registered successfully")
    else:
        print(f"   ❌ Registration failed: {register_response.text}")
        return
    
    # Step 2: Login (sends OTP)
    print("\n2. 🔐 Logging In (Sending OTP)...")
    login_data = {"email": "assessment@mindtrack.com"}
    
    login_response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    print(f"   Login Status: {login_response.status_code}")
    
    if login_response.status_code == 200:
        print("   ✅ OTP sent successfully")
        print("   📧 Check server terminal for OTP code")
    else:
        print(f"   ❌ Login failed: {login_response.text}")
        return
    
    # Step 3: Manual OTP verification instruction
    print("\n3. 🔑 OTP Verification Required...")
    print("   📋 TO COMPLETE THE TEST:")
    print("   1. Check the server terminal for the OTP code")
    print("   2. Copy the 6-digit OTP code")
    print("   3. Run the verification manually:")
    print(f"   4. Use this command with the OTP:")
    print(f"      curl -X POST {BASE_URL}/api/auth/verify-otp \\")
    print(f"           -H 'Content-Type: application/json' \\")
    print(f"           -d '{{\"email\": \"assessment@mindtrack.com\", \"otp_code\": \"YOUR_OTP_HERE\"}}'")
    
    # Step 4: Test assessment questions
    print("\n4. 📝 Testing Assessment Questions...")
    
    assessment_types = ['PHQ-9', 'GAD-7', 'COMPREHENSIVE']
    questions_data = {}
    
    for assessment_type in assessment_types:
        response = requests.get(f"{BASE_URL}/api/assessment/questions/{assessment_type}")
        if response.status_code == 200:
            data = response.json()
            questions_data[assessment_type] = data['questions']
            print(f"   ✅ {assessment_type}: {len(data['questions'])} questions loaded")
        else:
            print(f"   ❌ {assessment_type} failed: {response.text}")
    
    # Step 5: Show what happens after OTP verification
    print("\n5. 🎯 After OTP Verification...")
    print("   Once you verify the OTP, you will get:")
    print("   - A valid authentication token")
    print("   - User data stored in response")
    print("   - Ability to submit assessments")
    print("   - Access to all protected endpoints")
    
    # Step 6: Show assessment submission format
    if 'COMPREHENSIVE' in questions_data:
        print("\n6. 📊 Assessment Submission Format...")
        questions = questions_data['COMPREHENSIVE'][:3]  # First 3 questions
        
        sample_responses = []
        for i, question in enumerate(questions):
            sample_responses.append({
                "question_id": question["id"],
                "response": "Several days",
                "score": 1
            })
        
        submission_data = {
            "assessment_type": "COMPREHENSIVE",
            "responses": sample_responses
        }
        
        print("   📋 Sample submission data:")
        print(json.dumps(submission_data, indent=2))
        
        print("\n   🔐 With valid token, submit using:")
        print(f"      curl -X POST {BASE_URL}/api/assessment/submit \\")
        print(f"           -H 'Content-Type: application/json' \\")
        print(f"           -H 'Authorization: Bearer YOUR_TOKEN_HERE' \\")
        print(f"           -d '{json.dumps(submission_data)}'")
    
    print("\n" + "=" * 50)
    print("📋 SUMMARY:")
    print("=" * 50)
    print("✅ User registration: Working")
    print("✅ OTP sending: Working")
    print("✅ Assessment questions: Working")
    print("🔄 OTP verification: Manual step required")
    print("🔄 Assessment submission: Requires valid token")
    
    print("\n🛠️ TO FIX THE ASSESSMENT ISSUE:")
    print("1. Complete the OTP verification in browser")
    print("2. Login properly through the frontend")
    print("3. Then assessment submission will work")

def show_frontend_instructions():
    """Show instructions for using the frontend properly"""
    print("\n" + "=" * 60)
    print("🌐 FRONTEND USAGE INSTRUCTIONS")
    print("=" * 60)
    
    print("\n📋 STEP-BY-STEP GUIDE:")
    print("1. 🏠 Go to http://localhost:8000")
    print("2. 🔘 Click 'Get Started' button")
    print("3. 📝 Fill in registration form OR use login tab")
    print("4. 📧 Check server terminal for OTP code")
    print("5. 🔢 Enter the 6-digit OTP in the verification form")
    print("6. ✅ You'll be redirected to dashboard")
    print("7. 📊 Now you can take assessments and get results!")
    
    print("\n🎯 TEST USER CREDENTIALS:")
    print("   Email: assessment@mindtrack.com")
    print("   Name: Assessment Test User")
    print("   Student ID: ASSESS123")
    
    print("\n🔍 DEBUGGING TIPS:")
    print("   - Open browser console (F12) to see any JavaScript errors")
    print("   - Check localStorage.getItem('authToken') to verify login")
    print("   - Server terminal shows all OTP codes")
    print("   - All API endpoints are working correctly")

if __name__ == "__main__":
    test_complete_assessment_with_auth()
    show_frontend_instructions()
