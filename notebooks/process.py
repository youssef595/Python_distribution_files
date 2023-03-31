import subprocess
import os

def main():
    # Define the path to your Jupyter notebook
    notebook_path = os.path.abspath("save_folder.ipynb")
    subprocess.run(["jupyter", "notebook", notebook_path])