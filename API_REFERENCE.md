# API REFERENCE - Explainable Scoring System

## Endpoint: POST /api/resume/analyze

### Overview
Analyzes a resume and returns a detailed score breakdown with improvement suggestions and action plan.

---

## Sample Response (Complete)

```json
{
  "success": true,
  "filename": "john_doe_resume.pdf",
  "score": 82,
  "status": "✓ Strong Match",
  "feedback": "Good fit with strong fundamentals. Recommended for interview.",
  "details": {
    "name": "John Doe",
    "skills": [
      "python",
      "javascript",
      "react",
      "nodejs",
      "typescript",
      "sql",
      "postgresql",
      "mongodb",
      "docker",
      "aws",
      "git",
      "rest api",
      "fastapi",
      "leadership",
      "teamwork",
      "communication",
      "problem solving",
      "agile"
    ],
    "skills_count": 18,
    "experience_level": "mid-level",
    "certifications": [
      "AWS Certified Solutions Architect",
      "Google Cloud Professional Cloud Architect",
      "Certified Kubernetes Administrator"
    ],
    "contact": {
      "email": "john@example.com",
      "phone": "+1 (555) 123-4567"
    }
  },
  "breakdown": {
    "skills": {
      "score": 32,
      "max": 40,
      "percentage": 80,
      "details": "Found 18 unique skills with strong technical foundation"
    },
    "experience": {
      "score": 20,
      "max": 25,
      "level": "Mid-level (2-5 years)",
      "percentage": 80,
      "details": "Mid-level (2-5 years)"
    },
    "projects": {
      "score": 12,
      "max": 15,
      "basic_projects": 2,
      "relevant_projects": 1,
      "percentage": 80,
      "details": "Found 2 projects + 1 domain-relevant projects"
    },
    "certifications": {
      "score": 7,
      "max": 10,
      "count": 3,
      "percentage": 70,
      "details": "3 certifications + senior-level bonus"
    },
    "content": {
      "score": 8,
      "max": 10,
      "percentage": 80,
      "details": "Length: 450 words (adequate) | Contact: Email + Phone ✓ | Name: Present ✓ | Action keywords: 6 found ✓"
    }
  },
  "role_detection": {
    "primary_role": "Senior Full-Stack Developer",
    "confidence": 87,
    "confidence_level": "High Confidence",
    "secondary_roles": [
      "Tech Lead",
      "DevOps Engineer",
      "Software Architect"
    ],
    "message": "Strong match for Full-Stack and DevOps roles with excellent cloud experience."
  },
  "improvements": {
    "suggestions": [
      "🔧 Learn high-demand skills: React, Docker, Kubernetes",
      "🎯 Add 2–3 domain-specific projects relevant to target role",
      "🏆 Earn industry-recognized certifications (AWS, Google Cloud, etc.)",
      "📚 Pursue advanced cloud certifications",
      "✍️ Use action verbs: 'Achieved', 'Improved', 'Led', 'Implemented'",
      "📊 Add quantifiable metrics: 'Improved performance by 30%'",
      "🔗 Build portfolio on GitHub/personal website",
      "💡 Improve resume summary with key achievements"
    ],
    "by_category": {
      "skills": [
        "🔧 Learn high-demand skills: React, Docker, Kubernetes",
        "💬 Highlight soft skills: communication, problem-solving, teamwork"
      ],
      "experience": [],
      "projects": [
        "🎯 Add 2–3 domain-specific projects relevant to target role",
        "🔗 Include domain-specific projects relevant to target roles"
      ],
      "certifications": [
        "🏆 Earn industry-recognized certifications (AWS, Google Cloud, etc.)",
        "📚 Add more certifications (currently 3, target 3+)"
      ],
      "content": [
        "✍️ Use action verbs: 'Achieved', 'Improved', 'Led', 'Implemented'",
        "📊 Add quantifiable metrics: 'Improved performance by 30%'"
      ]
    },
    "priority": "🟡 MEDIUM",
    "priority_description": "Some improvements recommended for better competitiveness",
    "total_improvements": 8,
    "focus_areas": [
      "skills",
      "projects"
    ]
  },
  "action_plan": {
    "timeframe": "30 Days",
    "total_duration": "1 month",
    "phases": {
      "immediate": {
        "title": "🔥 Immediate Actions (Next 5 Days)",
        "actions": [
          {
            "category": "SKILLS",
            "action": "Update resume with contact details and action verbs",
            "duration": "3-5 days"
          },
          {
            "category": "CONTENT",
            "action": "Add quantifiable metrics to achievements",
            "duration": "2-3 days"
          }
        ]
      },
      "short_term": {
        "title": "⚡ Short-Term Improvements (1-2 Weeks)",
        "actions": [
          {
            "category": "SKILLS",
            "action": "Begin online course: Advanced React Patterns (Udemy/Coursera)",
            "duration": "1-2 weeks"
          },
          {
            "category": "PROJECTS",
            "action": "Start full-stack portfolio project with GitHub deployment",
            "duration": "1-2 weeks"
          }
        ]
      },
      "medium_term": {
        "title": "📚 Medium-Term Build (3-4 Weeks)",
        "actions": [
          {
            "category": "PROJECTS",
            "action": "Complete and deploy portfolio project to GitHub",
            "duration": "3-4 weeks"
          },
          {
            "category": "CERTIFICATIONS",
            "action": "Enroll in AWS Solutions Architect certification course",
            "duration": "3-4 weeks"
          }
        ]
      },
      "long_term": {
        "title": "🚀 Long-Term Growth (4+ Weeks)",
        "actions": [
          {
            "category": "EXPERIENCE",
            "action": "Seek internship or freelance project opportunities",
            "duration": "Ongoing"
          },
          {
            "category": "SKILLS",
            "action": "Continue learning complementary technologies",
            "duration": "Ongoing"
          },
          {
            "category": "GENERAL",
            "action": "Apply to jobs while building improvements",
            "duration": "Ongoing"
          }
        ]
      }
    }
  }
}
```

