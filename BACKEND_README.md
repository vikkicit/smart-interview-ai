# Smart Interview AI - Backend Documentation

## Architecture Overview

```
Frontend (React)
      ↓
POST /api/resume/analyze (file upload)
      ↓
FastAPI Backend
      ↓
┌─────────────────────────┐
│ Text Extraction Layer   │ → Extract text from PDF/DOCX/TXT
├─────────────────────────┤
│ Analysis Layer          │ → Extract skills, experience, certs
├─────────────────────────┤
│ Scoring Engine          │ → Calculate score (0-100)
├─────────────────────────┤
│ Response Generator      │ → Format JSON response
└─────────────────────────┘
      ↓
JSON Response
{
  "filename": "resume.pdf",
  "score": 85,
  "status": "Shortlisted",
  "feedback": "...",
  "details": {...},
  "breakdown": {...}
}
```

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point
│   ├── config.py              # Configuration settings
│   ├── routes/
│   │   ├── __init__.py
│   │   └── resume.py          # Resume endpoints
│   └── services/
│       ├── __init__.py
│       ├── resume_service.py  # Main business logic
│       ├── text_extractor.py  # PDF/DOCX/TXT extraction
│       └── resume_analyzer.py # NLP analysis & scoring
├── requirements.txt
├── .env.example
└── README.md
```

## Installation & Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Create Environment File

```bash
cp .env.example .env
```

### 3. Run the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server will be available at: `http://localhost:8000`

## API Endpoints

### 1. Analyze Resume
**Endpoint:** `POST /api/resume/analyze`

**Request:**
```
Content-Type: multipart/form-data
file: <binary file data>
```

**Response:**
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

### 2. Health Check
**Endpoint:** `GET /api/resume/health`

**Response:**
```json
{
  "status": "healthy",
  "service": "resume-analyzer",
  "version": "1.0.0"
}
```

### 3. API Documentation
**Endpoint:** `GET /docs`

Interactive Swagger UI documentation (auto-generated)

## Scoring System

Total Score: **100 points**

### Breakdown:
- **Skills (40 points)**: Technical skills + soft skills matching
- **Experience (30 points)**: Years of experience and level
- **Certifications (15 points)**: Industry certifications
- **Content Quality (15 points)**: Text length, contact info, etc.

### Status Mapping:
- **Score ≥ 80**: "Shortlisted" ✅ (Recommended for interview)
- **Score 60-79**: "Under Review" 📋 (Good fit, consider for interview)
- **Score 40-59**: "Possible Match" ⚠️ (May need skill development)
- **Score < 40**: "Rejected" ❌ (Does not meet minimum requirements)

## Supported Skills Database

### Technical Skills
- **Programming**: Python, JavaScript, Java, C#, C++, Ruby, PHP, Go, Rust, Kotlin, Swift, TypeScript
- **Web**: React, Vue, Angular, HTML5, CSS3, Tailwind, Bootstrap
- **Databases**: SQL, MySQL, PostgreSQL, MongoDB, Redis, Elasticsearch, Firebase
- **Cloud**: AWS, GCP, Azure
- **DevOps**: Docker, Kubernetes, CI/CD, Jenkins, GitHub Actions, Terraform
- **Data Science**: Machine Learning, TensorFlow, PyTorch, Pandas, NumPy, Scikit-learn, NLP

### Soft Skills
- Communication, Leadership, Problem Solving, Teamwork, Time Management, Adaptability, Creativity, Critical Thinking

## File Type Support

✅ **Supported Formats:**
- PDF (.pdf)
- Word Document (.docx, .doc)
- Plain Text (.txt)

**Max File Size:** 10 MB

## Key Features

1. **Text Extraction**
   - Robust PDF parsing with PyPDF2
   - DOCX support via python-docx
   - Plain text handling

2. **Resume Analysis**
   - Keyword matching for 50+ skills
   - Experience level detection
   - Certification extraction
   - Contact information extraction
   - Name extraction

3. **Intelligent Scoring**
   - Multi-factor scoring system
   - Weighted calculation
   - Detailed breakdown
   - Actionable feedback

4. **Production Ready**
   - Error handling & validation
   - Comprehensive logging
   - CORS enabled
   - Configuration management
   - Async/await support

## Error Handling

All errors return HTTP 400 with error details:

```json
{
  "detail": "Invalid file type. Allowed: PDF, DOCX, TXT"
}
```

## Performance Notes

- Average processing time: 100-500ms per resume
- Supports concurrent requests
- Async file handling

## Development

### Enable Debug Mode
Edit `.env`:
```
DEBUG=True
LOG_LEVEL=DEBUG
```

### Add New Skills
Edit `app/services/resume_analyzer.py`:
```python
TECHNICAL_SKILLS = {
    'new_skill': ['keyword1', 'keyword2'],
    ...
}
```

### Customize Scoring
Edit `calculate_resume_score()` function in `resume_analyzer.py`

## Deployment

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Server (Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## Testing the API

### Using cURL
```bash
curl -X POST "http://localhost:8000/api/resume/analyze" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/resume.pdf"
```

### Using Python
```python
import requests

with open('resume.pdf', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/resume/analyze',
        files={'file': f}
    )
    print(response.json())
```

## Troubleshooting

### PDF Extraction Fails
- Ensure file is not corrupted
- Check file permissions
- Verify PDF is text-based (not image-based)

### Skills Not Detected
- Check skills database in `resume_analyzer.py`
- Ensure resume uses standard keywords
- Add custom keywords to TECHNICAL_SKILLS dict

### Low Score
- Resume may lack skills keywords
- Check experience level mentions
- Verify content quality (minimum 300 words recommended)

## Future Enhancements

- [ ] Advanced NLP with spaCy
- [ ] Machine learning-based skill extraction
- [ ] Resume formatting quality score
- [ ] Job description matching
- [ ] Interview question generation
- [ ] Multiple resume comparison
- [ ] Database integration for audit logs

---

**Version:** 1.0.0  
**Last Updated:** April 2024
