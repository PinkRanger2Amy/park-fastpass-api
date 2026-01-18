# Park FastPass - Heroku Deployment Guide

## 🚀 Quick Heroku Deployment (5 minutes)

### Prerequisites
- Heroku account (https://signup.heroku.com)
- Heroku CLI installed ✅
- Git repository initialized ✅

### Step-by-Step Deployment

#### 1️⃣ **Login to Heroku**
```bash
heroku login
# Enter your Heroku credentials
```

#### 2️⃣ **Create Heroku App**
```bash
cd /Users/amarissneed/Desktop/ParkTickets/secure-payment-api

# Create app with custom name
heroku create park-fastpass-amy

# OR let Heroku choose a name
heroku create
```

#### 3️⃣ **Set Environment Variables**
```bash
# Set production environment
heroku config:set ENVIRONMENT=production

# Generate secure secret key
heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')

# Optional: Set database URL (uses SQLite by default)
heroku config:set DATABASE_URL=sqlite:///./tickets.db
```

#### 4️⃣ **Deploy Your Code**
```bash
# Push to Heroku
git push heroku main

# Wait for build to complete...
```

#### 5️⃣ **View Deployment Logs**
```bash
# Real-time logs
heroku logs --tail

# Recent logs (last 50 lines)
heroku logs -n 50
```

#### 6️⃣ **Open Your App**
```bash
heroku open
```

Your app will be live at: `https://park-fastpass-amy.herokuapp.com`

---

## 🔧 Useful Heroku Commands

### View Configuration
```bash
heroku config          # View all environment variables
heroku info            # App information
heroku apps            # List your apps
```

### Scale Dynos
```bash
heroku ps:scale web=1  # 1 web dyno
heroku ps               # View running dynos
```

### Run Commands
```bash
heroku run python scripts/seed_rides.py     # Seed rides
heroku run python -c "import app"           # Run Python code
heroku run bash                              # Interactive shell
```

### Manage Add-ons
```bash
heroku addons:create heroku-postgresql:hobby-dev   # PostgreSQL
heroku addons                                       # List add-ons
```

### Debugging
```bash
heroku logs --tail                          # Live logs
heroku logs --tail -d router                # Router logs
heroku ps:exec                              # SSH into dyno
```

### Maintenance
```bash
heroku maintenance:on                       # Enable maintenance mode
heroku maintenance:off                      # Disable maintenance mode
heroku releases                             # View deployment history
heroku rollback v5                          # Rollback to version 5
```

---

## 📊 Monitoring

### View Performance
```bash
heroku logs --tail
heroku ps aux
```

### Check Status
```bash
heroku status
```

---

## 🔐 Security Checklist

- ✅ Set strong `SECRET_KEY`
- ✅ Use `HTTPS` (automatic with Heroku)
- ✅ Don't commit `.env` file
- ✅ Use environment variables for secrets
- ✅ Enable two-factor authentication on Heroku
- ✅ Regularly update dependencies

---

## 🆘 Troubleshooting

### Build Errors
```bash
# Check build logs
heroku logs

# Rebuild
git push heroku main --force
```

### Runtime Errors
```bash
# View error logs
heroku logs --tail

# Check dyno status
heroku ps
```

### Database Issues
```bash
# Seed the database
heroku run python scripts/seed_rides.py

# Check database connection
heroku config | grep DATABASE_URL
```

### Port Issues
```bash
# The Procfile specifies the port
# Make sure app listens on $PORT variable
```

---

## 💰 Pricing

**Free Tier:**
- 550 free dyno hours/month
- Sleep after 30 mins of inactivity
- Suitable for development/testing

**Paid Tiers:**
- Standard: $7-50/month
- Performance: $25-250+/month

---

## 📚 Additional Resources

- [Heroku Python Support](https://devcenter.heroku.com/articles/python-support)
- [Procfile Guide](https://devcenter.heroku.com/articles/procfile)
- [Environment Variables](https://devcenter.heroku.com/articles/config-vars)
- [Deploying Python Apps](https://devcenter.heroku.com/articles/getting-started-with-python)

---

## 🎉 Success!

Once deployed, you can:
- Access API at: `https://park-fastpass-amy.herokuapp.com/api`
- View docs at: `https://park-fastpass-amy.herokuapp.com/docs`
- Monitor at: https://dashboard.heroku.com

---

**Need help?** Check `heroku --help` or visit https://devcenter.heroku.com
