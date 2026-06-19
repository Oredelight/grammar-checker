# Dreamy Checker - AI-Powered Grammar Correction System

An intelligent grammar checking and correction system powered by Google's Gemini AI. Dreamy Checker provides comprehensive text refinement through smart error detection and context-aware corrections with a focus on simplicity and efficiency.


## Overview

Dreamy Checker is an intelligent grammar correction tool designed to help users write better English. This system leverages Google Gemini AI for intelligent, context-aware corrections:

1. **AI-Powered Engine**: Google Gemini API provides intelligent, context-aware corrections
2. **Intelligent Chunking**: Handles long documents by splitting intelligently (max 180 words per chunk)
3. **Lightweight & Fast**: Minimal memory footprint, optimized for deployment on resource-constrained servers

### Why AI-Only?
- **Intelligence**: Gemini AI understands context and improves fluency naturally
- **Efficiency**: Minimal dependencies and memory usage
- **Context-Aware**: Better understanding of nuanced grammar issues
- **Scalability**: Perfect for deployment on limited server resources

## Features

### Core Capabilities
- **AI Grammar Correction**: Google Gemini AI for intelligent correction
- **REST API**: FastAPI-based endpoint for programmatic access with request validation
- **Interactive Web UI**: Clean, responsive interface with real-time grammar checking
- **Comprehensive Issue Detection**: Identifies grammar errors, spelling, capitalization, punctuation, and more
- **Contextual Analysis**: Returns context for each detected issue to help users understand the error
- **Intelligent Text Chunking**: Handles long documents by splitting intelligently (max 180 words per chunk)

## Technology Stack

### Backend Architecture
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | FastAPI 0.137.2 | Modern async API server |
| **ASGI Server** | Uvicorn | Production-ready server |
| **AI Provider** | Google Gemini API | Context-aware AI corrections |
| **Data Validation** | Pydantic 2.13.4 | Request/response validation |
| **Templating** | Jinja2 3.1.6 | HTML template rendering |
| **Configuration** | python-dotenv | Environment variable management |

### Frontend Stack
- **HTML5**: Semantic markup
- **CSS3**: Responsive design with custom styling
- **Vanilla JavaScript**: DOM manipulation and API communication
- **Design**: Pink/dreamy theme with accessibility considerations

### Key Dependencies Explained
```
Web Services:
  - fastapi: Async request handling
  - uvicorn: Production ASGI server
  - jinja2: Template rendering

AI Integration:
  - google-genai: Google Gemini API client for AI corrections

Data Handling:
  - pydantic: Type-safe validation

Utilities:
  - python-dotenv: Environment configuration
  - requests: HTTP client library
```

## Project Architecture

### Directory Structure
```
grammer-checker/
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies with versions
├── README.md                   # Comprehensive documentation (this file)
│
├── api/                        # API layer
│   ├── __init__.py
│   └── routes.py              # Grammar checker endpoint definitions
│
├── services/                   # Business logic layer
│   ├── __init__.py
│   ├── grammarchecker.py      # Core grammar checking orchestration
│   ├── aicorrector.py         # Google Gemini AI integration
│   └── schemas.py             # Pydantic data models and validators
│
├── evaluation/                 # Quality assurance
│   ├── __init__.py
│   ├── evaluate.py            # Test execution and reporting
│   └── test_cases.json        # Test cases with expected outputs
│
└── templates/                  # Frontend
    └── index.html             # Interactive web UI
```

### Component Interaction Diagram

```
┌─────────────────────────────────────────────────────────┐
│                     User Interface                       │
│                    (templates/index.html)                │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP POST /check-grammar
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   FastAPI Application                    │
│                      (main.py)                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                    API Routes Layer                      │
│                  (api/routes.py)                         │
│         • Input validation (GrammarInput schema)         │
│         • Response formatting (GrammarOutput schema)     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   Grammar Checker                        │
│            (services/grammarchecker.py)                  │
│         Primary orchestration logic:                     │
│  1. Call Google Gemini AI for corrections                │
│  2. Diff original vs corrected text                      │
│  3. Extract issues from differences                      │
│  4. Return formatted results                             │
└────────────┬────────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────┐
│  Google Gemini AI Service        │
│  (services/aicorrector.py)       │
│                                  │
│ • Natural language AI            │
│ • Context-aware prompts          │
│ • Intelligent chunking           │
│ • API-based (cloud)              │
│ • Free tier available            │
└──────────────────────────────────┘
```

