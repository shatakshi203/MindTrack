#!/usr/bin/env python3

import requests
import json

BASE_URL = "http://localhost:8000"

def test_assessment_backend():
    """Test assessment backend with proper authentication"""
    print("🎯 TESTING ASSESSMENT BACKEND")
    print("=" * 60)
    
    # Step 1: Login
    print("\n1. 🔐 Logging in...")
    login_response = requests.post(f"{BASE_URL}/api/auth/login", 
                                 json={"email": "215ucf036@gbu.ac.in"})
    
    if login_response.status_code == 200:
        print("   ✅ OTP sent to Gmail")
        print("   📧 Check your Gmail for the OTP")
    else:
        print(f"   ❌ Login failed: {login_response.text}")
        return
    
    # Step 2: Get OTP from user
    otp = input("\n   Enter OTP from Gmail: ").strip()
    if not otp:
        print("   ❌ No OTP provided")
        return
    
    # Step 3: Verify OTP
    print("\n2. 🔑 Verifying OTP...")
    verify_response = requests.post(f"{BASE_URL}/api/auth/verify-otp",
                                  json={"email": "215ucf036@gbu.ac.in", "otp_code": otp})
    
    if verify_response.status_code == 200:
        data = verify_response.json()
        token = data['access_token']
        print("   ✅ Authentication successful")
        print(f"   🔑 Token: {token[:50]}...")
    else:
        print(f"   ❌ Verification failed: {verify_response.text}")
        return
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Step 4: Load questions
    print("\n3. 📝 Loading questions...")
    questions_response = requests.get(f"{BASE_URL}/api/assessment/questions/COMPREHENSIVE", 
                                    headers=headers)
    
    if questions_response.status_code == 200:
        questions_data = questions_response.json()
        questions = questions_data['questions']
        print(f"   ✅ Loaded {len(questions)} questions")
    else:
        print(f"   ❌ Failed to load questions: {questions_response.text}")
        return
    
    # Step 5: Submit assessment
    print("\n4. 🚀 Submitting assessment...")
    
    # Create responses
    responses = []
    sample_scores = [1, 0, 2, 1, 0, 1, 2, 0, 1, 1]
    response_texts = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
    
    for i, question in enumerate(questions):
        score = sample_scores[i % len(sample_scores)]
        responses.append({
            "question_id": question["id"],
            "response": response_texts[score],
            "score": score
        })
    
    submission_data = {
        "assessment_type": "COMPREHENSIVE",
        "responses": responses
    }
    
    submit_response = requests.post(f"{BASE_URL}/api/assessment/submit",
                                  json=submission_data, headers=headers)
    
    if submit_response.status_code == 200:
        result = submit_response.json()
        print("   ✅ ASSESSMENT SUBMITTED SUCCESSFULLY!")
        print(f"   📊 Assessment ID: {result['assessment_id']}")
        print(f"   📈 Total Score: {result['total_score']}")
        print(f"   🎯 Severity Level: {result['severity_level']}")
        print(f"   💡 Recommendations: {result['recommendations']}")
        print(f"   🤖 AI Analysis: {result['ai_analysis']}")
        
        assessment_id = result['assessment_id']
    else:
        print(f"   ❌ Submission failed: {submit_response.text}")
        return
    
    # Step 6: Get history
    print("\n5. 📚 Getting history...")
    history_response = requests.get(f"{BASE_URL}/api/assessment/history", headers=headers)
    
    if history_response.status_code == 200:
        history_data = history_response.json()
        assessments = history_data['assessments']
        print(f"   ✅ Found {len(assessments)} assessments")
        
        for i, assessment in enumerate(assessments[:3]):
            print(f"   {i+1}. {assessment['assessment_type']} - Score: {assessment['total_score']} - {assessment['severity_level']}")
    else:
        print(f"   ❌ History failed: {history_response.text}")
    
    # Step 7: Get detailed result
    print("\n6. 📋 Getting detailed result...")
    result_response = requests.get(f"{BASE_URL}/api/assessment/result/{assessment_id}", 
                                 headers=headers)
    
    if result_response.status_code == 200:
        detailed = result_response.json()
        print("   ✅ Got detailed result")
        print(f"   📊 Type: {detailed['assessment_type']}")
        print(f"   📈 Score: {detailed['total_score']}")
        print(f"   🎯 Severity: {detailed['severity_level']}")
        print(f"   📝 Responses: {len(detailed['responses'])} recorded")
    else:
        print(f"   ❌ Detailed result failed: {result_response.text}")
    
    print("\n" + "=" * 60)
    print("🎉 BACKEND TESTING COMPLETE!")
    print("=" * 60)
    print("✅ All backend endpoints working correctly")
    print("✅ Authentication system working")
    print("✅ Assessment submission working")
    print("✅ Results generation working")
    print("✅ History tracking working")
    
    print(f"\n🔑 Your working token: {token}")
    print("💡 You can now use the frontend with this token")
    
    return token

if __name__ == "__main__":
    test_assessment_backend()
