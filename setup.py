from setuptools import find_packages,setup
from typing import List

"""
def get_requirement(file_path:str)=>List[str]:
    with open(file_path,'read') as file:
        requirements=  file.read().splitlines()
    return requirements

"""

HYPHEN_E_DOT="-e ."
def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as obj:
        requirements=obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
name= "ML end to end",
version="0.0.1",
author= "harshita",
author_email="starlastyle@gmail.com",
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn'] what if we want 1000 package
install_requires=get_requirement("requirement.txt")
)