import os
import subprocess

notebooks = ["VFT_Analysis_Visualization_2018_2023.ipynb"]

for notebook in notebooks:
    py_script = notebook.replace(".ipynb", ".py")
    subprocess.run(["jupyter", "nbconvert", "--to", "script", notebook])
    subprocess.run(["python", py_script])
