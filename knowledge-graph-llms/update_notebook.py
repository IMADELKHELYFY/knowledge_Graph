import json

# Read the notebook
with open('knowledge_graph.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Cell 0: Update pip install command
nb['cells'][0]['source'] = [
    "%pip install --upgrade langchain langchain-experimental langchain-google-genai python-dotenv pyvis\n"
]

# Cell 1: Update API key loading
nb['cells'][1]['source'] = [
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "# Load the .env file\n",
    "load_dotenv()\n",
    "# Get API key from environment variable \n",
    "# (make sure the key is present in .env file in the project directory)\n",
    "api_key = os.getenv(\"GOOGLE_API_KEY\")\n"
]

# Cell 2: Update markdown description
nb['cells'][2]['source'] = [
    "### LLM Graph Transformer\n",
    "Using Google Gemini 1.5 Pro in all examples.\n"
]

# Cell 3: Update imports and model initialization
nb['cells'][3]['source'] = [
    "from langchain_experimental.graph_transformers import LLMGraphTransformer\n",
    "from langchain_core.documents import Document\n",
    "from langchain_google_genai import ChatGoogleGenerativeAI\n",
    "\n",
    "# Initialize Gemini model\n",
    "llm = ChatGoogleGenerativeAI(\n",
    "    model=\"gemini-1.5-pro\",\n",
    "    temperature=0,\n",
    "    google_api_key=api_key\n",
    ")\n",
    "\n",
    "graph_transformer = LLMGraphTransformer(llm=llm)\n"
]

# Save the updated notebook
with open('knowledge_graph.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("Notebook updated successfully!")
print("Updated cells: 0, 1, 2, 3")
