from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the requirements
    '''

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]  #Betweenn the packages will apear automaticli \n
         
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# We specify parameters here metadadata infos of project
setup(
name='mlproject',
version='0.0.1',
author='Riyad',
author_email='riyadouldabdallah@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')



)