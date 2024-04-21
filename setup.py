import os
from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='foxglove-base-msgs',
    version='0.1',
    packages=find_packages(),
    package_data={
    'foxglove-base-msgs': ['msgs/*.proto', 
                           'msgs/*.bin', 
                           'msgs/*.py']
    },
    include_package_data=True,
    install_requires=Path('requirements.txt').read_text().splitlines(),
)