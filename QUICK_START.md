# 🚀 Quick Start Guide

## Get Running in 5 Minutes!

### 1️⃣ Setup Items API (2 minutes)

```bash
cd items_api
./setup.sh
```

Or manually:
```bash
cd items_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Test Locally (1 minute)

```bash
# Start the API
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# In another terminal, test it:
curl http://localhost:8000/

# Create some items:
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '[{"name": "Test Item", "price": 100}]'

# Get all items:
curl http://localhost:8000/items
```

Open http://localhost:8000/docs for interactive API documentation!

### 3️⃣ Setup Systemd Services (1 minute)

For **Items API**:
```bash
# Edit the service file (replace YOUR_USERNAME and paths)
nano items_api/items-api.service

# Copy and enable
sudo cp items_api/items-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable items-api
sudo systemctl start items-api
sudo systemctl status items-api
```

For **Simple HTTP Service**:
```bash
# Edit the service file
nano simple_http_service/simple-http.service

# Copy and enable
sudo cp simple_http_service/simple-http.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable simple-http
sudo systemctl start simple-http
sudo systemctl status simple-http
```

### 4️⃣ Expose with ngrok (1 minute)

```bash
# Install ngrok (if not installed)
# Visit: https://ngrok.com/download

# Authenticate
ngrok config add-authtoken YOUR_TOKEN_HERE

# Expose Items API (in one terminal)
ngrok http 8000

# Expose HTTP Service (in another terminal)
ngrok http 9000
```

## ✅ Done!

You now have:
- ✅ Items API running on port 8000
- ✅ Simple HTTP Service on port 9000
- ✅ Both services auto-start with system
- ✅ Both services exposed via ngrok

### 📱 Share These URLs:

- **Items API**: `https://YOUR_NGROK_URL.ngrok.app/docs`
- **HTTP Service**: `https://YOUR_NGROK_URL.ngrok.app/`

---

## 🧪 Quick Test Commands

```bash
# Test Items API
curl https://YOUR_NGROK_URL.ngrok.app/items

# Create items
curl -X POST https://YOUR_NGROK_URL.ngrok.app/items \
  -H "Content-Type: application/json" \
  -d '[
    {"name": "Lapiz", "price": 1200.50},
    {"name": "Cuaderno", "price": 3500}
  ]'

# View items
curl https://YOUR_NGROK_URL.ngrok.app/items
```

---

For detailed documentation, see [README.md](README.md)