## Installation & Setup

### Prerequisites
Before installation, ensure you have:
- **Python 3.8+** (tested on 3.10 and 3.11)
- **pip** package manager
- **Virtual environment** support (venv or conda)
- **Google Gemini API Key** (Free tier available at https://aistudio.google.com/)
- **~500MB Disk Space**: For dependencies (much smaller without LanguageTool)

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/grammer-checker.git
cd grammer-checker
```

#### 2. Create Virtual Environment
```bash
# Using venv (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables
```bash
# Create .env file in project root
echo GEMINI_API_KEY=your_api_key_here > .env

# Get your API key from: https://aistudio.google.com/
```

#### 5. Verify Installation
```bash
# Check Python version
python --version

# Test FastAPI
python -c "import fastapi; print(f'FastAPI {fastapi.__version__}')"

# Test Gemini client
python -c "import google.genai; print('Gemini API ready')"
```

## Running the Application

### Development Server
```bash
# Run with hot-reload for development
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Output:
# INFO:     Uvicorn running on http://0.0.0.0:8000
# INFO:     Application startup complete
```

Then open: `http://localhost:8000/`

### Production Server
```bash
# Multi-worker production setup
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Testing the Installation
```bash
# Test via curl
curl -X POST "http://localhost:8000/check-grammar" \
  -H "Content-Type: application/json" \
  -d '{"text": "He go to the store yesterday."}'

# Expected response:
# {
#   "original": "He go to the store yesterday.",
#   "corrected": "He goes to the store yesterday.",
#   "issues": [
#     {
#       "message": "Third person singular...",
#       "context": "go"
#     }
#   ]
# }
```

## API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints Overview

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/check-grammar` | Check and correct grammar |
| GET | `/` | Interactive web interface |
| GET | `/docs` | Swagger UI documentation |
| GET | `/redoc` | ReDoc API documentation |

### Detailed Endpoint Reference

#### 1. Grammar Checker Endpoint
```
POST /check-grammar
```

**Purpose**: Analyzes text for grammar errors and returns corrections

**Content-Type**: `application/json`

**Request Body**:
```json
{
  "text": "Your text to check for grammar errors."
}
```

**Field Descriptions**:
- `text` (string, required): The text to check
  - Minimum length: 1 character
  - Maximum length: No hard limit (chunked automatically)
  - Must not be empty or whitespace-only

**Request Examples**:
```bash
# Simple query
curl -X POST "http://localhost:8000/check-grammar" \
  -H "Content-Type: application/json" \
  -d '{"text": "The cat are sleeping."}'

# Complex text
curl -X POST "http://localhost:8000/check-grammar" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I have went to the store and buyed some milk. The weather were nice."
  }'

# Long document (auto-chunked)
curl -X POST "http://localhost:8000/check-grammar" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Here is a very long text that spans multiple paragraphs and sentences..."
  }'
```

**Response** (200 OK):
```json
{
  "original": "The cat are sleeping.",
  "corrected": "The cat is sleeping.",
  "issues": [
    {
      "message": "Subject-verb agreement: 'cat' is singular but 'are' is plural",
      "context": "are"
    }
  ]
}
```

**Response Fields**:
- `original` (string): The input text unchanged
- `corrected` (string): The corrected version of the text
- `issues` (array): Detected grammar issues
  - `message` (string): Description of the error
  - `context` (string): The specific word/phrase causing the issue

**Error Responses**:

422 Unprocessable Entity (Empty text):
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "text"],
      "msg": "Text cannot be empty",
      "input": ""
    }
  ]
}
```

500 Internal Server Error (Model issues):
```json
{
  "detail": "Error loading AI model. Check logs for details."
}
```

**Response Time**:
- Cold start (first request, model loading): 3-5 seconds
- Subsequent requests: 0.5-2 seconds (avg 1.41s)
- Varies by text length and system resources

#### 2. Web Interface Endpoint
```
GET /dreamy-checker
```

**Purpose**: Serves the interactive web UI

**Response**: HTML page with embedded CSS/JavaScript

**Features**:
- Real-time grammar checking
- Side-by-side display of original vs corrected
- Issue list with context
- Copy-to-clipboard functionality
- Beautiful pink/dreamy theme
- Responsive mobile design

#### 3. API Documentation
```
GET /docs           # Swagger UI
GET /redoc          # ReDoc
GET /openapi.json   # OpenAPI spec
```




### User Workflow
```
1. Navigate to /dreamy-checker
2. Paste or type text in input box
3. Click "Fix Grammar" button
4. See errors highlighted, corrected, and issues
5. Copy corrected text or try again
```

## How It Works

### AI-Powered Grammar Checking Process

**Grammar Correction Flow**
- Receives user text input
- Splits text into intelligent chunks (max 180 words for optimal API performance)
- Sends each chunk to Gemini API with grammar correction prompt
- Context-aware corrections using LLM understanding
- Gracefully falls back to original text if API unavailable

**Issue Detection & Reporting**
- Compares original vs. AI-corrected text using SequenceMatcher
- Extracts differences at word level
- Returns comprehensive issue list with context and suggested corrections
- Highlights specific problem areas to help users understand errors

### API Features
- **Graceful Degradation**: Works even if Gemini API is temporarily unavailable
- **Auto-Chunking**: Handles documents of any length
- **Context Preservation**: Maintains semantic meaning while correcting grammar
- **Fast Processing**: Minimal overhead with optimized chunking



### Running Tests

```bash
# Execute evaluation suite
python -m evaluation.evaluate

