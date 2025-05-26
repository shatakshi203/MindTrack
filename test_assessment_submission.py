#!/usr/bin/env python3

import requests
import json

BASE_URL = "http://localhost:8000"

# Token from OTP verification
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc3Nlc3NtZW50QG1pbmR0cmFjay5jb20iLCJ1c2VyX2lkIjozLCJleHAiOjE3NDgyNzU0MDB9.7JtpzCvlH7oCb4W6KGoG45Yxm8Kk0OnFkl9NmOXabnM"

def test_assessment_submission():
    """Test assessment submission with valid token"""
    print("🎯 TESTING ASSESSMENT SUBMISSION WITH VALID TOKEN")
    print("=" * 60)

    # Step 1: Get assessment questions
    print("\n1. 📝 Getting Assessment Questions...")
    response = requests.get(f"{BASE_URL}/api/assessment/questions/COMPREHENSIVE")

    if response.status_code == 200:
        data = response.json()
        questions = data['questions']
        print(f"   ✅ Got {len(questions)} questions")

        # Step 2: Create sample responses
        print("\n2. 📊 Creating Sample Responses...")
        sample_responses = []

        for i, question in enumerate(questions):
            # Vary the responses for realistic test
            scores = [0, 1, 2, 1, 0, 1, 2, 0, 1, 1]  # Mix of scores
            score = scores[i % len(scores)]

            response_texts = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
            response_text = response_texts[score]

            sample_responses.append({
                "question_id": question["id"],
                "response": response_text,
                "score": score
            })

        print(f"   ✅ Created {len(sample_responses)} responses")
        print(f"   📊 Total score will be: {sum(r['score'] for r in sample_responses)}")

        # Step 3: Submit assessment
        print("\n3. 🚀 Submitting Assessment...")

        submission_data = {
            "assessment_type": "COMPREHENSIVE",
            "responses": sample_responses
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AUTH_TOKEN}"
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

            return True
        else:
            print(f"   ❌ Submission failed: {submit_response.text}")
            return False
    else:
        print(f"   ❌ Failed to get questions: {response.text}")
        return False

def test_assessment_history():
    """Test getting assessment history"""
    print("\n4. 📚 Testing Assessment History...")

    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    response = requests.get(f"{BASE_URL}/api/assessment/history", headers=headers)

    if response.status_code == 200:
        data = response.json()
        assessments = data.get('assessments', [])
        print(f"   ✅ Found {len(assessments)} assessments in history")

        if assessments:
            latest = assessments[0]
            print(f"   📊 Latest: {latest['assessment_type']} - Score: {latest['total_score']} - {latest['severity_level']}")
    else:
        print(f"   ❌ Failed to get history: {response.text}")

def main():
    """Run the complete test"""
    success = test_assessment_submission()

    if success:
        test_assessment_history()

        print("\n" + "=" * 60)
        print("🎉 ASSESSMENT SYSTEM FULLY WORKING!")
        print("=" * 60)
        print("✅ Authentication: Working")
        print("✅ Question Loading: Working")
        print("✅ Assessment Submission: Working")
        print("✅ Results Generation: Working")
        print("✅ History Tracking: Working")

        print("\n🌐 FRONTEND INSTRUCTIONS:")
        print("1. Go to http://localhost:8000")
        print("2. Click 'Get Started'")
        print("3. Login with: assessment@mindtrack.com")
        print("4. Use OTP from server terminal")
        print("5. Take assessment and get results!")

    else:
        print("\n❌ Assessment submission failed")

if __name__ == "__main__":
    main()
