import json

# Read the notebook
with open('knowledge_graph.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Cell 3: Update model initialization - remove explicit API key parameter
nb['cells'][3]['source'] = [
    "from langchain_experimental.graph_transformers import LLMGraphTransformer\n",
    "from langchain_core.documents import Document\n",
    "from langchain_google_genai import ChatGoogleGenerativeAI\n",
    "\n",
    "# Initialize Gemini model\n",
    "llm = ChatGoogleGenerativeAI(\n",
    "    model=\"gemini-1.5-pro\",\n",
    "    temperature=0\n",
    ")\n",
    "\n",
    "graph_transformer = LLMGraphTransformer(llm=llm)\n"
]

# Save the updated notebook
with open('knowledge_graph.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("Notebook updated - removed explicit google_api_key parameter")
