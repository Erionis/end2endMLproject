from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str)-> List[str]:
    '''
    Read requirements.txt file and return list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        requirements = [line.replace("\n","") for line in lines if not line.startswith('-e')]
    return requirements
        
        

setup(
    name='mlproject',
    version='0.0.1',
    author='Erionis',
    author_email='erion.islamay@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)