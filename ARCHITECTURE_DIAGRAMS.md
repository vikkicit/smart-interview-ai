# 🏗️ ARCHITECTURE & FLOW DIAGRAMS

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (React)                         │
│                                                             │
│  ┌────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│  │   Upload   │  │   Analyze    │  │  ✨ Improve ✨   │   │
│  │   Resume   │→ │   Resume     │→ │  Resume Button  │   │
│  │            │  │              │  │                 │   │
│  └────────────┘  └──────────────┘  └────────┬────────┘   │
│                                            │              │
│                                     ┌──────↓──────┐       │
│                                     │  Beautiful  │       │
│                                     │   Modal     │       │
│                                     │  (Glass UI) │       │
│                                     └─────────────┘       │
│                                                            │
└────────────────┬─────────────────────────────────────────┘
                 │ API Calls (JSON)
                 ↓
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                        │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   /analyze   │  │  Role        │  │  /improve    │    │
│  │   endpoint   │→ │  Detector    │→ │  endpoint    │    │
│  │              │  │  (13 roles)  │  │  ✨ NEW!     │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                             │
│                   ┌──────────────────────┐                 │
│                   │ Resume Rewriter      │                 │
│                   │ Service ✨ NEW!       │                 │
│                   │                      │                 │
│                   │ • Strengthen verbs   │                 │
│                   │ • Categorize skills  │                 │
│                   │ • Suggest keywords   │                 │
│                   │ • Generate summaries │                 │
│                   └──────────────────────┘                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Request/Response Flow for Improve Endpoint

```
CLIENT REQUEST:
┌─────────────────────────────────────────┐
│ POST /api/resume/improve                │
│                                         │
│ {                                       │
│   "resume_analysis": {                 │
│     "score": 88,                       │
│     "details": {                       │
│       "name": "John",                  │
│       "skills": ["React", "Python"],  │
│       ...                              │
│     },                                 │
│     "role_detection": {                │
│       "primary_role": "Full Stack"    │
│     }                                  │
│   },                                   │
│   "improvements": "full"               │
│ }                                       │
└─────────────────────────────────────────┘
             ↓ PROCESSING ↓

BACKEND PROCESSING:
┌─────────────────────────────────────────┐
│ 1. Extract job role                     │
│ 2. Generate improved summary            │
│ 3. Categorize skills                    │
│ 4. Improve bullet points               │
│ 5. Generate suggestions                │
│ 6. Find recommended keywords           │
│ 7. Create before/after sections        │
└─────────────────────────────────────────┘
             ↓ RESPONSE ↓

SERVER RESPONSE:
┌──────────────────────────────────────────┐
│ {                                        │
│   "success": true,                       │
│   "data": {                              │
│     "job_role": "Full Stack Developer",  │
│     "sections": {                        │
│       "summary": {                       │
│         "before": "Good developer...",   │
│         "after": "Results-driven...",    │
│         "tips": [...]                    │
│       },                                 │
│       "skills": {...},                   │
│       "bullets": {...}                   │
│     },                                   │
│     "suggestions": [                     │
│       {                                  │
│         "title": "Strengthen Verbs",     │
│         "priority": "high",              │
│         "description": "..."             │
│       }                                  │
│     ],                                   │
│     "recommended_keywords": {            │
│       "ats": ["Full-stack", "..."],     │
│       "role_specific": ["..."]          │
│     }                                    │
│   }                                      │
│ }                                        │
└──────────────────────────────────────────┘
             ↓ DISPLAY IN MODAL ↓

BEAUTIFUL UI MODAL:
┌─────────────────────────────────────┐
│  ✨ Resume Improvements        ✕    │
├─────────────────────────────────────┤
│ Before: "Good developer..."         │
│  →                                  │
│ After: "Results-driven developer"   │
│                                     │
│ 💡 Tips:                            │
│ • Tailored for Full Stack           │
│ • Added key skills                  │
│                                     │
│ 🎯 Suggestions:                     │
│ • Strengthen Verbs [HIGH]           │
│ • Add Keywords [MEDIUM]             │
│                                     │
│ 📌 Keywords:                        │
│ [Full-stack] [Microservices]       │
│              [Got it! Close]        │
└─────────────────────────────────────┘
```

