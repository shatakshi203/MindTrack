#!/usr/bin/env python3

import sqlite3
import sys
import os

def check_user_registration():
    """Check if user is registered in the database"""
    try:
        conn = sqlite3.connect('mindtrack.db')
        cursor = conn.cursor()
        
        print("🔍 CHECKING USER REGISTRATION")
        print("=" * 50)
        
        # Check all users
        cursor.execute("SELECT id, email, full_name, student_id, is_verified, created_at FROM users")
        users = cursor.fetchall()
        
        print(f"📊 Total users in database: {len(users)}")
        print("\n👥 All registered users:")
        for user in users:
            print(f"   ID: {user[0]}")
            print(f"   Email: {user[1]}")
            print(f"   Name: {user[2]}")
            print(f"   Student ID: {user[3]}")
            print(f"   Verified: {user[4]}")
            print(f"   Created: {user[5]}")
            print("   " + "-" * 40)
        
        # Check specific user
        target_email = "215ucf036@gbu.ac.in"
        cursor.execute("SELECT * FROM users WHERE email = ?", (target_email,))
        target_user = cursor.fetchone()
        
        print(f"\n🎯 Checking specific user: {target_email}")
        if target_user:
            print("   ✅ User found in database!")
            print(f"   📧 Email: {target_user[1]}")
            print(f"   👤 Name: {target_user[2]}")
            print(f"   🆔 Student ID: {target_user[3]}")
            print(f"   ✅ Verified: {target_user[7]}")
            print(f"   📅 Created: {target_user[8]}")
        else:
            print("   ❌ User NOT found in database!")
            print("   💡 User needs to register first")
        
        # Check OTP records
        cursor.execute("SELECT email, otp_code, expires_at, created_at FROM otp_verifications ORDER BY created_at DESC LIMIT 10")
        otps = cursor.fetchall()
        
        print(f"\n🔐 Recent OTP records ({len(otps)}):")
        for otp in otps:
            print(f"   📧 {otp[0]} → OTP: {otp[1]} (Expires: {otp[2]})")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

def test_registration_api():
    """Test registration API for the specific user"""
    import requests
    
    print("\n🧪 TESTING REGISTRATION API")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    
    # Test registration
    user_data = {
        "email": "215ucf036@gbu.ac.in",
        "full_name": "Student User",
        "student_id": "215UCF036",
        "department": "Computer Science",
        "year_of_study": 4,
        "phone": "1234567890"
    }
    
    try:
        response = requests.post(f"{base_url}/api/auth/register", json=user_data)
        print(f"📝 Registration Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: {data.get('message')}")
            print(f"   🆔 User ID: {data.get('user_id')}")
            print("   📧 Check server terminal for OTP")
        elif response.status_code == 400:
            error_data = response.json()
            print(f"   ⚠️ Registration issue: {error_data.get('detail')}")
            if "already exists" in error_data.get('detail', ''):
                print("   💡 User already registered, try login instead")
        else:
            print(f"   ❌ Error: {response.text}")
            
    except Exception as e:
        print(f"   ❌ API Error: {e}")

def test_login_api():
    """Test login API for the specific user"""
    import requests
    
    print("\n🔑 TESTING LOGIN API")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    
    login_data = {
        "email": "215ucf036@gbu.ac.in"
    }
    
    try:
        response = requests.post(f"{base_url}/api/auth/login", json=login_data)
        print(f"🔐 Login Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: {data.get('message')}")
            print("   📧 Check server terminal for OTP")
        elif response.status_code == 404:
            error_data = response.json()
            print(f"   ❌ User not found: {error_data.get('detail')}")
            print("   💡 User needs to register first")
        else:
            print(f"   ❌ Error: {response.text}")
            
    except Exception as e:
        print(f"   ❌ API Error: {e}")

if __name__ == "__main__":
    check_user_registration()
    test_registration_api()
    test_login_api()
    
    print("\n" + "=" * 50)
    print("📋 SUMMARY & NEXT STEPS")
    print("=" * 50)
    print("1. Check if user exists in database above")
    print("2. If not found, registration should work")
    print("3. If registration fails, check error message")
    print("4. After registration, use OTP from server terminal")
    print("5. Complete OTP verification to get access token")
