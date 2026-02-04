import json

with open('knowledge_graph.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('notebook_cells.txt', 'w', encoding='utf-8') as out:
    for i, cell in enumerate(nb['cells']):
        out.write(f"\n{'='*60}\n")
        out.write(f"Cell {i} - Type: {cell['cell_type']}\n")
        out.write('='*60 + '\n')
        if 'source' in cell:
            source = ''.join(cell['source'])
            out.write(source + '\n')