---

## Component Hierarchy (Frontend)

```
App
├── State Management
│   ├── file (resume file)
│   ├── loading (API call status)
│   ├── result (analysis result)
│   ├── error (error messages)
│   ├── improveLoading ✨ NEW!
│   ├── improveResult ✨ NEW!
│   └── showImproveModal ✨ NEW!
│
├── UI Components
│   ├── Header
│   ├── Tabs
│   ├── Upload Section
│   │   ├── File Input
│   │   ├── File Info
│   │   └── Analyze Button
│   │
│   └── Results Section
│       ├── Role Detection Card
│       ├── Score Card
│       ├── Skills Display
│       ├── Certifications
│       ├── Contact Info
│       └── Improve Button ✨ NEW!
│
└── Modal Component ✨ NEW!
    ├── Modal Overlay (glass effect)
    ├── Close Button
    ├── Improvement Sections
    │   ├── Before/After comparison
    │   └── Tips display
    ├── Suggestions Box
    ├── Keywords Box
    └── Action Button
```

---

## Service Layer Architecture (Backend)

```
resume_rewriter.py
│
├── Constants
│   ├── ACTION_VERBS (weak → strong mapping)
│   ├── WEAK_PHRASE_REPLACEMENTS
│   ├── IMPACT_PHRASES
│   ├── ATS_KEYWORDS
│   └── SUMMARY_TEMPLATES
│
├── Helper Functions
│   ├── extract_job_role()
│   ├── strengthen_action_verbs()
│   ├── add_metrics_to_achievements()
│   ├── rewrite_bullet_point()
│   └── generate_improvement_suggestions()
│
├── Section Rewriters
│   ├── rewrite_summary()
│   ├── rewrite_skills_section()
│   └── rewrite_project_description()
│
└── Main Function
    └── rewrite_resume() ← Entry point
```

---

## Data Transformation Flow

```
INPUT: Resume Text
│
├─→ Extract Skills: ["React", "Python", "Node.js"]
│
├─→ Detect Role: "Full Stack Developer"
│
├─→ SUMMARY TRANSFORMATION:
│   Input:  "Good developer"
│   ↓
│   Template: "Results-driven {role} with proven..."
│   ↓
│   Output: "Results-driven Full Stack Developer..."
│
├─→ SKILLS TRANSFORMATION:
│   Input:  ["React", "Python", "Docker", "SQL"]
│   ↓
│   Categorize:
│   - Languages: [Python]
│   - Tools: [Docker]
│   - Technical: [React, SQL]
│   ↓
│   Output: {Languages: [...], Tools: [...], ...}
│
├─→ BULLET TRANSFORMATION:
│   Input:  "Worked on ML project"
│   ↓
│   Step 1: Replace verb: "Engineered"
│   Step 2: Add context: "ML project"
│   Step 3: Add metrics: "[X]% improvement"
│   ↓
│   Output: "Engineered machine learning solution..."
│
├─→ SUGGESTION GENERATION:
│   Analyze: Missing action verbs? Missing metrics?
│   ↓
│   Generate: Priority-based suggestions
│   ↓
│   Output: [{title, priority, description}, ...]
│
└─→ OUTPUT: Complete Improvement Data
    {
      sections: {...},
      suggestions: [...],
      keywords: {...}
    }
```

---

## CSS Class Hierarchy

```
root
│
├── .improve-btn
│   ├── :hover
│   ├── :disabled
│   └── ::before (shine effect)
│
├── .modal-overlay
│   ├── @keyframes fadeIn
│   └── backdrop-filter (glass effect)
│
├── .modal-content
│   ├── @keyframes slideIn
│   ├── ::-webkit-scrollbar (styled scrollbar)
│   ├── .modal-close
│   ├── .modal-subtitle
│   ├── .modal-action-btn
│   │
│   └── .improvement-section
│       ├── .before-after
│       │   ├── .before-box
│       │   ├── .arrow
│       │   └── .after-box
│       │
│       ├── .tips-box
│       │
│       ├── .suggestions-box
│       │   ├── .suggestion-item
│       │   ├── .suggestion-header
│       │   ├── .priority-badge
│       │   │   ├── .high
│       │   │   ├── .medium
│       │   │   └── .low
│       │   └── .suggestion-example
│       │
│       └── .keywords-box
│           ├── .keywords-grid
│           ├── .keywords-list
│           └── .keyword-tag
│               └── :hover (glow)
│
└── Media Queries
    ├── @media (max-width: 600px)
    └── @media (max-width: 400px)
```

