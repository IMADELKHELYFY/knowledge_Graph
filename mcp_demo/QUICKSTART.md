# 🚀 Quick Start Guide - Running the MCP Server

## Step 1: Start the Server

Open a terminal in the `mcp_demo` folder and run:

```bash
python server.py
```

You should see:
```
======================================================================
🚀 Starting Clinisys Finance Invoice MCP Server
======================================================================

📋 Available Invoices in Mock Database:
   • INV-2024-001: Dell Technologies - $45,000.00 (PAID)
   • INV-2024-002: Microsoft Corporation - $125,000.00 (PENDING)
   • INV-2024-003: Oracle Corporation - $78,000.00 (OVERDUE)

🔧 Server running on: http://localhost:8000
📖 API Docs: http://localhost:8000/docs
🏥 Health Check: http://localhost:8000/health
```

**Keep this terminal open!** The server needs to stay running.

---

## Step 2: Test the Server

Open a **NEW terminal** (keep the first one running) and run:

```bash
python test_client.py
```

This will run 6 automated tests showing:
- ✅ Successful invoice retrieval
- ✅ Error handling for missing invoices
- ✅ Error handling for invalid tools

---

## Step 3: Explore the API (Optional)

While the server is running, open your browser and visit:

**Interactive API Documentation:**
http://localhost:8000/docs

Here you can:
- See all available endpoints
- Test the API directly in the browser
- View request/response schemas

---

## Alternative: Manual Testing with curl

```bash
# Test 1: Get Microsoft invoice
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get_invoice_details",
      "arguments": {"invoice_id": "INV-2024-002"}
    },
    "id": "1"
  }'
```

---

## Stopping the Server

In the terminal where the server is running, press:
```
Ctrl + C
```

---

## Troubleshooting

**Problem:** Port 8000 already in use
**Solution:** Change the port in `server.py` (last line):
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Use 8001 instead
```

**Problem:** Module not found
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```
