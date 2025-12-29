from setuptools import find_packages,setup
from typing import List

def get_requirements_list()->List[str]:
# this function will return list of requirements

    requirements_list:List[str]=[]
    """ 
    write a code to read requirements.txt file and append each requirements
    in requirement_list variable
    """

    return requirements_list



setup(
    name="sensor",
    author="Subodh Kumar yadav",
    version="0.0.1",
    author_email="subodhkumary933@gmail.com",
    packages=find_packages(),
    install_requries=get_requirements_list()
)