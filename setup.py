from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    this function will return the list of requirements
    """
    requirement_list: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_list
setup(
    name='NetworkSecurityProject',
    version='0.0.1',
    author='Firas Mahjoubi',
    author_email='mahjoubi.firas@esprit.tn',
    packages=find_packages(),
    install_requires=get_requirements(),
)
            
            
            