---

## Response Fields Explanation

### Top Level
| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Whether analysis completed successfully |
| `filename` | string | Name of uploaded resume file |
| `score` | number | Final weighted score (0-100) |
| `status` | string | Status badge with emoji |
| `feedback` | string | Recommendation text |

### Details
| Field | Type | Description |
|-------|------|-------------|
| `details.name` | string | Extracted candidate name |
| `details.skills` | array | List of detected skills |
| `details.skills_count` | number | Total unique skills |
| `details.experience_level` | string | Career level detected |
| `details.certifications` | array | List of certifications found |
| `details.contact` | object | Email and phone if found |

### Breakdown (NEW)
Each component (skills, experience, projects, certifications, content):

| Field | Type | Description |
|-------|------|-------------|
| `score` | number | Points earned (0 to max) |
| `max` | number | Maximum possible points |
| `percentage` | number | Score as percentage (0-100) |
| `details` | string | Human-readable explanation |
| `level` | string | (Experience only) Level description |
| `count` | number | (Certifications) Number of certs |
| `basic_projects` | number | (Projects) Basic project count |
| `relevant_projects` | number | (Projects) Domain-relevant count |

### Improvements (NEW)
| Field | Type | Description |
|-------|------|-------------|
| `suggestions` | array | Overall improvement suggestions |
| `by_category` | object | Suggestions grouped by category |
| `priority` | string | Priority level with emoji |
| `priority_description` | string | What priority means |
| `total_improvements` | number | Count of suggestions |
| `focus_areas` | array | Categories needing attention |

### Action Plan (NEW)
| Field | Type | Description |
|-------|------|-------------|
| `timeframe` | string | Duration of plan (e.g., "30 Days") |
| `phases` | object | Four time-based phases |
| `phases.*.title` | string | Phase name with emoji |
| `phases.*.actions` | array | Action items for phase |
| `action.category` | string | Skill area (SKILLS, PROJECTS, etc.) |
| `action.action` | string | Specific action to take |
| `action.duration` | string | Estimated time to complete |

---

## Score Status Levels

### Status Values and Meanings

```
⭐ Shortlisted (90-100)
   → "Excellent candidate. Proceed to interview immediately."
   
✓ Strong Match (75-89)
   → "Good fit with strong fundamentals. Recommended for interview."
   
~ Under Review (60-74)
   → "Moderate match. Consider for interview with skill review."
   
⚠ Possible Match (45-59)
   → "Below average. May require significant skill development."
   
✗ Needs Improvement (<45)
   → "Does not meet current requirements. Recommend skill building."
```

---

## Priority Levels

### Priority Values and Meanings

```
🔴 CRITICAL (<45 score)
   "Significant improvements needed across multiple areas"
   
🟠 HIGH (45-59 score)
   "Notable improvements recommended before job applications"
   
🟡 MEDIUM (60-74 score)
   "Some improvements recommended for better competitiveness"
   
🟢 LOW (75+ score)
   "Minor improvements suggested for optimization"
```

---

## Detailed Examples

### Example 1: Excellent Candidate

```json
{
  "score": 95,
  "status": "⭐ Shortlisted",
  "breakdown": {
    "skills": {
      "score": 40,
      "max": 40,
      "percentage": 100,
      "details": "Found 25+ unique skills with comprehensive coverage"
    },
    "experience": {
      "score": 25,
      "max": 25,
      "percentage": 100,
      "level": "Senior (5+ years)"
    },
    "projects": {
      "score": 15,
      "max": 15,
      "percentage": 100,
      "details": "Found 2 projects + 2 domain-relevant projects"
    },
    "certifications": {
      "score": 10,
      "max": 10,
      "percentage": 100,
      "details": "5+ certifications (comprehensive) + senior-level bonus"
    },
    "content": {
      "score": 10,
      "max": 10,
      "percentage": 100,
      "details": "Length: 620 words (comprehensive) | Contact: Email + Phone ✓ | Name: Present ✓ | Action keywords: 12 found ✓"
    }
  },
  "improvements": {
    "suggestions": [],
    "priority": "🟢 LOW",
    "priority_description": "Minor improvements suggested for optimization",
    "total_improvements": 0
  }
}
```

