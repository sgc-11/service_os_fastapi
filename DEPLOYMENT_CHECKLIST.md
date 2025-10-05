# ✅ Deployment Checklist

Use this checklist to complete your homework step by step.

---

## 📋 Pre-Deployment

### Local Development Setup

- [ ] Navigate to project directory: `cd items_api`
- [ ] Run setup script: `./setup.sh` (or manually create venv and install)
- [ ] Activate virtual environment: `source venv/bin/activate`
- [ ] Start API locally: `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`
- [ ] Test in browser: http://localhost:8000/docs
- [ ] Test GET endpoint: `curl http://localhost:8000/items`
- [ ] Test POST endpoint: `./test_api.sh`
- [ ] Verify database created: `ls -la items.db`

---

## 🔧 Systemd Service 1: Items API

### Configure Service File

- [ ] Open `items_api/items-api.service`
- [ ] Replace `YOUR_USERNAME` with your actual username (e.g., `ubuntu`, `student`)
- [ ] Replace `/path/to/items_api` with full absolute path (e.g., `/home/ubuntu/OS_2025_2/items_api`)
- [ ] Save the file

### Install and Enable Service

```bash
# Copy service file
sudo cp items_api/items-api.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable service (auto-start on boot)
sudo systemctl enable items-api

# Start service now
sudo systemctl start items-api

# Check status
sudo systemctl status items-api
```

- [ ] Service file copied to `/etc/systemd/system/`
- [ ] systemd reloaded
- [ ] Service enabled
- [ ] Service started
- [ ] Status shows "active (running)"

### Troubleshooting (if needed)

If service fails:
```bash
# View logs
sudo journalctl -u items-api -n 50 --no-pager

# Check permissions
ls -la items_api/

# Fix ownership if needed
sudo chown -R $USER:$USER items_api/
```

- [ ] No errors in logs
- [ ] Service running successfully

---

## 🔧 Systemd Service 2: Simple HTTP Server

### Configure Service File

- [ ] Open `simple_http_service/simple-http.service`
- [ ] Replace `YOUR_USERNAME` with your actual username
- [ ] Replace `/path/to/simple_http_service` with full absolute path
- [ ] Save the file

### Install and Enable Service

```bash
# Copy service file
sudo cp simple_http_service/simple-http.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable service
sudo systemctl enable simple-http

# Start service
sudo systemctl start simple-http

# Check status
sudo systemctl status simple-http
```

- [ ] Service file copied
- [ ] systemd reloaded
- [ ] Service enabled
- [ ] Service started
- [ ] Status shows "active (running)"

### Test Local HTTP Service

```bash
# Test in browser
curl http://localhost:9000

# Or open in browser
# http://localhost:9000
```

- [ ] HTTP service responding
- [ ] HTML page loads correctly

---

## 🌐 ngrok Setup

### Install ngrok

- [ ] Go to https://ngrok.com
- [ ] Create free account
- [ ] Download ngrok for your OS
- [ ] Extract and install ngrok

```bash
# Linux/Mac example
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin/
```

- [ ] ngrok installed
- [ ] `ngrok version` works

### Configure ngrok

- [ ] Go to https://dashboard.ngrok.com/get-started/your-authtoken
- [ ] Copy your authtoken
- [ ] Run: `ngrok config add-authtoken YOUR_TOKEN`

```bash
ngrok config add-authtoken YOUR_ACTUAL_TOKEN_HERE
```

- [ ] Authtoken configured

---

## 🚀 Expose Services with ngrok

### Expose Items API (Port 8000)

Open a new terminal window:

```bash
ngrok http 8000
```

- [ ] ngrok running for port 8000
- [ ] Public URL displayed (e.g., `https://abc123.ngrok.app`)
- [ ] **SAVE THIS URL**: ____________________________

### Test Public Items API

