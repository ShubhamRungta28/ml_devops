from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
name='mldevops',
version='0.0.1',
author='shubhamrungta',
author_email='shubhamrungta28@gmail.com',
packages=find_packages(),
install_requires=get_requirements(r'D:\ML_AndrewNg\ML specialisation\Codes\ML_start_01\ML Projects\ml_DEVOPS\requirements.txt')
)