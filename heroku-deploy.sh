#!/bin/bash
# Park FastPass Heroku Deployment Script

echo "🚀 Park FastPass Heroku Deployment"
echo "=================================="
echo ""

# Step 1: Login to Heroku
echo "📝 Step 1: Login to Heroku"
echo "Run: heroku login"
echo ""

# Step 2: Create Heroku app
echo "🔨 Step 2: Create Heroku App"
echo "Run: heroku create park-fastpass-amy"
echo ""

# Step 3: Set environment variables
echo "⚙️  Step 3: Set Environment Variables"
echo "Run the following commands:"
echo ""
echo "heroku config:set ENVIRONMENT=production"
echo "heroku config:set SECRET_KEY=\$(python -c 'import secrets; print(secrets.token_hex(32))')"
echo ""

# Step 4: Add Heroku remote
echo "🔗 Step 4: Add Heroku Remote"
echo "Run: git remote add heroku https://git.heroku.com/park-fastpass-amy.git"
echo ""

# Step 5: Deploy
echo "📤 Step 5: Deploy to Heroku"
echo "Run: git push heroku main"
echo ""

# Step 6: View logs
echo "📊 Step 6: View Deployment Logs"
echo "Run: heroku logs --tail"
echo ""

# Step 7: Access the app
echo "🌐 Step 7: Open Your App"
echo "Run: heroku open"
echo ""

echo "=================================="
echo "✅ Deployment steps ready!"
