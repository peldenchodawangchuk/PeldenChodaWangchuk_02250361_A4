# My DevOps Web App – Assignment IV (DSO101)

A simple Flask web application deployed using GitHub Actions (CI/CD) and Render.

---

## Live URL

https://peldenchodawangchuk-02250361-a4.onrender.com
---

## Tools Used

- **GitHub** – Version control and repository hosting
- **GitHub Actions** – CI/CD pipeline automation
- **Render** – Cloud deployment platform
- **Flask** – Python web framework
- **Gunicorn** – WSGI server for production

---

## Project Structure

```
my-devops-app/
├── app.py                        # Main Flask application
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .github/
    └── workflows/
        └── deploy.yml            # GitHub Actions CI/CD workflow
```

---

## Setup Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### Step 2: Install Dependencies Locally
```bash
pip install -r requirements.txt
```

### Step 3: Run the App Locally
```bash
python app.py
```
Open your browser at `http://127.0.0.1:5000`

---

## CI/CD with GitHub Actions

Every time code is pushed to the `main` branch:
1. GitHub Actions automatically triggers the workflow defined in `.github/workflows/deploy.yml`
2. It checks out the code, sets up Python, and installs dependencies
3. Render detects the push and automatically redeploys the application

---

## Deployment on Render

1. Go to [https://render.com](https://render.com) and sign in with GitHub
2. Click **New → Web Service**
3. Connect your GitHub repository
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy**

---

##  Common Errors & Fixes

| Problem | Solution |
|---|---|
| App not starting | Ensure start command is `gunicorn app:app` |
| Build failed | Check `requirements.txt` has `flask` and `gunicorn` |
| Deployment fails | Reconnect GitHub repo in Render settings |

---