```bash
# Test with your ngrok URL
curl https://YOUR_NGROK_URL.ngrok.app/

# Test docs
# Open in browser: https://YOUR_NGROK_URL.ngrok.app/docs

# Test POST
curl -X POST https://YOUR_NGROK_URL.ngrok.app/items \
  -H "Content-Type: application/json" \
  -d '[{"name": "Test", "price": 100}]'

# Test GET
curl https://YOUR_NGROK_URL.ngrok.app/items
```

- [ ] Public URL accessible
- [ ] API docs work
- [ ] POST creates items
- [ ] GET returns items

### Expose Simple HTTP Service (Port 9000)

Open another new terminal window:

```bash
ngrok http 9000
```

- [ ] ngrok running for port 9000
- [ ] Public URL displayed
- [ ] **SAVE THIS URL**: ____________________________

### Test Public HTTP Service

```bash
# Test with your ngrok URL
curl https://YOUR_NGROK_URL.ngrok.app/

# Or open in browser
```

- [ ] Public URL accessible
- [ ] HTML page loads

---

## 📸 Documentation for Submission

### Screenshots to Take

- [ ] Screenshot: systemd status for `items-api` service
- [ ] Screenshot: systemd status for `simple-http` service
- [ ] Screenshot: ngrok terminal showing Items API tunnel
- [ ] Screenshot: ngrok terminal showing HTTP service tunnel
- [ ] Screenshot: Items API docs page (https://xxx.ngrok.app/docs)
- [ ] Screenshot: Simple HTTP service webpage
- [ ] Screenshot: Successful API test (POST and GET)

### Commands to Save Output

```bash
# Service statuses
sudo systemctl status items-api > service1_status.txt
sudo systemctl status simple-http > service2_status.txt

# Test outputs
./test_api.sh https://YOUR_API_URL.ngrok.app > api_test_results.txt
```

- [ ] All screenshots taken
- [ ] Output files saved

---

## 🎓 Final Verification

### Both Services Running

```bash
sudo systemctl status items-api
sudo systemctl status simple-http
```

- [ ] Both services show "active (running)"
- [ ] Both services enabled (will start on boot)

### Both Services Publicly Accessible

- [ ] Items API URL works from another device/network
- [ ] Simple HTTP URL works from another device/network

### Reboot Test (Optional but Recommended)

```bash
sudo reboot
```

After reboot:
```bash
# Check both services auto-started
sudo systemctl status items-api
sudo systemctl status simple-http
```

- [ ] Services auto-started after reboot

---

## 📝 Submission Package

Prepare the following for submission:

- [ ] All source code files
- [ ] Service configuration files
- [ ] Screenshots of running services
- [ ] Public ngrok URLs (documented)
- [ ] Test results
- [ ] This completed checklist

---

## 🆘 Common Issues and Solutions

### Issue: Service fails to start

**Solution:**
```bash
# Check logs
sudo journalctl -u items-api -n 50

# Common fixes:
# 1. Check paths in service file are absolute
# 2. Check user has permission to access files
# 3. Check venv exists and has packages installed
```

### Issue: Port already in use

**Solution:**
```bash
# Find what's using the port
sudo lsof -i :8000

# Kill the process if needed
sudo kill -9 PID
```

### Issue: ngrok "connection refused"

**Solution:**
- Verify service is running locally first
- Test with `curl http://localhost:8000`
- Check firewall settings

### Issue: Permission denied

**Solution:**
```bash
# Fix ownership
sudo chown -R $USER:$USER items_api/
sudo chown -R $USER:$USER simple_http_service/

# Fix permissions
chmod +x items_api/setup.sh
chmod +x test_api.sh
```

---

## ✅ Completion Criteria

You're done when:

- [x] Both services run as systemd services
- [x] Both services start automatically on boot
- [x] Both services are publicly accessible via ngrok
- [x] Items API can create and retrieve items
- [x] All tests pass
- [x] Documentation complete

---

## 🎉 Congratulations!

You've successfully completed the OS 2025-2 project!

**Your URLs to submit:**
- Items API: ____________________________
- Simple HTTP Service: ____________________________

---

**Prepared:** October 2025  
**Project:** OS 2025-2 Homework  
**Status:** Ready for Deployment ✅

