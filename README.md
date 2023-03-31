# Python_distribution_files
This repository shows examples to convert python projects to python distribution files format like wheel format

1. create a virtual env :
conda create --prefix ./env_wheel python=3.9.12

2. activate it :
conda activate C:\Users\Youssef\Documents\Python_distribution_files\env_wheel

3. build the wheel file :
python setup.py bdist_wheel

4. cd dist folder and launch : 
pip install today_folder-1.0.0-py3-none-any.whl

5. cd.. then cd notebooks and launch the script that launches the main.ipynb :
python process.py 