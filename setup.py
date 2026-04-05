from setuptools import find_packages,setup
from typing import List

HYPEN_E_OUT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This funcation will retrun th list of the requirements. 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_E_OUT in requirements:
            requirements.remove(HYPEN_E_OUT)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Shrikant',
author_email='ncoolboy21@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)