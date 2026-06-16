# Dreamy Checker - Advanced Grammar Correction System

A sophisticated dual-engine grammar checking and correction system that combines rule-based detection with AI-powered corrections to provide comprehensive text refinement. Dreamy Checker uses a hybrid approach to achieve 96.23% accuracy across diverse grammar error categories.


## Overview

Dreamy Checker is an intelligent grammar correction tool designed to help users write better English. Unlike single-engine solutions, this system leverages both rule-based and AI-powered approaches:

1. **Rule-Based Engine**: LanguageTool detects grammar violations against comprehensive English rules
2. **AI Enhancement**: Grammarly's CoEdit-Large model refines corrections with context awareness
3. **Validation Loop**: A second pass ensures corrections are valid and improves overall quality

### Why Dual-Engine?
- **Precision**: Rule-based engine catches technical grammar errors
- **Context**: AI model understands meaning and improves fluency
- **Reliability**: Validation loop prevents over-corrections
- **Accuracy**: 96.23% success rate on diverse test cases

## Features

### Core Capabilities
- **Hybrid Grammar Correction**: Combines LanguageTool rule-based checking with AI-powered Grammarly CoEdit model
- **Dual-Pass Refinement**: First pass uses LanguageTool, second pass uses CoEdit-Large model
- **REST API**: FastAPI-based endpoint for programmatic access with full request validation
- **Interactive Web UI**: Beautiful, responsive interface with real-time grammar checking
- **Comprehensive Issue Detection**: Identifies grammar errors, spelling, style, punctuation, and more
- **Contextual Analysis**: Returns context for each detected issue to help users understand the error
- **GPU Acceleration**: Supports CUDA for dramatically faster AI model inference (50% faster)
- **Intelligent Text Chunking**: Handles long documents by splitting intelligently (max 180 words per chunk)
- **Smart Filtering**: Removes false positives by filtering noisy rules

### Supported Error Categories

The system reliably corrects:
- ✅ **Articles** (a/an/the usage)
- ✅ **Capitalization** (proper nouns, sentence starts)
- ✅ **Possessives** (apostrophe placement)
- ✅ **Prepositions** (in/on/at/by, etc.)
- ✅ **Pronouns** (he/she/they agreement)
- ✅ **Punctuation** (commas, periods, semicolons)
- ✅ **Spelling** (typos and misspellings)
- ✅ **Subject-Verb Agreement** (plural/singular matching)
- ✅ **Tense** (past, present, future consistency)
- ✅ **Mixed Errors** (combination of multiple issues)

## Technology Stack

### Backend Architecture
| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Web Framework** | FastAPI | 0.136.3 | Modern async API server |
| **ASGI Server** | Uvicorn | Latest | Production-ready server |
| **Grammar Engine** | language-tool-python | 3.4 | Rule-based error detection |
| **AI Model** | Transformers (Hugging Face) | Latest | Pre-trained NLP models |
| **Deep Learning** | PyTorch | 2.x | GPU-accelerated inference |
| **Data Validation** | Pydantic | 2.13.4 | Request/response validation |
| **Templating** | Jinja2 | 3.1.6 | HTML template rendering |

### Frontend Stack
- **HTML5**: Semantic markup
- **CSS3**: Responsive design with custom styling
- **Canvas API**: Animated star background effects
- **Vanilla JavaScript**: DOM manipulation and API communication
- **Design**: Pink/dreamy theme with accessibility considerations

### Key Dependencies Explained
```
Core Processing:
  - torch: GPU-enabled tensor operations
  - transformers: State-of-the-art NLP models
  - language-tool-python: Comprehensive grammar rules

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
│   ├── aicorrector.py         # AI model integration and inference
│   ├── schemas.py             # Pydantic data models and validators
│   ├── rules.py               # Grammar rules configuration and management
│
├── evaluation/                 # Quality assurance
│   ├── __init__.py
│   ├── evaluate.py            # Test execution and reporting
│   └── test_cases.json        # 53 test cases with expected outputs
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
│  3. Apply first corrections                              │
│  4. Call AI corrector                                    │
│  5. Final LanguageTool validation pass                   │
└────┬────────────────────────────┬───────────────────────┘
     │                            │
     ▼                            ▼
┌──────────────────┐    ┌──────────────────────────┐
│  LanguageTool    │    │   AI Corrector Service   │
│ (Rule-based)     │    │ (services/aicorrector.py)│
│                  │    │                          │
│ • 50+ grammar    │    │ • CoEdit-Large model     │
│   rules          │    │ • GPU acceleration       │
│ • English US     │    │ • Text chunking (180w)   │
│ • 5 suggestions  │    │ • Beam search (b=2)      │
│ • Fast matching  │    │ • Context aware          │
└──────────────────┘    └──────────────────────────┘
```

