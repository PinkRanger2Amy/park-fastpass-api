# DEPLOYMENT GUIDE

## 🚀 Heroku Deployment

### Prerequisites
- Heroku CLI installed
- GitHub repository connected

### Step 1: Install Heroku CLI
```bash
brew install heroku/brew/heroku
heroku login
```

### Step 2: Create Heroku App
```bash
cd /Users/amarissneed/Desktop/ParkTickets/secure-payment-api
heroku create park-fastpass-api
```

### Step 3: Set Environment Variables
```bash
heroku config:set ENVIRONMENT=production
heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
```

### Step 4: Deploy
```bash
git push heroku main
```

### Step 5: Seed Database
```bash
heroku run python scripts/seed_rides.py
```

Visit: `https://park-fastpass-api.herokuapp.com`

---

## 🚀 Railway Deployment

### Step 1: Connect GitHub
1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Connect your GitHub account
5. Select `park-fastpass-api` repository

### Step 2: Configure
- Service: Python
- Build command: `pip install -r backend/requirements.txt`
- Start command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Step 3: Deploy
Railway auto-deploys on push to main!

---

## 🚀 AWS Deployment

### Using Elastic Beanstalk

```bash
# Install EB CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 park-fastpass-api

# Create environment
eb create park-fastpass-prod

# Deploy
eb deploy

# Open application
eb open
```

### Using EC2 + RDS

1. Launch EC2 instance (Ubuntu 20.04)
2. SSH into instance
3. Clone repository
4. Install dependencies
5. Configure Nginx reverse proxy
6. Set up RDS database
7. Deploy with Gunicorn/Supervisor

---

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -f backend/Dockerfile -t park-fastpass:latest .
```

### Run Container
```bash
docker run -p 8765:8765 \
  -e DATABASE_URL="sqlite:///./tickets.db" \
  park-fastpass:latest
```

### Docker Compose
```bash
docker-compose up --build
```

---

## 📊 Monitoring & Logging

### Heroku Logs
```bash
heroku logs --tail
```

### Error Tracking (Sentry)
1. Sign up at https://sentry.io
2. Install: `pip install sentry-sdk`
3. Configure in app/main.py:
```python
import sentry_sdk
sentry_sdk.init("YOUR_SENTRY_DSN")
```

---

## 🔒 Security Checklist

- [ ] Set strong SECRET_KEY in production
- [ ] Use HTTPS only
- [ ] Enable CORS restrictions
- [ ] Use environment variables for secrets
- [ ] Regular dependency updates
- [ ] Database backups enabled
- [ ] Rate limiting configured
- [ ] Input validation in place

---

## 📈 Performance Optimization

- Enable caching headers
- Use CDN for static assets
- Database indexing on frequently queried fields
- Connection pooling for database
- API rate limiting

---

## 🆘 Troubleshooting

### Port already in use
```bash
lsof -i :8765
kill -9 <PID>
```

### Database errors
```bash
python scripts/seed_rides.py
```

### Import errors
```bash
pip install -r requirements.txt
```

### CORS issues
Check `main.py` CORS middleware configuration

---

For more help, visit the GitHub repository:
https://github.com/Pinkranger2Amy/park-fastpass-api
