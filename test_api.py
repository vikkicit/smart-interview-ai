"""
Test script for Smart Interview AI Backend
Run this to test the resume analysis API
"""
import requests
import json

# Configuration
API_URL = "http://localhost:8000"
RESUME_FILE = "sample_resume.pdf"  # Replace with your resume path

def test_health():
    """Test health check endpoint"""
    print("🏥 Testing Health Check...")
    response = requests.get(f"{API_URL}/api/resume/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_upload_resume(file_path):
    """Test resume upload and analysis"""
    print(f"📄 Testing Resume Upload: {file_path}")
    
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                f"{API_URL}/api/resume/analyze",
                files=files
            )
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n✅ Analysis Successful!")
            print(f"Filename: {result.get('filename')}")
            print(f"Score: {result.get('score')}/100")
            print(f"Status: {result.get('status')}")
            print(f"Feedback: {result.get('feedback')}")
            
            print(f"\n📊 Score Breakdown:")
            for key, value in result.get('breakdown', {}).items():
                print(f"  {key.capitalize()}: {value} points")
            
            details = result.get('details', {})
            print(f"\n👤 Details:")
            print(f"  Name: {details.get('name')}")
            print(f"  Experience: {details.get('experience_level')}")
            print(f"  Skills ({details.get('skills_count')}): {', '.join(details.get('skills', []))}")
            if details.get('certifications'):
                print(f"  Certifications: {', '.join(details.get('certifications', []))}")
            if details.get('contact'):
                contact = details.get('contact', {})
                if contact.get('email'):
                    print(f"  Email: {contact.get('email')}")
                if contact.get('phone'):
                    print(f"  Phone: {contact.get('phone')}")
        else:
            print(f"❌ Error: {response.json()}")
            
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_invalid_file():
    """Test with invalid file type"""
    print("\n🔴 Testing Invalid File Type...")
    test_data = {'file': ('test.jpg', b'fake image data')}
    response = requests.post(
        f"{API_URL}/api/resume/analyze",
        files=test_data
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

if __name__ == "__main__":
    print("=" * 60)
    print("Smart Interview AI - Backend Test Suite")
    print("=" * 60)
    print()
    
    # Test health check
    test_health()
    
    # Test resume upload (comment out if no resume file)
    # test_upload_resume(RESUME_FILE)
    
    # Test invalid file
    test_invalid_file()
    
    print("=" * 60)
    print("Tests completed!")
    print("=" * 60)
