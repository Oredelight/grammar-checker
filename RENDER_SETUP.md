# Render Deployment Setup - Local LanguageTool Server (Docker)

## Changes Made

1. **Dockerfile** — Builds a Docker image with Java runtime and Python dependencies
2. **render.yaml** — Configuration for Docker deployment
3. **grammarchecker.py** — Uses local LanguageTool server instead of public API

## Render Configuration Steps

### Option 1: Using Render Dashboard (Recommended)
1. Go to your Render service
2. Click **Settings**
3. Under **Build & Deploy**, change **Environment** from "Python" to "Docker"
4. Save and click **Deploy**
5. Render will automatically detect the Dockerfile and build from it

### Option 2: Using render.yaml
- The `render.yaml` file is already configured for Docker deployment
- Just push your changes and redeploy

## How It Works

1. Render detects `Dockerfile` in your repository
2. Builds a Docker image that:
   - Starts with Python 3.11 slim image
   - Installs Java runtime (required for LanguageTool server)
   - Installs Python dependencies from `requirements.txt`
   - Runs your FastAPI app on port 8000
3. Local LanguageTool server starts automatically with your app

## Benefits

✅ Java installed without read-only filesystem issues  
✅ No rate limits — unlimited local grammar checking  
✅ Full control over runtime environment  
✅ Automatic fallback to AI if LanguageTool fails  
✅ Free (included in Render pricing)

## Troubleshooting

- **Build is slow?** First Docker build takes 3-5 minutes due to Java installation. Subsequent deploys are faster.
- **Out of memory?** Upgrade to a larger Render plan if needed.
- **LanguageTool not starting?** Check deploy logs. Service automatically falls back to AI corrections.
- **Want to verify Java is installed?** Check deploy logs for "default-jre" installation messages.
