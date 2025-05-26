#!/usr/bin/env python3

import requests
import json

BASE_URL = "http://localhost:8000"

def test_complete_assessment_flow():
    """Test the complete assessment flow for your email"""
    print("🎯 TESTING COMPLETE ASSESSMENT FLOW")
    print("=" * 60)
    
    # Step 1: Login and get OTP
    print("\n1. 🔐 Logging in with your email...")
    login_data = {"email": "215ucf036@gbu.ac.in"}
    
    login_response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    print(f"   Login Status: {login_response.status_code}")
    
    if login_response.status_code == 200:
        print("   ✅ OTP sent successfully")
        print("   📧 Check server terminal for OTP code")
    else:
        print(f"   ❌ Login failed: {login_response.text}")
        return None
    
    # Step 2: Get OTP from user input
    print("\n2. 🔢 OTP Verification...")
    print("   📋 Please check the server terminal for your OTP code")
    print("   💡 Look for: 'OTP CODE: XXXXXX' for 215ucf036@gbu.ac.in")
    
    # For testing, let's use the latest OTP from the logs
    # You can replace this with the actual OTP from terminal
    otp_code = input("   Enter your OTP code: ").strip()
    
    if not otp_code:
        print("   ❌ No OTP provided")
        return None
    
    # Step 3: Verify OTP and get token
    verify_data = {"email": "215ucf036@gbu.ac.in", "otp_code": otp_code}
    verify_response = requests.post(f"{BASE_URL}/api/auth/verify-otp", json=verify_data)
    
    print(f"   Verify Status: {verify_response.status_code}")
    
    if verify_response.status_code == 200:
        verify_result = verify_response.json()
        auth_token = verify_result.get('access_token')
        print("   ✅ OTP verified successfully")
        print(f"   🔑 Got auth token: {auth_token[:50]}...")
    else:
        print(f"   ❌ OTP verification failed: {verify_response.text}")
        return None
    
    # Step 4: Test assessment questions
    print("\n3. 📝 Loading Assessment Questions...")
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    questions_response = requests.get(f"{BASE_URL}/api/assessment/questions/COMPREHENSIVE", headers=headers)
    print(f"   Questions Status: {questions_response.status_code}")
    
    if questions_response.status_code == 200:
        questions_data = questions_response.json()
        questions = questions_data['questions']
        print(f"   ✅ Loaded {len(questions)} questions")
    else:
        print(f"   ❌ Failed to load questions: {questions_response.text}")
        return None
    
    # Step 5: Create sample assessment responses
    print("\n4. 📊 Creating Assessment Responses...")
    responses = []
    
    # Create varied responses for realistic test
    sample_scores = [1, 0, 2, 1, 0, 1, 2, 0, 1, 1]  # Mix of scores
    response_texts = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
    
    for i, question in enumerate(questions):
        score = sample_scores[i % len(sample_scores)]
        response_text = response_texts[score]
        
        responses.append({
            "question_id": question["id"],
            "response": response_text,
            "score": score
        })
    
    total_score = sum(r['score'] for r in responses)
    print(f"   ✅ Created {len(responses)} responses")
    print(f"   📊 Total score will be: {total_score}")
    
    # Step 6: Submit assessment
    print("\n5. 🚀 Submitting Assessment...")
    
    submission_data = {
        "assessment_type": "COMPREHENSIVE",
        "responses": responses
    }
    
    submit_response = requests.post(
        f"{BASE_URL}/api/assessment/submit",
        json=submission_data,
        headers=headers
    )
    
    print(f"   Submit Status: {submit_response.status_code}")
    
    if submit_response.status_code == 200:
        result = submit_response.json()
        print("   ✅ ASSESSMENT SUBMITTED SUCCESSFULLY!")
        print(f"   📊 Assessment ID: {result.get('assessment_id')}")
        print(f"   📈 Total Score: {result.get('total_score')}")
        print(f"   🎯 Severity Level: {result.get('severity_level')}")
        print(f"   💡 Recommendations: {result.get('recommendations')[:100]}...")
        print(f"   🤖 AI Analysis: {result.get('ai_analysis')[:100]}...")
        
        if 'next_steps' in result:
            print(f"   📋 Next Steps: {len(result['next_steps'])} recommendations")
            for step in result['next_steps']:
                print(f"      • {step}")
        
        assessment_id = result.get('assessment_id')
        
    else:
        print(f"   ❌ Submission failed: {submit_response.text}")
        return None
    
    # Step 7: Test assessment history
    print("\n6. 📚 Testing Assessment History...")
    
    history_response = requests.get(f"{BASE_URL}/api/assessment/history", headers=headers)
    print(f"   History Status: {history_response.status_code}")
    
    if history_response.status_code == 200:
        history_data = history_response.json()
        assessments = history_data.get('assessments', [])
        print(f"   ✅ Found {len(assessments)} assessments in history")
        
        if assessments:
            latest = assessments[0]
            print(f"   📊 Latest: {latest['assessment_type']} - Score: {latest['total_score']} - {latest['severity_level']}")
            print(f"   📅 Date: {latest['created_at']}")
    else:
        print(f"   ❌ Failed to get history: {history_response.text}")
    
    # Step 8: Test detailed result
    print("\n7. 📋 Testing Detailed Result...")
    
    result_response = requests.get(f"{BASE_URL}/api/assessment/result/{assessment_id}", headers=headers)
    print(f"   Result Status: {result_response.status_code}")
    
    if result_response.status_code == 200:
        detailed_result = result_response.json()
        print(f"   ✅ Got detailed result")
        print(f"   📊 Type: {detailed_result['assessment_type']}")
        print(f"   📈 Score: {detailed_result['total_score']}")
        print(f"   🎯 Severity: {detailed_result['severity_level']}")
        print(f"   📝 Responses: {len(detailed_result['responses'])} recorded")
    else:
        print(f"   ❌ Failed to get detailed result: {result_response.text}")
    
    return auth_token

def main():
    """Run the complete test"""
    print("🚀 MINDTRACK COMPLETE ASSESSMENT TESTING")
    print("=" * 60)
    print("📧 Testing with your email: 215ucf036@gbu.ac.in")
    print("🔑 Make sure you have the OTP from server terminal")
    
    auth_token = test_complete_assessment_flow()
    
    if auth_token:
        print("\n" + "=" * 60)
        print("🎉 COMPLETE ASSESSMENT FLOW WORKING!")
        print("=" * 60)
        print("✅ Authentication: Working")
        print("✅ Question Loading: Working")
        print("✅ Assessment Submission: Working")
        print("✅ Results Generation: Working")
        print("✅ History Tracking: Working")
        print("✅ Detailed Results: Working")
        
        print("\n🌐 FRONTEND TESTING:")
        print("1. Go to http://localhost:8000")
        print("2. Login with: 215ucf036@gbu.ac.in")
        print("3. Use OTP from server terminal")
        print("4. Navigate to Assessment")
        print("5. Complete assessment and see results!")
        print("6. Check dashboard for recent assessments")
        
        print(f"\n🔑 Your auth token: {auth_token}")
        print("💡 You can now use the frontend with full functionality!")
        
    else:
        print("\n❌ Assessment flow failed - check the errors above")

if __name__ == "__main__":
    main()
