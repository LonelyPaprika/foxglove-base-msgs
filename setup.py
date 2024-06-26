import os
from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='foxglove_base_msgs',
    version='1.0.1',
    packages=find_packages(),
    package_data={
    'foxglove_base_msgs': ['msgs/*.proto', 
                           'msgs/*.bin', 
                           'msgs/*.py']
    },
    include_package_data=True,
    install_requires=Path('requirements.txt').read_text().splitlines(),
)