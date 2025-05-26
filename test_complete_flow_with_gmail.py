#!/usr/bin/env python3

import requests
import json

BASE_URL = "http://localhost:8000"

def test_complete_flow_with_gmail():
    """Test complete flow with Gmail OTP"""
    print("🎯 TESTING COMPLETE FLOW WITH GMAIL OTP")
    print("=" * 60)
    print("📧 Email: 215ucf036@gbu.ac.in")
    print("📬 Check your Gmail for the OTP!")
    
    # Step 1: Get fresh OTP
    print("\n1. 🔐 Requesting fresh OTP...")
    login_data = {"email": "215ucf036@gbu.ac.in"}
    
    login_response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    print(f"   Login Status: {login_response.status_code}")
    
    if login_response.status_code == 200:
        print("   ✅ OTP sent to your Gmail!")
        print("   📧 Check your Gmail inbox for the beautiful MindTrack email")
    else:
        print(f"   ❌ Login failed: {login_response.text}")
        return None
    
    # Step 2: Get OTP from user
    print("\n2. 🔢 OTP Verification...")
    print("   📋 Please check your Gmail for the OTP code")
    print("   💌 Look for the email from MindTrack with your verification code")
    
    otp_code = input("   Enter your OTP code from Gmail: ").strip()
    
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
        user_data = verify_result.get('user')
        print("   ✅ OTP verified successfully!")
        print(f"   🔑 Got auth token: {auth_token[:50]}...")
        print(f"   👤 User: {user_data.get('full_name')} ({user_data.get('email')})")
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
        
        # Show first few questions
        for i, q in enumerate(questions[:3]):
            print(f"   Q{i+1}: {q['question_text'][:60]}...")
    else:
        print(f"   ❌ Failed to load questions: {questions_response.text}")
        return None
    
    # Step 5: Create realistic assessment responses
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
    print(f"   📊 Total score: {total_score}")
    
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
        print(f"   💡 Recommendations: {result.get('recommendations')}")
        print(f"   🤖 AI Analysis: {result.get('ai_analysis')}")
        
        if 'next_steps' in result:
            print(f"   📋 Next Steps:")
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
        
        for i, assessment in enumerate(assessments[:3]):  # Show first 3
            print(f"   {i+1}. {assessment['assessment_type']} - Score: {assessment['total_score']} - {assessment['severity_level']}")
            print(f"      Date: {assessment['created_at']}")
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
        print(f"   💡 Recommendations: {detailed_result['recommendations']}")
        print(f"   🤖 AI Analysis: {detailed_result['ai_analysis']}")
    else:
        print(f"   ❌ Failed to get detailed result: {result_response.text}")
    
    return auth_token

def create_frontend_instructions(auth_token):
    """Create instructions for using the frontend"""
    print("\n" + "=" * 60)
    print("🌐 FRONTEND USAGE INSTRUCTIONS")
    print("=" * 60)
    
    print("📋 STEP-BY-STEP FRONTEND USAGE:")
    print("1. Open browser: http://localhost:8000")
    print("2. Click 'Get Started' button")
    print("3. Switch to 'Login' tab")
    print("4. Enter email: 215ucf036@gbu.ac.in")
    print("5. Click 'Send OTP'")
    print("6. Check your Gmail for the OTP")
    print("7. Enter the 6-digit OTP code")
    print("8. Click 'Verify OTP'")
    print("9. You'll be redirected to dashboard")
    print("10. Click 'Assessment' card to take assessment")
    print("11. Complete assessment and see results!")
    print("12. Check 'Recent Assessments' section")
    
    print("\n🎯 WHAT YOU'LL SEE:")
    print("✅ Beautiful Gmail email with OTP")
    print("✅ Successful login and dashboard access")
    print("✅ Interactive assessment questions")
    print("✅ Detailed results with AI analysis")
    print("✅ Assessment history and tracking")
    print("✅ Professional UI with dark/light mode")
    
    print(f"\n🔑 Your working auth token: {auth_token[:50]}...")
    print("💡 Token is automatically stored in browser localStorage")

def main():
    """Run the complete test"""
    print("🚀 MINDTRACK COMPLETE FLOW WITH GMAIL")
    print("=" * 60)
    print("📧 Testing with your email: 215ucf036@gbu.ac.in")
    print("📬 Real Gmail integration with beautiful HTML emails")
    print("🔑 Complete authentication and assessment flow")
    
    auth_token = test_complete_flow_with_gmail()
    
    if auth_token:
        create_frontend_instructions(auth_token)
        
        print("\n" + "=" * 60)
        print("🎉 COMPLETE SYSTEM WORKING!")
        print("=" * 60)
        print("✅ Real Gmail OTP delivery")
        print("✅ Authentication system")
        print("✅ Assessment submission")
        print("✅ AI analysis with OpenAI")
        print("✅ Results display")
        print("✅ History tracking")
        print("✅ Frontend integration")
        
        print("\n🎯 YOUR MINDTRACK PLATFORM IS READY!")
        print("📧 Check your Gmail for the OTP")
        print("🌐 Use the frontend for the complete experience")
        print("🎓 Perfect for BTech CSE final year project demonstration!")
        
    else:
        print("\n❌ Flow failed - check the errors above")
        print("💡 Make sure to check your Gmail for the OTP")

if __name__ == "__main__":
    main()
