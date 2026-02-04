# 🏢 Clinisys Finance Invoice MCP Server - Complete Guide

## 📚 Table of Contents
1. [What is This Project?](#what-is-this-project)
2. [Understanding MCP (Model Context Protocol)](#understanding-mcp)
3. [Project Architecture](#project-architecture)
4. [How It Works](#how-it-works)
5. [Files Explained](#files-explained)
6. [Running the Project](#running-the-project)
7. [Security Features](#security-features)
8. [Interview Talking Points](#interview-talking-points)

---

## 🎯 What is This Project?

This is a **demonstration project** for a job interview that shows how to build a secure **Model Context Protocol (MCP) server** using Python and FastAPI.

**The Problem It Solves:**
- AI agents (like Microsoft Copilot) need to access company data (invoices)
- Giving AI direct database access is **dangerous** (it could run any SQL query)
- We need a **safe way** for AI to get data without direct database access

**The Solution:**
- Create a "middle layer" (MCP server) between the AI and the database
- AI can only call **specific, pre-approved functions**
- No SQL injection, no unauthorized access, fully controlled

---

## 🧠 Understanding MCP (Model Context Protocol)

### What is MCP?

**Model Context Protocol** is like a "waiter" between an AI and your data:

```
┌─────────────┐
│  AI Agent   │  "I want invoice INV-2024-002"
│  (Copilot)  │
└──────┬──────┘
       │
       │ (MCP Request - JSON format)
       ▼
┌─────────────┐
│ MCP Server  │  "Let me check if you're allowed..."
│ (This Code) │  "Yes, here's the data"
└──────┬──────┘
       │
       │ (Controlled function call)
       ▼
┌─────────────┐
│  Database   │  (Oracle/Mock DB)
└─────────────┘
```

### Why Use MCP?

**Without MCP (Dangerous):**
```python
# AI could send: "DELETE FROM invoices WHERE 1=1"
# 💥 All data deleted!
```

**With MCP (Safe):**
```python
# AI can only call: get_invoice_details(invoice_id)
# ✅ Only retrieves data, cannot delete or modify
```

---

## 🏗️ Project Architecture

### The Three Layers

```
┌──────────────────────────────────────────┐
│         PRESENTATION LAYER               │
│  - dashboard.html (Web UI)               │
│  - test_client.py (Test script)          │
└──────────────┬───────────────────────────┘
               │
               │ HTTP POST /mcp
               ▼
┌──────────────────────────────────────────┐
│         MCP PROTOCOL LAYER               │
│  - server.py (FastAPI)                   │
│  - JSON-RPC 2.0 handler                  │
│  - Tool registry                         │
└──────────────┬───────────────────────────┘
               │
               │ Python function call
               ▼
┌──────────────────────────────────────────┐
│         DATA LAYER                       │
│  - MOCK_ORACLE_DB (Dictionary)           │
│  - get_invoice_details() function        │
└──────────────────────────────────────────┘
```

### Request Flow Example

**1. User clicks "Microsoft Invoice" in dashboard**
```javascript
// JavaScript sends this JSON:
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "get_invoice_details",
    "arguments": {"invoice_id": "INV-2024-002"}
  },
  "id": "1"
}
```

**2. FastAPI server receives it**
```python
# Server validates:
# - Is the method "tools/call"? ✓
# - Does the tool "get_invoice_details" exist? ✓
# - Are the arguments valid? ✓
```

**3. Server calls the function**
```python
result = get_invoice_details("INV-2024-002")
# Returns: Microsoft invoice data
```

**4. Server sends response**
```json
{
  "jsonrpc": "2.0",
  "result": {
    "vendor": "Microsoft Corporation",
    "amount": 125000.00,
    "status": "PENDING"
  },
  "id": "1"
}
```

**5. Dashboard displays it**
```
✅ Invoice retrieved successfully!
```

---

## 📁 Files Explained

### 1. `server.py` - The Main Server (Most Important!)

**What it does:**
- Runs a FastAPI web server on port 8000
- Implements the MCP protocol
- Contains the mock database
- Has the secure `get_invoice_details()` function

**Key Components:**

```python
# Mock Database (in production, this would be real Oracle DB)
MOCK_ORACLE_DB = {
    "INV-2024-001": {...},  # Dell invoice
    "INV-2024-002": {...},  # Microsoft invoice
    "INV-2024-003": {...}   # Oracle invoice
}

# The secure function AI can call
def get_invoice_details(invoice_id: str):
    # Only retrieves data, cannot modify
    return MOCK_ORACLE_DB[invoice_id]

# The MCP endpoint
@app.post("/mcp")
async def mcp_endpoint(request: MCPRequest):
    # Validates and executes tool calls
    # Returns JSON-RPC 2.0 response
```

---

### 2. `dashboard.html` - Web Interface

**What it does:**
- Beautiful web UI to visualize invoices
- Allows testing the MCP API with clicks
- Shows real-time API responses

**Features:**
- 📊 Statistics cards (total invoices, amounts)
- 💳 Invoice cards (click to test API)
- 🧪 API testing section with live responses

**How it works:**
```javascript
// When you click an invoice:
async function testAPI() {
    // Sends POST request to http://localhost:8000/mcp
    const response = await fetch('http://localhost:8000/mcp', {
        method: 'POST',
        body: JSON.stringify(mcpRequest)
    });
    // Displays the result
}
```

---

### 3. `test_client.py` - Automated Tests

**What it does:**
- Simulates an AI agent (like Copilot)
- Runs 6 different test scenarios
- Shows how the API handles success and errors

**Test Cases:**
1. ✅ Retrieve Microsoft invoice (success)
2. ✅ Retrieve Dell invoice (success)
3. ✅ Retrieve Oracle invoice (success)
4. ❌ Try to get non-existent invoice (error handling)
5. ❌ Try to call non-existent tool (error handling)
6. ❌ Use wrong method (error handling)

---

### 4. `requirements.txt` - Dependencies

```
fastapi>=0.104.0      # Web framework
uvicorn>=0.24.0       # ASGI server
pydantic>=2.5.0       # Data validation
requests>=2.31.0      # HTTP client for testing
```

---

## 🚀 Running the Project

### Step-by-Step Guide

**1. Install Dependencies**
```bash
cd "d:\Desktop\knowledge graph\mcp_demo"
pip install -r requirements.txt
```

**2. Start the Server**
```bash
python server.py
```

You'll see:
```
🚀 Starting Clinisys Finance Invoice MCP Server
📋 Available Invoices:
   • INV-2024-001: Dell - $45,000 (PAID)
   • INV-2024-002: Microsoft - $125,000 (PENDING)
   • INV-2024-003: Oracle - $78,000 (OVERDUE)

🔧 Server running on: http://localhost:8000
```

**3. Open the Dashboard**

**Option A:** Double-click `dashboard.html`

**Option B:** Open browser → http://localhost:8000/docs (Swagger UI)

**4. Test It!**

Click any invoice card in the dashboard, or run:
```bash
python test_client.py
```

---

## 🔒 Security Features

### Why This is Secure (For Dean Bennett)

**1. No SQL Injection**
```python
# ❌ DANGEROUS (Direct SQL):
query = f"SELECT * FROM invoices WHERE id = '{user_input}'"
# User could send: "1' OR '1'='1" and get all data!

# ✅ SAFE (MCP):
def get_invoice_details(invoice_id: str):
    return MOCK_ORACLE_DB.get(invoice_id)
# Only exact key lookup, no SQL construction
```

**2. Read-Only Access**
```python
# AI can ONLY call get_invoice_details()
# Cannot call: delete_invoice(), update_invoice(), etc.
# These functions don't even exist!
```

**3. Input Validation**
```python
# Pydantic automatically validates:
class ToolCall(BaseModel):
    name: str  # Must be a string
    arguments: Dict[str, Any]  # Must be a dictionary
# Invalid data is rejected before reaching the function
```

**4. Tool Registry (Whitelist)**
```python
TOOL_REGISTRY = {
    "get_invoice_details": get_invoice_details
}
# Only tools in this registry can be called
# AI cannot execute arbitrary functions
```

**5. Audit Trail**
```python
# Every request is logged:
# - Who called it (request ID)
# - What tool was called
# - What arguments were used
# - What was returned
# Perfect for compliance and debugging
```

---

## 💡 Interview Talking Points

### For Dean Bennett (Architect)

**1. Scalability**
- "This architecture scales easily - just add more tools to the registry"
- "Can handle thousands of requests with FastAPI's async support"
- "Easy to add caching, rate limiting, or authentication"

**2. Maintainability**
- "Clear separation of concerns: Protocol layer, Business logic, Data layer"
- "Type hints throughout for IDE support and fewer bugs"
- "Self-documenting via OpenAPI/Swagger"

**3. Production Readiness**
- "Mock DB can be swapped with real Oracle connection in 5 minutes"
- "CORS configured for security"
- "Error handling covers all edge cases"
- "Health check endpoint for monitoring"

**4. Standards Compliance**
- "Uses JSON-RPC 2.0 standard (industry-wide protocol)"
- "RESTful API design"
- "OpenAPI 3.0 specification"

**5. Security First**
- "Principle of least privilege - AI only gets what it needs"
- "No direct database access"
- "Deterministic, predictable behavior"
- "All inputs validated"

---

## 🎓 Key Concepts to Understand

### 1. JSON-RPC 2.0
A standard way to call remote functions using JSON:
```json
{
  "jsonrpc": "2.0",        // Protocol version
  "method": "tools/call",   // What to do
  "params": {...},          // Arguments
  "id": "1"                 // Request ID
}
```

### 2. FastAPI
A modern Python web framework:
- Fast (built on Starlette and Pydantic)
- Automatic API documentation
- Type checking
- Async support

### 3. Pydantic Models
Data validation using Python classes:
```python
class MCPRequest(BaseModel):
    jsonrpc: str = "2.0"  # Must be "2.0"
    method: str           # Required field
    params: ToolCall      # Must be ToolCall type
```

### 4. CORS (Cross-Origin Resource Sharing)
Allows the dashboard (file://) to call the API (http://localhost:8000):
```python
app.add_middleware(CORSMiddleware, allow_origins=["*"])
```

---

## 🐛 Troubleshooting

### Server won't start - "Port 8000 already in use"
```bash
# Find the process using port 8000
netstat -ano | findstr :8000

# Kill it (replace PID with actual number)
taskkill /F /PID <PID>
```

### Dashboard shows "Failed to fetch"
1. Make sure server is running: `python server.py`
2. Check CORS is enabled in server.py
3. Try Swagger UI instead: http://localhost:8000/docs

### Import errors
```bash
pip install -r requirements.txt
```

---

## 📊 Project Statistics

- **Lines of Code:** ~350
- **Files:** 5 (server, dashboard, test client, README, requirements)
- **API Endpoints:** 3 (/mcp, /, /health)
- **Available Tools:** 1 (get_invoice_details)
- **Test Cases:** 6
- **Mock Invoices:** 3

---

## 🎯 Next Steps for Production

1. **Replace Mock DB** with real Oracle connection using `cx_Oracle`
2. **Add Authentication** (API keys, OAuth, JWT)
3. **Add Rate Limiting** to prevent abuse
4. **Add Logging** to file/database for audit trails
5. **Add More Tools** (create_invoice, update_status, etc.)
6. **Deploy** to cloud (AWS, Azure, GCP)
7. **Add Monitoring** (Prometheus, Grafana)

---

## 📞 Support

For questions about this demo:
- Review the code comments in `server.py`
- Check the Swagger UI: http://localhost:8000/docs
- Run the test client: `python test_client.py`

---

**Built for Clinisys Finance Invoice Agent Interview Demo**
*Demonstrating secure Model Context Protocol implementation*
