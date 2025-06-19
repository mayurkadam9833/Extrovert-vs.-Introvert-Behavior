from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    requirements_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as f:  # use "r" mode to read, not "w"
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirements_lst


setup(
    name="your_project_name",  # <-- You should specify a name
    version="0.0.1",
    author="mayur",
    packages=find_packages(),
    install_requires=get_requirements()
)
