# Deploy OpenAlgo to Production

## Current Status
- ✅ All configurations updated for production domain
- ✅ 25 Python strategies configured and ready
- ✅ Datetime serialization bug fixed
- ✅ Dhan API credentials configured
- ⚠️ Need to deploy to server where https://algo.endoscopicspinehyderabad.in points

## Deployment Options

### Option 1: Deploy to Your Server via Git

```bash
# On your production server (where algo.endoscopicspinehyderabad.in points):

# 1. Pull latest changes
cd /path/to/openalgo
git pull origin main

# 2. Copy your local .env to the server
# (or update .env on server with new credentials)

# 3. Restart Docker containers
docker-compose down
docker-compose build
docker-compose up -d

# 4. Check logs
docker logs -f openalgo-web
```

### Option 2: Deploy from Your Mac

```bash
# 1. Commit your changes
cd /Users/mac/openalgo/openalgo
git add .
git commit -m "Update Dhan credentials and fix datetime bug"
git push origin main

# 2. SSH to your production server
ssh your-server

# 3. Pull and restart (on server)
cd /path/to/openalgo
git pull
docker-compose restart

# 4. Or rebuild if needed
docker-compose down && docker-compose up -d --build
```

### Option 3: Direct File Transfer

```bash
# Copy .env and updated files to production server
scp /Users/mac/openalgo/openalgo/.env user@server:/path/to/openalgo/
scp /Users/mac/openalgo/openalgo/strategies/utils/strategy_common.py user@server:/path/to/openalgo/strategies/utils/
scp /Users/mac/openalgo/openalgo/utils/env_check.py user@server:/path/to/openalgo/utils/

# Then SSH and restart
ssh user@server
cd /path/to/openalgo
docker-compose restart
```

## Key Files Updated

1. **/.env** - Production URLs and Dhan credentials
2. **/strategies/utils/strategy_common.py** - Fixed datetime serialization
3. **/utils/env_check.py** - Disabled strict Dhan key validation

## After Deployment

1. **Verify server is running:**
   ```bash
   curl https://algo.endoscopicspinehyderabad.in/
   ```

2. **Complete Dhan OAuth:**
   - Go to: https://algo.endoscopicspinehyderabad.in/brlogin
   - Select "Dhan" broker
   - Click "Connect to Broker"
   - Complete authentication

3. **Verify strategies:**
   - Go to: https://algo.endoscopicspinehyderabad.in/pythonstrategy
   - Check status of 25 strategies
   - They should auto-start during market hours (09:15-15:30 IST)

## Production Server Configuration

### Required in Dhan API Portal:
- **Redirect URL**: https://algo.endoscopicspinehyderabad.in/dhan/callback
- **API Key**: 95329be4
- **API Secret**: 4ef8b142-4df3-4c96-b1e0-38f7d885ef45

### Environment Variables (.env):
```bash
BROKER_API_KEY = '95329be4'
BROKER_API_SECRET = '4ef8b142-4df3-4c96-b1e0-38f7d885ef45'
REDIRECT_URL = 'https://algo.endoscopicspinehyderabad.in/dhan/callback'
HOST_SERVER = 'https://algo.endoscopicspinehyderabad.in'
```

## Troubleshooting

### If strategies don't start:
1. Check broker authentication: Dashboard → Check for "Invalid Token" errors
2. Check market hours: Strategies only run 09:15-15:30 IST weekdays
3. Check logs: `docker logs openalgo-web`

### If OAuth fails:
1. Verify redirect URL in Dhan portal matches exactly
2. Check API credentials are active
3. Try restarting container: `docker-compose restart`

## Next Steps

After deployment:
1. SSH to your production server
2. Pull latest code or copy updated files
3. Restart Docker container
4. Complete Dhan OAuth login
5. Strategies will auto-start during market hours

---

**Your server location**: Wherever algo.endoscopicspinehyderabad.in DNS points to
**Local instance**: Running on http://127.0.0.1:5002 (for testing only)
