#!/bin/bash
# Quick test script for Items API

API_URL="${1:-http://localhost:8000}"

echo "🧪 Testing Items API at: $API_URL"
echo ""

# Test 1: Root endpoint
echo "1️⃣ Testing root endpoint..."
curl -s "$API_URL/" | python3 -m json.tool
echo ""

# Test 2: Get items (should be empty initially)
echo "2️⃣ Getting all items (initial)..."
curl -s "$API_URL/items" | python3 -m json.tool
echo ""

# Test 3: Create items
echo "3️⃣ Creating items..."
curl -s -X POST "$API_URL/items" \
  -H "Content-Type: application/json" \
  -d '[
    {"name": "Lapiz", "price": 1200.50},
    {"name": "Cuaderno", "price": 3500},
    {"name": "Borrador", "price": 800}
  ]' | python3 -m json.tool
echo ""

# Test 4: Get all items again
echo "4️⃣ Getting all items (after creation)..."
curl -s "$API_URL/items" | python3 -m json.tool
echo ""

echo "✅ Tests completed!"
echo ""
echo "To test with ngrok URL:"
echo "  ./test_api.sh https://your-url.ngrok.app"

