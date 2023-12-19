import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="ClassEval",
    py_modules=["ClassEval"],
    version="1.1.0",
    description="",
    author="FDSE",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)