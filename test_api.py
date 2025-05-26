#!/usr/bin/env python3

import requests

def test_assessment_api():
    """Test the assessment API directly"""
    base_url = "http://localhost:8000"
    
    print("Testing assessment API endpoints...")
    
    # Test PHQ-9 questions
    try:
        response = requests.get(f"{base_url}/api/assessment/questions/PHQ-9")
        print(f"PHQ-9 Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"PHQ-9 Questions: {len(data['questions'])}")
        else:
            print(f"PHQ-9 Error: {response.text}")
    except Exception as e:
        print(f"PHQ-9 Exception: {e}")
    
    # Test GAD-7 questions
    try:
        response = requests.get(f"{base_url}/api/assessment/questions/GAD-7")
        print(f"GAD-7 Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"GAD-7 Questions: {len(data['questions'])}")
        else:
            print(f"GAD-7 Error: {response.text}")
    except Exception as e:
        print(f"GAD-7 Exception: {e}")
    
    # Test COMPREHENSIVE questions
    try:
        response = requests.get(f"{base_url}/api/assessment/questions/COMPREHENSIVE")
        print(f"COMPREHENSIVE Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"COMPREHENSIVE Questions: {len(data['questions'])}")
        else:
            print(f"COMPREHENSIVE Error: {response.text}")
    except Exception as e:
        print(f"COMPREHENSIVE Exception: {e}")

if __name__ == "__main__":
    test_assessment_api()
