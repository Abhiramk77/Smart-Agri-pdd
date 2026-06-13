#!/usr/bin/env python3
"""
Automated App Demo - Interacts with the Farming App
"""

import time
import requests
from urllib.parse import urljoin

BASE_URL = "http://localhost:3000"

def test_api_endpoints():
    """Test various API endpoints"""
    print("\n" + "="*60)
    print("AUTOMATED APP DEMONSTRATION")
    print("="*60)

    endpoints = {
        "GET /api/chats": "/api/chats",
        "GET /api/contracts": "/api/contracts",
        "GET /api/contracts/marketplace": "/api/contracts/marketplace",
        "GET /api/auth/me": "/api/auth/me",
    }

    headers = {"Authorization": "Bearer mock_token_u2"}

    for name, endpoint in endpoints.items():
        print(f"\n[*] Testing: {name}")
        try:
            response = requests.get(urljoin(BASE_URL, endpoint), headers=headers, timeout=5)
            status = response.status_code

            if status == 200:
                print(f"    ✓ Status: {status}")
                if response.text:
                    try:
                        data = response.json()
                        if isinstance(data, list):
                            print(f"    ✓ Returned {len(data)} item(s)")
                        else:
                            print(f"    ✓ Response received")
                    except:
                        print(f"    ✓ Response received (non-JSON)")
            else:
                print(f"    ✗ Status: {status}")
        except Exception as e:
            print(f"    ✗ Error: {str(e)[:50]}")

    # Test login
    print(f"\n[*] Testing: POST /api/auth/login")
    try:
        response = requests.post(
            urljoin(BASE_URL, "/api/auth/login"),
            json={"email": "farmer@farming.com"},
            timeout=5
        )
        if response.status_code == 200:
            print(f"    ✓ Login successful")
            data = response.json()
            if "token" in data:
                print(f"    ✓ Token received: {data['token'][:20]}...")
        else:
            print(f"    ✗ Status: {response.status_code}")
    except Exception as e:
        print(f"    ✗ Error: {str(e)[:50]}")

    # Test signup
    print(f"\n[*] Testing: POST /api/auth/signup")
    try:
        response = requests.post(
            urljoin(BASE_URL, "/api/auth/signup"),
            json={
                "name": "Demo User",
                "email": f"demo_{int(time.time())}@test.com",
                "role": "farmer"
            },
            timeout=5
        )
        if response.status_code in [201, 409]:
            print(f"    ✓ Signup response: {response.status_code}")
        else:
            print(f"    ? Status: {response.status_code}")
    except Exception as e:
        print(f"    ✗ Error: {str(e)[:50]}")

    print("\n" + "="*60)
    print("API TESTING COMPLETE")
    print("="*60 + "\n")

if __name__ == "__main__":
    print("\n[*] Starting automated app demo...")
    time.sleep(2)

    try:
        test_api_endpoints()
        print("[+] Demo completed successfully!")
    except Exception as e:
        print(f"[!] Error: {e}")

