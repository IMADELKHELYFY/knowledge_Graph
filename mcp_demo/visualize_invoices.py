"""
Invoice Knowledge Graph Visualizer
Generates an interactive network graph showing relationships between:
- Invoices
- Vendors
- Payment Status
- Risk Levels
- Due Dates
"""

from pyvis.network import Network
import os

# Mock Oracle Database (same as in server.py)
MOCK_ORACLE_DB = {
    "INV-2024-001": {
        "vendor": "Dell Technologies",
        "status": "PAID",
        "amount": 45000.00,
        "due_date": "2024-01-15",
        "risk_level": "LOW",
        "payment_date": "2024-01-10"
    },
    "INV-2024-002": {
        "vendor": "Microsoft Corporation",
        "status": "PENDING",
        "amount": 125000.00,
        "due_date": "2024-02-28",
        "risk_level": "MEDIUM",
        "payment_date": None
    },
    "INV-2024-003": {
        "vendor": "Oracle Corporation",
        "status": "OVERDUE",
        "amount": 78000.00,
        "due_date": "2024-01-20",
        "risk_level": "HIGH",
        "payment_date": None
    },
    "INV-2024-004": {  # Changed from duplicate INV-2024-001 to INV-2024-004
        "vendor": "IBM Corporation",
        "status": "PAID",
        "amount": 45000.00,
        "due_date": "2024-01-18",
        "risk_level": "LOW",
        "payment_date": "2024-01-18"
    }
}


def create_invoice_knowledge_graph():
    """
    Creates an interactive knowledge graph of the invoice database
    """
    
    # Create network with dark theme
    net = Network(
        height="900px",
        width="100%",
        directed=True,
        notebook=False,
        bgcolor="#1a1a2e",
        font_color="white",
        filter_menu=True,
        cdn_resources='remote'
    )
    
    # Color scheme
    colors = {
        "invoice": "#667eea",      # Purple for invoices
        "vendor": "#48bb78",       # Green for vendors
        "status_paid": "#38b2ac",  # Teal for paid
        "status_pending": "#ed8936", # Orange for pending
        "status_overdue": "#f56565", # Red for overdue
        "risk_low": "#68d391",     # Light green
        "risk_medium": "#f6ad55",  # Light orange
        "risk_high": "#fc8181"     # Light red
    }
    
    # Track unique nodes to avoid duplicates
    vendors_added = set()
    statuses_added = set()
    risks_added = set()
    
    # Add invoice nodes and their relationships
    for invoice_id, data in MOCK_ORACLE_DB.items():
        vendor = data["vendor"]
        status = data["status"]
        risk = data["risk_level"]
        amount = data["amount"]
        due_date = data["due_date"]
        
        # Add invoice node (center of the graph)
        invoice_label = f"{invoice_id}\n${amount:,.0f}"
        net.add_node(
            invoice_id,
            label=invoice_label,
            title=f"Invoice: {invoice_id}<br>Amount: ${amount:,.2f}<br>Due: {due_date}",
            color=colors["invoice"],
            size=30,
            shape="box",
            font={"size": 14, "color": "white"}
        )
        
        # Add vendor node (if not already added)
        if vendor not in vendors_added:
            net.add_node(
                vendor,
                label=vendor,
                title=f"Vendor: {vendor}",
                color=colors["vendor"],
                size=25,
                shape="ellipse",
                font={"size": 12, "color": "white"}
            )
            vendors_added.add(vendor)
        
        # Add relationship: Invoice -> Vendor
        net.add_edge(
            invoice_id,
            vendor,
            label="VENDOR",
            color="#48bb78",
            arrows="to",
            width=2
        )
        
        # Add status node (if not already added)
        status_node = f"STATUS_{status}"
        if status_node not in statuses_added:
            status_color = colors.get(f"status_{status.lower()}", "#999")
            net.add_node(
                status_node,
                label=status,
                title=f"Payment Status: {status}",
                color=status_color,
                size=20,
                shape="diamond",
                font={"size": 12, "color": "white"}
            )
            statuses_added.add(status_node)
        
        # Add relationship: Invoice -> Status
        net.add_edge(
            invoice_id,
            status_node,
            label="STATUS",
            color=colors.get(f"status_{status.lower()}", "#999"),
            arrows="to",
            width=2
        )
        
        # Add risk level node (if not already added)
        risk_node = f"RISK_{risk}"
        if risk_node not in risks_added:
            risk_color = colors.get(f"risk_{risk.lower()}", "#999")
            net.add_node(
                risk_node,
                label=f"{risk} RISK",
                title=f"Risk Level: {risk}",
                color=risk_color,
                size=20,
                shape="triangle",
                font={"size": 12, "color": "white"}
            )
            risks_added.add(risk_node)
        
        # Add relationship: Invoice -> Risk
        net.add_edge(
            invoice_id,
            risk_node,
            label="RISK",
            color=colors.get(f"risk_{risk.lower()}", "#999"),
            arrows="to",
            width=2
        )
        
        # Add due date node
        due_date_node = f"DUE_{due_date}"
        net.add_node(
            due_date_node,
            label=due_date,
            title=f"Due Date: {due_date}",
            color="#9f7aea",
            size=15,
            shape="dot",
            font={"size": 10, "color": "white"}
        )
        
        # Add relationship: Invoice -> Due Date
        net.add_edge(
            invoice_id,
            due_date_node,
            label="DUE",
            color="#9f7aea",
            arrows="to",
            width=1
        )
    
    # Configure physics for better layout
    net.set_options("""
        {
            "physics": {
                "forceAtlas2Based": {
                    "gravitationalConstant": -80,
                    "centralGravity": 0.015,
                    "springLength": 200,
                    "springConstant": 0.08,
                    "damping": 0.4,
                    "avoidOverlap": 0.5
                },
                "minVelocity": 0.75,
                "solver": "forceAtlas2Based",
                "stabilization": {
                    "enabled": true,
                    "iterations": 100
                }
            },
            "interaction": {
                "hover": true,
                "tooltipDelay": 100,
                "navigationButtons": true,
                "keyboard": true
            }
        }
    """)
    
    # Save the graph
    output_file = "invoice_knowledge_graph.html"
    net.save_graph(output_file)
    
    print("=" * 70)
    print("🎨 Invoice Knowledge Graph Generated!")
    print("=" * 70)
    print(f"\n📊 Graph Statistics:")
    print(f"   • Total Invoices: {len(MOCK_ORACLE_DB)}")
    print(f"   • Unique Vendors: {len(vendors_added)}")
    print(f"   • Payment Statuses: {len(statuses_added)}")
    print(f"   • Risk Levels: {len(risks_added)}")
    print(f"\n💾 Saved to: {os.path.abspath(output_file)}")
    print(f"\n🌐 Open this file in your browser to view the interactive graph!")
    print("=" * 70)
    
    # Try to open in browser
    try:
        import webbrowser
        webbrowser.open(f"file://{os.path.abspath(output_file)}")
        print("\n✅ Opening in browser...")
    except:
        print("\n💡 Manually open the file to view the graph")
    
    return net


if __name__ == "__main__":
    print("\n🚀 Generating Invoice Knowledge Graph...\n")
    create_invoice_knowledge_graph()
