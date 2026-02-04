# Knowledge Graph Generator

A Streamlit application that extract graph data (entities and relationships) from text input using LangChain and Google's Gemini models, and generates interactive graphs.
![CleanShot 2025-05-28 at 13 11 46](https://github.com/user-attachments/assets/4fef9158-8dd8-432d-bb8a-b53953a82c6c)

👉 This repo is part of my project tutorial on Youtube:
[![](https://img.youtube.com/vi/O-T_6KOXML4/0.jpg)](https://www.youtube.com/watch?v=O-T_6KOXML4)

## Features

- Two input methods: text upload (.txt files) or direct text input
- Interactive knowledge graph visualization
- Customizable graph display with physics-based layout
- Entity relationship extraction powered by Google's Gemini 1.5 Pro model

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Dependencies

The application requires the following Python packages:

- langchain (>= 0.1.0): Core LLM framework
- langchain-experimental (>= 0.0.45): Experimental LangChain features
- langchain-google-genai (>= 0.0.5): Google Gemini integration for LangChain
- python-dotenv (>= 1.0.0): Environment variable support
- pyvis (>= 0.3.2): Graph visualization
- streamlit (>= 1.32.0): Web UI framework

Install all required dependencies using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

### Setup

1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd knowledge_graph_app_2
   ```

   Note: Replace `[repository-url]` with the actual URL of this repository.

2. Create a `.env` file in the root directory with your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```
   
   You can get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Running the Application

To run the Streamlit app:

```bash
streamlit run app.py
```

This will start the application and open it in your default web browser (typically at http://localhost:8501).

## Usage

1. Choose your input method from the sidebar (Upload txt or Input text)
2. If uploading a file, select a .txt file from your computer
3. If using direct input, type or paste your text into the text area
4. Click the "Generate Knowledge Graph" button
5. Wait for the graph to be generated (this may take a few moments depending on the length of the text)
6. Explore the interactive knowledge graph:
   - Drag nodes to rearrange the graph
   - Hover over nodes and edges to see additional information
   - Zoom in/out using the mouse wheel
   - Filter the graph for specific nodes and edges.

## How It Works

The application uses LangChain's experimental graph transformers with Google's Gemini 1.5 Pro model to:
1. Extract entities from the input text
2. Identify relationships between these entities
3. Generate a graph structure representing this information
4. Visualize the graph using PyVis, a Python interface for the vis.js visualization library

## License

This project is licensed under the MIT License - a permissive open source license that allows for free use, modification, and distribution of the software.

For more details, see the [MIT License](https://opensource.org/licenses/MIT) documentation.
