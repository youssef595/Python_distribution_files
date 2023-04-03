from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

from setuptools import setup, find_packages

setup(
    name='save_date',
    version='1.0.0',
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'run_package = save_date.save_folder:function2'
        ]
    }
)
