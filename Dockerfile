FROM python:3.11-slim

# Install Java
RUN apt-get update && apt-get install -y \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download LanguageTool during build
RUN python -c "import language_tool_python; language_tool_python.LanguageTool('en-US')" || true

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