# Output includes:
# - Test results for each category
# - Overall success metrics
# - Average response time
# - Failed case details
```

### Test Cases

Test cases are stored in `evaluation/test_cases.json` and cover:
- Articles (a/an/the usage)
- Capitalization (proper nouns, sentence starts)
- Mixed Errors (combination of multiple issues)
- Possessives (apostrophe placement)
- Prepositions (in/on/at/by, etc.)
- Pronouns (he/she/they agreement)
- Punctuation (commas, periods, semicolons)
- Spelling (typos and misspellings)
- Subject-Verb Agreement (plural/singular matching)
- Tense (past, present, future consistency)





### Test Cases Structure

Test cases are stored in `evaluation/test_cases.json`:
```json
[
  {
    "category": "subject_verb_agreement",
    "input": "The dogs runs quickly.",
    "expected": "The dogs run quickly."
  },
  {
    "category": "spelling",
    "input": "I recieved your message.",
    "expected": "I received your message."
  }
]
```

### Adding New Test Cases

1. Edit `evaluation/test_cases.json`
2. Add entry with category, input, and expected output
3. Run evaluation:
   ```bash
   python -m evaluation.evaluate
   ```


### Performance Troubleshooting

| Symptom | Likely Cause | Solution |
|---------|---------|----------|
| No corrections provided | Gemini API key missing/invalid | Add GEMINI_API_KEY to .env |
| Slow API responses | Rate limiting or large text | Check Gemini API quota, reduce text size |
| Empty text error | Invalid input | Provide non-empty text |
| Text not chunking properly | Large document | Check text formatting, ensure UTF-8 encoding |


## Deployment

### Render.com Deployment

The application is optimized for deployment on Render's free tier using Python native runtime:

**Configuration (render.yaml)**:
```yaml
services:
  - type: web
    name: grammer-checker
    env: python
    plan: standard
    startCommand: python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

**Environment Variables** on Render:
1. Add `GEMINI_API_KEY` in your Render dashboard environment variables
2. Commit and push your code to trigger automatic deployment

**Memory Optimization**:
- Removed LanguageTool (259MB) for minimal memory footprint
- ~50MB of dependencies only
- Perfect for 512MB free tier instances

### Other Hosting Platforms

Works on any platform supporting Python (Heroku, Railway, Vercel with serverless, AWS Lambda, GCP Cloud Run, etc.)

**Basic Command**:
```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request


---

**Last Updated**: June 2026\
**AI Engine**: Google Gemini API\
**Architecture**: AI-powered (Cloud-based LLM)