# 🚀 Deployment Guide (Render)

Deploying your **DiabetesAI** system to the web is simple using [Render](https://render.com/). Follow these steps:

## 1. Prepare your Code
I have already prepared the following files for you:
- `requirements.txt`: Includes `gunicorn` (the production web server).
- `Procfile`: Tells Render how to run your app (`web: gunicorn run:app`).
- `.gitignore`: Ensures we don't upload the virtual environment.

## 2. Push to GitHub
1. Create a new repository on [GitHub](https://github.com/new).
2. Initialize and push your local code:
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

## 3. Deploy on Render
1. Create a free account on [Render.com](https://render.com/).
2. Click **"New +"** and select **"Web Service"**.
3. Connect your GitHub repository.
4. Use the following settings:
   - **Name**: `diabetes-prediction-ai` (or your choice)
   - **Environment**: `Python`
   - **Region**: Select the one closest to you.
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app`
5. Click **"Create Web Service"**.

## 4. That's it! 🥳
Render will build your app and give you a public URL (e.g., `https://diabetes-prediction-ai.onrender.com`).

---
**Note:** The first load might take a minute on Render's free tier if the server has "spun down" due to inactivity.
