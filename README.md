# Python_distribution_files
This repository shows examples to convert python projects to python distribution files format like wheel format

1. create a virtual env :
conda create --prefix ./env_wheel python=3.9.12

2. activate it :
conda activate C:\Users\Youssef\Documents\Python_distribution_files\env_wheel

3. install setup tools and wheel packages
pip install -U setuptools wheel

4. build the wheel file :
python setup.py bdist_wheel

5. cd dist folder and launch : 
pip install today_folder-1.0.0-py3-none-any.whl

6. laucnh project with :
* Run_project (this will run the script specified in entry points of setup.py)
* Or Call your modules like this :
from save_date.save_folder import function2