---

## Event Flow

```
User Action: Click Improve Button
│
├─→ handleImproveResume() called
│
├─→ Validation
│   ├── Check if result exists
│   └── Show error if missing
│
├─→ API Call
│   ├── Set improveLoading = true
│   ├── POST /api/resume/improve
│   └── Set improveLoading = false
│
├─→ Response Handling
│   ├── Check response.ok
│   ├── Check data.success
│   └── Set improveResult
│
├─→ UI Update
│   ├── Set showImproveModal = true
│   └── Modal renders with data
│
└─→ User Interaction
    ├── View improvement sections
    ├── Read suggestions
    ├── Check keywords
    └── Click close (setShowImproveModal = false)
```

---

## State Diagram

```
Initial State:
  improveLoading: false
  improveResult: null
  showImproveModal: false

↓ User clicks Improve button

Loading State:
  improveLoading: true ← API call in progress
  improveResult: null
  showImproveModal: false

↓ API response received

Success State:
  improveLoading: false
  improveResult: {data} ← Populated with response
  showImproveModal: true ← Modal opens

↓ User clicks Close

Back to Initial:
  improveLoading: false
  improveResult: null
  showImproveModal: false
```

---

## Algorithm: Action Verb Strengthening

```
INPUT: "Worked on backend API"

STEP 1: Find weak verbs
  Pattern: \b(worked|helped|handled|did|used)\b
  Found: "Worked"

STEP 2: Map to strong verb
  WEAK_PHRASE_REPLACEMENTS["worked on"] → "Developed"

STEP 3: Replace in text
  "Worked on" → "Developed"

STEP 4: Capitalize properly
  "Developed" (already capitalized)

STEP 5: Add context
  Result: "Developed backend API"

OUTPUT: "Developed backend API"
```

---

## Algorithm: Skill Categorization

```
INPUT: ["React", "Python", "Docker", "SQL", "Communication"]

DICTIONARY LOOKUP:
  "React" → in programming_langs → Languages
  "Python" → in programming_langs → Languages
  "Docker" → in tools_platforms → Tools & Platforms
  "SQL" → not in dict → Technical
  "Communication" → in soft_skills_list → Soft Skills

OUTPUT:
{
  "Languages": ["React", "Python"],
  "Tools & Platforms": ["Docker"],
  "Technical": ["SQL"],
  "Soft Skills": ["Communication"]
}
```

---

## Error Handling Flow

```
Try:
  ├─→ Call improve endpoint
  ├─→ Get response
  ├─→ Parse JSON
  └─→ Validate data

Catch Errors:
  ├─→ Network error
  │   └─→ Show: "Connection failed"
  │
  ├─→ HTTP error (response.ok = false)
  │   └─→ Show: "Failed to improve resume"
  │
  ├─→ Data error (data.success = false)
  │   └─→ Show: data.error
  │
  └─→ Unexpected error
      └─→ Show: General error message

Finally:
  └─→ Set improveLoading = false
```

---

## Performance Optimization Points

```
Frontend:
  ✅ React.useState for efficient state management
  ✅ Conditional rendering to avoid unnecessary DOM
  ✅ CSS animations (GPU-accelerated)
  ✅ Modal only loads when needed

Backend:
  ✅ Simple dictionary lookups (O(1) complexity)
  ✅ No database queries
  ✅ Fast string operations
  ✅ Async/await for responsiveness

Network:
  ✅ Single POST request (instead of multiple)
  ✅ Minimal JSON payload
  ✅ Efficient data structures
  ✅ No file uploads
```

---

**This architecture ensures clean separation of concerns, easy maintenance, and optimal performance!**
