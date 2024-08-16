from setuptools import setup, find_packages
from typing import List
hyphen_E_DOT= '-e .'
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if hyphen_E_DOT in requirements:
            requirements.remove(hyphen_E_DOT)
    return requirements

setup(
    name='MLProject',
    version='0.1',
    author='SakshiSrivas14',
    author_email='srivastavasakshi1413@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)