## Installation & Setup

### Prerequisites
Before installation, ensure you have:
- **Python 3.8+** (tested on 3.10 and 3.11)
- **pip** package manager
- **Virtual environment** support (venv or conda)
- **8GB+ RAM** for comfortable operation
- **GPU (Optional)**: CUDA 11.8+ for ~50% faster inference
- **~4GB Disk Space**: For model weights and dependencies

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

# For GPU support (CUDA 11.8+)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### 4. Verify Installation
```bash
# Check Python version
python --version

# Test FastAPI
python -c "import fastapi; print(f'FastAPI {fastapi.__version__}')"

# Test PyTorch
python -c "import torch; print(f'PyTorch {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"

# Test language tools
python -c "import language_tool_python; print('Language Tool ready')"
```

#### 5. Download Models (Automatic on First Run)
```bash
# Models will download automatically when the app first runs
# Or manually pre-download:
python -c "from transformers import AutoModel; AutoModel.from_pretrained('grammarly/coedit-large')"
```

## Running the Application

### Development Server
```bash
# Run with hot-reload for development
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Output:
# INFO:     Uvicorn running on http://0.0.0.0:8000
# INFO:     Application startup complete
# INFO:     Uvicorn running on http://0.0.0.0:8000
```

Then open: `http://localhost:8000/dreamy-checker`

### Production Server
```bash
# Multi-worker production setup
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# With custom timeout
uvicorn main:app --host 0.0.0.0 --port 8000 --timeout-keep-alive 600
```

### Docker Deployment (Optional)
```bash
# Build image
docker build -t dreamy-checker .

# Run container
docker run -p 8000:8000 --gpus all dreamy-checker
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



**Model Details**:
- **Name**: grammarly/coedit-large
- **Type**: Seq2Seq Transformer
- **Training Data**: Extensive grammar correction corpus
- **Output**: Natural, grammatically correct text

**Inference Process**:
1. Split text into chunks (max 180 words)
2. Add "grammar: " prefix for task specification
3. Tokenize with max_length=512
4. Generate with beam search (num_beams=2)
5. Decode output skipping special tokens
6. Combine all chunks with space separator

**GPU Acceleration**:
- Automatically detects CUDA availability
- Falls back to CPU if GPU unavailable
- 50% faster on GPU for typical requests


``

DREAMY CHECKER EVALUATION REPORT



### Detailed Analysis

**Performance Metrics**:
- **Overall Success Rate**: 96.23% (51 of 53 tests passing)
- **Perfect Categories**: 8 out of 10 (80%)
- **Average Processing Time**: 1.41 seconds
- **Precision**: High confidence in corrections
- **Recall**: Catches most errors

**Category Performance**:

| Category | Tests | Passed | Rate | Status |
|----------|-------|--------|------|--------|
| Articles | 5 | 5 | 100% | ✓ Excellent |
| Capitalization | 5 | 5 | 100% | ✓ Excellent |
| Mixed Errors | 6 | 6 | 100% | ✓ Excellent |
| Possessives | 5 | 5 | 100% | ✓ Excellent |
| Prepositions | 5 | 5 | 100% | ✓ Excellent |
| Pronouns | 6 | 5 | 83% | ⚠ Good |
| Punctuation | 5 | 5 | 100% | ✓ Excellent |
| Spelling | 5 | 5 | 100% | ✓ Excellent |
| Subject-Verb Agr. | 5 | 5 | 100% | ✓ Excellent |
| Tense | 6 | 5 | 83% | ⚠ Good |

**Strengths**:
- Exceptional at structural errors (articles, prepositions)
- Perfect spelling and capitalization correction
- Handles complex mixed errors well
- Fast processing even on CPU

**Areas for Improvement**:
- Pronoun disambiguation (5/6 cases)
- Complex tense shifts (5/6 cases)



### Running Tests

```bash
# Execute full evaluation suite
python -m evaluation.evaluate

# Output includes:
# - Overall success rate
# - Category-by-category breakdown
# - Average response time
# - Failed case details
```





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
| First request slow | Model loading | Normal, 3-5s expected |
| Subsequent requests slow | CPU inference | Enable GPU |
| Memory errors | Models too large | Reduce batch size |
| Hanging requests | Bad text input | Validate input |
| No output | Network issue | Check API connection |


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
docker build -t dreamy-checker .
docker run -p 8000:8000 --gpus all dreamy-checker
```

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request


---

**Last Updated**: June 2026\
**Status**: Production Ready (v1.0)\
**Test Coverage**: 96.23% accuracy across 53 test cases