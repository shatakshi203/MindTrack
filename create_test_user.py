#!/usr/bin/env python3

import requests
import json

BASE_URL = "http://localhost:8000"

def create_test_user():
    """Create a test user"""
    print("👤 Creating test user...")
    
    user_data = {
        "email": "test@mindtrack.com",
        "password": "testpass123",
        "full_name": "Test User",
        "student_id": "TEST001",
        "phone": "1234567890",
        "emergency_contact": "Emergency Contact",
        "emergency_phone": "0987654321"
    }
    
    response = requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
    
    if response.status_code == 200:
        print("✅ Test user created successfully!")
        return True
    else:
        print(f"❌ User creation failed: {response.status_code} - {response.text}")
        return False

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
        return data.get("access_token")
    else:
        print(f"❌ Login failed: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    create_test_user()
    token = test_login()
    if token:
        print(f"🎉 Authentication working! Token: {token[:20]}...")