### Example 2: Needs Development

```json
{
  "score": 35,
  "status": "✗ Needs Improvement",
  "breakdown": {
    "skills": {
      "score": 14,
      "max": 40,
      "percentage": 35,
      "details": "Found 7 unique skills (limited coverage)"
    },
    "experience": {
      "score": 0,
      "max": 25,
      "percentage": 0,
      "level": "Entry-level/Fresher"
    },
    "projects": {
      "score": 3,
      "max": 15,
      "percentage": 20,
      "details": "Found 1 projects + 0 domain-relevant projects"
    },
    "certifications": {
      "score": 0,
      "max": 10,
      "percentage": 0,
      "details": "No certifications found"
    },
    "content": {
      "score": 5,
      "max": 10,
      "percentage": 50,
      "details": "Length: 180 words (too brief) | Contact: Email or Phone ✓"
    }
  },
  "improvements": {
    "suggestions": [
      "⚠️ CRITICAL: Skills gap detected. Consider online courses",
      "📅 Build real-world experience: Seek internships",
      "🎯 Add 2-3 substantial projects with clear impact",
      "⚠️ CRITICAL: No projects found. Add portfolio projects",
      "🏆 Earn industry certifications (Coursera, AWS, etc.)",
      "📝 Expand resume content to 400-600 words",
      "📧 Add email address to contact information",
      "✍️ Use action verbs and quantifiable metrics"
    ],
    "by_category": {
      "skills": [
        "⚠️ CRITICAL: Skills gap detected. Consider online courses",
        "💬 Highlight soft skills: communication, teamwork"
      ],
      "experience": [
        "📅 Build real-world experience: Seek internships",
        "🛠️ Create portfolio projects to demonstrate experience"
      ],
      "projects": [
        "🎯 Add 2-3 substantial projects with clear impact",
        "⚠️ CRITICAL: No projects found. Add portfolio projects"
      ],
      "certifications": [
        "🏆 Earn industry certifications (Coursera, AWS, etc.)"
      ],
      "content": [
        "📝 Expand resume content to 400-600 words",
        "📧 Add email address to contact information"
      ]
    },
    "priority": "🔴 CRITICAL",
    "priority_description": "Significant improvements needed across multiple areas",
    "total_improvements": 8,
    "focus_areas": [
      "skills",
      "experience",
      "projects",
      "certifications",
      "content"
    ]
  }
}
```

---

## Error Response

### If Something Goes Wrong

```json
{
  "success": false,
  "error": "Could not extract sufficient text from file"
}
```

### Possible Errors
- `"Invalid file type. Allowed: PDF, DOCX, TXT"`
- `"File is empty"`
- `"Could not extract sufficient text from file"`
- `"Failed to process resume: {error details}"`

---

## Testing the API

### Using cURL

```bash
# Upload and analyze a resume
curl -X POST http://localhost:8000/api/resume/analyze \
  -F "file=@resume.pdf"
```

### Using Python

```python
import requests

with open('resume.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post(
        'http://localhost:8000/api/resume/analyze',
        files=files
    )
    
result = response.json()
print(f"Score: {result['score']}")
print(f"Status: {result['status']}")
print(f"Breakdown: {result['breakdown']}")
print(f"Improvements: {result['improvements']}")
```

### Using JavaScript/Fetch

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

const response = await fetch(
  'http://localhost:8000/api/resume/analyze',
  {
    method: 'POST',
    body: formData
  }
);

const result = await response.json();
console.log('Score:', result.score);
console.log('Suggestions:', result.improvements.suggestions);
```

---

## Integration Checklist

- [ ] Backend returns new response structure
- [ ] Frontend displays breakdown section
- [ ] Frontend displays improvements section
- [ ] Frontend displays action plan
- [ ] All icons render correctly
- [ ] Colors display properly
- [ ] Mobile layout is responsive
- [ ] Suggestions are readable
- [ ] Action plan is clickable/copyable
- [ ] No console errors

---

## Migration from Old API

### What Changed
- Response structure extended (not breaking)
- Old fields still present for backward compatibility
- New fields: `improvements`, `action_plan`
- Enhanced: `breakdown` (now includes details)

### What Stayed the Same
- Same endpoint `/api/resume/analyze`
- Same upload method (multipart form)
- Same `score`, `status`, `feedback` fields
- Same `details`, `role_detection` fields

### How to Update Frontend
1. No changes needed if you only use old fields
2. Add new sections for improvements & action_plan
3. Update breakdown display to show details
4. Add responsive styles for new sections

---

**API Reference Complete!** 🚀

For more details, see:
- EXPLAINABLE_SCORING_SYSTEM.md (scoring logic)
- SCORING_QUICK_START.md (examples)
- UI_BREAKDOWN_LAYOUT.md (visual guide)
