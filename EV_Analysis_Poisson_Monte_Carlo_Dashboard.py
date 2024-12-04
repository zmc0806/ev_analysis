import os
import subprocess

notebooks = ["EV_Analysis_Poisson_Monte_Carlo_Dashboard.ipynb"]

for notebook in notebooks:
    py_script = notebook.replace(".ipynb", ".py")
    subprocess.run(["jupyter", "nbconvert", "--to", "script", notebook])
    subprocess.run(["python", py_script])
