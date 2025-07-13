import json

with open("MALAIA_Liyab_data.ipynb", "r") as f:
    notebook = json.load(f)

for cell in notebook["cells"]:
    if "source" in cell:
        cell["source"] = [line.replace("\\n", "\n") for line in cell["source"]]

with open("MALAIA_Liyab_data.ipynb", "w") as f:
    json.dump(notebook, f, indent=2)
    f.write("\n")
