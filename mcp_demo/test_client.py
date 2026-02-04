"""
Test Client for Clinisys Finance Invoice MCP Server
Simulates Microsoft Copilot or other AI agents sending requests
"""

import requests
import json
from typing import Dict, Any


def send_mcp_request(tool_name: str, arguments: Dict[str, Any], request_id: str = "1") -> Dict:
    """
    Sends a JSON-RPC 2.0 compliant MCP request to the server
    
    This simulates how Microsoft Copilot or other AI agents would interact
    with the MCP server to retrieve invoice information.
    
    Args:
        tool_name: Name of the tool to invoke (e.g., "get_invoice_details")
        arguments: Dictionary of arguments to pass to the tool
        request_id: Unique identifier for this request
    
    Returns:
        Dictionary containing the server's response
    """
    
    url = "http://localhost:8000/mcp"
    
    # Construct JSON-RPC 2.0 request payload
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        },
        "id": request_id
    }
    
    print(f"\n{'='*70}")
    print(f"📤 Sending Request (ID: {request_id})")
    print(f"{'='*70}")
    print(json.dumps(payload, indent=2))
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        
        result = response.json()
        
        print(f"\n{'='*70}")
        print(f"📥 Received Response")
        print(f"{'='*70}")
        print(json.dumps(result, indent=2))
        
        return result
    
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Could not connect to server.")
        print("   Make sure the server is running: python server.py")
        return {}
    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ ERROR: {e}")
        return {}


def main():
    """
    Test Suite - Simulates various AI agent queries
    """
    
    print("\n" + "="*70)
    print("🤖 Clinisys Finance Invoice MCP - Test Client")
    print("   Simulating Microsoft Copilot AI Agent Requests")
    print("="*70)
    
    # Test 1: Successful invoice retrieval (Microsoft)
    print("\n\n🧪 TEST 1: Retrieve Microsoft Invoice (PENDING)")
    send_mcp_request(
        tool_name="get_invoice_details",
        arguments={"invoice_id": "INV-2024-002"},
        request_id="test-001"
    )
    
    # Test 2: Successful invoice retrieval (Dell - PAID)
    print("\n\n🧪 TEST 2: Retrieve Dell Invoice (PAID)")
    send_mcp_request(
        tool_name="get_invoice_details",
        arguments={"invoice_id": "INV-2024-001"},
        request_id="test-002"
    )
    
    # Test 3: Successful invoice retrieval (Oracle - OVERDUE)
    print("\n\n🧪 TEST 3: Retrieve Oracle Invoice (OVERDUE - HIGH RISK)")
    send_mcp_request(
        tool_name="get_invoice_details",
        arguments={"invoice_id": "INV-2024-003"},
        request_id="test-003"
    )
    
    # Test 4: Error handling - Invoice not found
    print("\n\n🧪 TEST 4: Error Handling - Non-existent Invoice")
    send_mcp_request(
        tool_name="get_invoice_details",
        arguments={"invoice_id": "INV-9999-999"},
        request_id="test-004"
    )
    
    # Test 5: Error handling - Invalid tool name
    print("\n\n🧪 TEST 5: Error Handling - Invalid Tool Name")
    send_mcp_request(
        tool_name="delete_invoice",  # This tool doesn't exist
        arguments={"invoice_id": "INV-2024-001"},
        request_id="test-005"
    )
    
    # Test 6: Error handling - Invalid method
    print("\n\n🧪 TEST 6: Error Handling - Invalid Method")
    url = "http://localhost:8000/mcp"
    payload = {
        "jsonrpc": "2.0",
        "method": "invalid/method",  # Wrong method
        "params": {
            "name": "get_invoice_details",
            "arguments": {"invoice_id": "INV-2024-001"}
        },
        "id": "test-006"
    }
    
    print(f"\n{'='*70}")
    print(f"📤 Sending Request (ID: test-006)")
    print(f"{'='*70}")
    print(json.dumps(payload, indent=2))
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        result = response.json()
        print(f"\n{'='*70}")
        print(f"📥 Received Response")
        print(f"{'='*70}")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
    
    print("\n\n" + "="*70)
    print("✅ Test Suite Completed")
    print("="*70)
    print("\n💡 Key Takeaways for Interview:")
    print("   • MCP provides secure, controlled access to backend data")
    print("   • AI agents can't execute arbitrary SQL or access unauthorized data")
    print("   • All requests follow JSON-RPC 2.0 standard protocol")
    print("   • Error handling is robust and informative")
    print("   • Architecture is scalable and production-ready")
    print("\n")


if __name__ == "__main__":
    main()
