import os
import subprocess

notebooks = ["Shortest_Path_Visualization.ipynb"]

for notebook in notebooks:
    py_script = notebook.replace(".ipynb", ".py")
    subprocess.run(["jupyter", "nbconvert", "--to", "script", notebook])
    subprocess.run(["python", py_script])
