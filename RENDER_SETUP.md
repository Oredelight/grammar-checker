# Render Deployment Setup - Local LanguageTool Server

## Changes Made

1. **build.sh** — Build script that installs Java runtime before installing Python dependencies
2. **render.yaml** — Configuration file for Render deployment
3. **grammarchecker.py** — Updated to use local LanguageTool server instead of public API

## Render Configuration Steps

1. **Push your changes** to your GitHub repository (including `build.sh` and `render.yaml`)

2. **In Render Dashboard:**
   - Go to your Web Service
   - Click **Settings**
   - Scroll to **Build & Deploy**
   - Change **Build Command** to: `./build.sh`
   - Change **Start Command** to: `python -m uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Alternative (If using render.yaml):**
   - Render can read `render.yaml` automatically
   - Make sure the file is in your repository root
   - Redeploy to apply settings

4. **Deploy**
   - Click **Deploy** to trigger a new build
   - The build will now install Java and use the local LanguageTool server

## Benefits

✅ No rate limits — local server can handle unlimited requests  
✅ No Java dependency errors — Java is installed during build  
✅ Fallback to AI — if LanguageTool fails to start, uses AI corrections only  
✅ Free — no additional costs beyond Render hosting

## Troubleshooting

- If build takes >30 minutes, Java download might timeout (increase build timeout in Render)
- Check deploy logs for "LanguageTool" to verify it initialized successfully
- If local server fails to start, you'll automatically fall back to AI corrections
