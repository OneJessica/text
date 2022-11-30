from setuptools import setup,find_packages
 
import os


root = os.path.dirname(os.path.realpath("__file__"))
path = os.path.join(root,'REQUIREMENT.txt')
REQUIR = [i.strip() for i in open(path).readlines()]

setup(
    name = 'easy_sql',
    version = '0.0.1',
    # install_requires = REQUIR,
    packages = find_packages(),
    
    
    
)

