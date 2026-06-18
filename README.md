# Dreamy Checker - Advanced Grammar Correction System

A sophisticated hybrid grammar checking and correction system that combines rule-based detection with Google's Gemini AI for intelligent corrections. Dreamy Checker provides comprehensive text refinement through intelligent error detection and context-aware corrections.


## Overview

Dreamy Checker is an intelligent grammar correction tool designed to help users write better English. This system leverages both rule-based and AI-powered approaches for comprehensive grammar checking:

1. **Rule-Based Engine**: LanguageTool detects grammar violations against comprehensive English rules
2. **AI Enhancement**: Google Gemini API provides intelligent, context-aware corrections
3. **Intelligent Chunking**: Handles long documents by splitting intelligently (max 180 words per chunk)

### Why Hybrid Approach?
- **Precision**: Rule-based engine catches technical grammar errors with reliable patterns
- **Intelligence**: Gemini AI understands context and improves fluency naturally
- **Scalability**: Intelligently chunks text to handle documents of any length
- **Reliability**: Filters out false positives and noisy rules

## Features

### Core Capabilities
- **Hybrid Grammar Correction**: Combines LanguageTool rule-based checking with Google Gemini AI
- **Dual-Layer Detection**: First pass uses LanguageTool rules, second pass uses AI analysis
- **REST API**: FastAPI-based endpoint for programmatic access with request validation
- **Interactive Web UI**: Clean, responsive interface with real-time grammar checking
- **Comprehensive Issue Detection**: Identifies grammar errors, spelling, capitalization, punctuation, and more
- **Contextual Analysis**: Returns context for each detected issue to help users understand the error
- **Intelligent Text Chunking**: Handles long documents by splitting intelligently (max 180 words per chunk)
- **Smart Filtering**: Removes false positives by filtering noisy LanguageTool rules

## Technology Stack

### Backend Architecture
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | FastAPI 0.136.3 | Modern async API server |
| **ASGI Server** | Uvicorn | Production-ready server |
| **Grammar Engine** | language-tool-python 3.4 | Rule-based error detection |
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
Core Processing:
  - language-tool-python: Comprehensive grammar rules (English)
  - google-genai: Google Gemini API client for AI corrections

Web Services:
  - fastapi: Async request handling
  - uvicorn: Production ASGI server
  - jinja2: Template rendering

Data Handling:
  - pydantic: Type-safe validation
  - python-multipart: Form data parsing

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
│  1. Initial LanguageTool pass                            │
│  2. Extract issues and context                           │
│  3. Call Google Gemini AI for corrections                │
│  4. Diff original vs corrected text                      │
│  5. Merge and deduplicate issues                         │
└────┬────────────────────────────┬───────────────────────┘
     │                            │
     ▼                            ▼
┌──────────────────┐    ┌──────────────────────────┐
│  LanguageTool    │    │ Google Gemini AI Service │
│ (Rule-based)     │    │ (services/aicorrector.py)│
│                  │    │                          │
│ • 50+ grammar    │    │ • Natural language AI    │
│   rules          │    │ • Context-aware prompts  │
│ • English US     │    │ • Intelligent chunking   │
│ • Pattern match  │    │ • API-based (cloud)      │
│ • Fast detection │    │ • Graceful fallback      │
└──────────────────┘    └──────────────────────────┘
```

## Installation & Setup

### Prerequisites
Before installation, ensure you have:
- **Python 3.8+** (tested on 3.10 and 3.11)
- **pip** package manager
- **Virtual environment** support (venv or conda)
- **Google Gemini API Key** (Free tier available at https://aistudio.google.com/)
- **~2GB Disk Space**: For dependencies

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

# Test language tools
python -c "import language_tool_python; print('Language Tool ready')"

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

Then open: `http://localhost:8000/dreamy-checker`

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
| GET | `/dreamy-checker` | Interactive web interface |
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

### Dual-Layer Grammar Checking Process

**Layer 1: Rule-Based Detection (LanguageTool)**
- Detects issues using 50+ predefined grammar rules
- Fast pattern matching on original text
- Provides rule-based suggestions
- Filters out noisy rules (SKIP_RULES)

**Layer 2: AI-Powered Refinement (Google Gemini)**
- Splits text into intelligent chunks (max 180 words)
- Sends each chunk to Gemini API with grammar correction prompt
- Context-aware corrections using LLM understanding
- Gracefully falls back to original text if API unavailable

**Integration & Deduplication**
- Compares original vs. AI-corrected text using SequenceMatcher
- Extracts differences at word level
- Merges issues from both layers
- Removes duplicate/overlapping issues
- Returns comprehensive issue list with context

### API Features
- **Graceful Degradation**: Works even if Gemini API is unavailable (returns LanguageTool results)
- **Auto-Chunking**: Handles documents of any length
- **Context Preservation**: Maintains semantic meaning while correcting grammar



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
| Slow API responses | Rate limiting | Check Gemini API quota |
| LanguageTool only results | Gemini API unavailable | Check API connection, see logs |
| Empty text error | Invalid input | Provide non-empty text |
| Text not chunking properly | Large document | Check text formatting |


## Deployment

### Docker Deployment

**Dockerfile**:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build and Run**:
```bash
# Build image
docker build -t dreamy-checker .

# Run with environment variable
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key_here dreamy-checker

# Or with .env file
docker run -p 8000:8000 --env-file .env dreamy-checker
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
**Architecture**: Hybrid (Rule-based + AI-powered)