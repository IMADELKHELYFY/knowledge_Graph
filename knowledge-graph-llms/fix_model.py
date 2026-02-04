import json

# Read the notebook
with open('knowledge_graph.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Cell 2: Update markdown description
nb['cells'][2]['source'] = [
    "### LLM Graph Transformer\n",
    "Using Google Gemini Pro in all examples.\n"
]

# Cell 3: Update model to gemini-pro
nb['cells'][3]['source'] = [
    "from langchain_experimental.graph_transformers import LLMGraphTransformer\n",
    "from langchain_core.documents import Document\n",
    "from langchain_google_genai import ChatGoogleGenerativeAI\n",
    "\n",
    "# Initialize Gemini model\n",
    "llm = ChatGoogleGenerativeAI(\n",
    "    model=\"gemini-pro\",\n",
    "    temperature=0\n",
    ")\n",
    "\n",
    "graph_transformer = LLMGraphTransformer(llm=llm)\n"
]

# Save the updated notebook
with open('knowledge_graph.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("Notebook updated to use gemini-pro model")
