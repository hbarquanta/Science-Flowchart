import json
import os

def load_tree(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def mermaid_from_tree(tree, root_label="Science"):
    lines = ["flowchart TD", f'ROOT["{root_label}"]']
    
    def recurse(subtree, parent_id):
        for name, children in subtree.items():
            safe_id = name.upper().replace(" ", "_").replace("-", "_")
            lines.append(f'{parent_id} --> {safe_id}["{name}"]')
            if isinstance(children, dict) and children:
                recurse(children, safe_id)
    
    recurse(tree, "ROOT")
    return "\n".join(lines)

def main():
    tree = load_tree('data/disciplines.json')
    mmd = mermaid_from_tree(tree)
    os.makedirs('diagrams', exist_ok=True)
    with open('diagrams/core-sciences.mmd', 'w', encoding='utf-8') as f:
        f.write(mmd)
    print("Generated diagrams/core-sciences.mmd")

if __name__ == "__main__":
    main()
