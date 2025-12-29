from setuptools import find_packages,setup
#from typeing import List

def get_requirements_list()-> list(str):
    requirements_list=list(str)=[]
    return requirements_list



setup(
    name="sensor",
    author="Subodh Kumar yadav",
    version="0.0.1",
    author_email="subodhkumary933@gmail.com",
    packages=find_packages(),
    install_requries=get_requirements_list()
)