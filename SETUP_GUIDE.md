# Smart Interview AI - Complete Setup & Run Guide

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (for backend)
- Node.js 16+ (for frontend)
- npm or yarn

## 📋 Step-by-Step Setup

### 1️⃣ Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create environment file (optional)
cp .env.example .env

# Start the backend server
uvicorn app.main:app --reload --port 8000
```

✅ Backend will run on: `http://localhost:8000`

**Verify Backend:**
- Visit `http://localhost:8000/docs` for interactive API documentation
- Or check health: `http://localhost:8000/api/resume/health`

### 2️⃣ Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install npm dependencies
npm install

# Start development server
npm run dev
```

✅ Frontend will run on: `http://localhost:5173` (or another available port)

---

## 🎯 Using the Application

1. **Open Frontend**: Go to `http://localhost:5173` in your browser
2. **Upload Resume**: Click "📄 Upload Resume" and select a PDF, DOCX, or TXT file
3. **Analyze**: Click "🔍 Analyze Resume"
4. **View Results**: See score, skills, experience level, and detailed feedback

---

## 📊 API Endpoints

### Analyze Resume
```bash
POST http://localhost:8000/api/resume/analyze
Content-Type: multipart/form-data

file: <resume file>
```

**Example with curl:**
```bash
curl -X POST "http://localhost:8000/api/resume/analyze" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@resume.pdf"
```

**Example with Python:**
```python
import requests

with open('resume.pdf', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/resume/analyze',
        files={'file': f}
    )
    print(response.json())
```

### Response Format
```json
{
  "success": true,
  "filename": "resume.pdf",
  "score": 85,
  "status": "Shortlisted",
  "feedback": "Strong candidate. Proceed to interview.",
  "details": {
    "name": "John Doe",
    "skills": ["python", "react", "machine learning"],
    "skills_count": 3,
    "experience_level": "mid-level",
    "certifications": ["AWS Certified"],
    "contact": {
      "email": "john@example.com",
      "phone": "+1-234-567-8900"
    }
  },
  "breakdown": {
    "skills": 35,
    "experience": 25,
    "certifications": 10,
    "content": 15
  }
}
```

---

## 🧪 Testing

### Test Backend
```bash
cd backend
python test_api.py
```

### Test with Sample Resume
1. Place a resume file in the backend folder
2. Update `test_api.py` with the filename
3. Run the test script

---

## 📁 Project Structure

```
smart-interview-ai/
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI app
│   │   ├── config.py              # Configuration
│   │   ├── routes/
│   │   │   └── resume.py          # Resume endpoints
│   │   └── services/
│   │       ├── resume_service.py  # Business logic
│   │       ├── text_extractor.py  # PDF/DOCX extraction
│   │       └── resume_analyzer.py # Analysis & scoring
│   ├── requirements.txt
│   ├── .env.example
│   ├── test_api.py
│   └── BACKEND_README.md
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                # Main component
│   │   ├── App.css                # Styles
│   │   ├── main.jsx               # Entry point
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
└── README.md (this file)
```

---

## 🎨 Frontend Features

- ✅ Beautiful, modern UI with gradient design
- ✅ File upload with drag-and-drop support
- ✅ Real-time analysis feedback
- ✅ Detailed score breakdown
- ✅ Skills detection and display
- ✅ Certification recognition
- ✅ Contact information extraction
- ✅ Responsive mobile design

---

## 🧠 Backend Features

### Supported File Types
- PDF (.pdf)
- Word Documents (.docx, .doc)
- Plain Text (.txt)

### Analysis Capabilities
- **Text Extraction**: Robust PDF and document parsing
- **Skill Detection**: 50+ technical and soft skills
- **Experience Level**: Junior, Mid-level, Senior detection
- **Certification**: Industry certification recognition
- **Contact Extraction**: Email and phone number detection
- **Intelligent Scoring**: Multi-factor scoring system (0-100)

### Scoring Breakdown
- **Skills (40 points)**: Technical + soft skills matching
- **Experience (30 points)**: Years and level of experience
- **Certifications (15 points)**: Industry certifications
- **Content Quality (15 points)**: Resume quality metrics

### Status Categories
- **Shortlisted (80+)**: Strong candidate, recommend for interview
- **Under Review (60-79)**: Good fit, consider for interview
- **Possible Match (40-59)**: May need skill development
- **Rejected (<40)**: Does not meet minimum requirements

---

## 🔧 Configuration

### Backend (.env)
```
DEBUG=False
API_TITLE=Smart Interview AI
API_VERSION=1.0.0
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
MAX_FILE_SIZE=10
LOG_LEVEL=INFO
```

### Frontend (App.jsx)
Update the API URL if backend runs on different port:
```javascript
const API_URL = "http://localhost:8000";
```

---

## 🐛 Troubleshooting

### Backend Won't Start
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# If occupied, run on different port
uvicorn app.main:app --reload --port 8001
```

### Frontend Connection Issues
- Ensure backend is running on port 8000
- Check browser console for CORS errors
- Verify firewall settings allow localhost connection

### PDF Extraction Fails
- Ensure PDF is not corrupted
- Try with TXT or DOCX format
- Check file permissions

### Low Scores
- Resume may lack keywords
- Minimum 300 words recommended
- Include standard job-related terminology

---

## 📈 Future Enhancements

- [ ] Advanced NLP with spaCy
- [ ] Machine learning-based scoring
- [ ] Job description matching
- [ ] Interview question generation
- [ ] Multiple resume comparison
- [ ] Database integration for audit logs
- [ ] User authentication and profiles
- [ ] Resume formatting quality scoring

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [PyPDF2 Documentation](https://pypi.org/project/PyPDF2/)
- [Vite Documentation](https://vitejs.dev/)

---

## 📧 Support

For issues or questions:
1. Check the [BACKEND_README.md](backend/BACKEND_README.md) for backend details
2. Review error messages in terminal
3. Check browser console for frontend errors

---

**Version:** 1.0.0  
**Last Updated:** April 2024  
**Status:** ✅ Production Ready
