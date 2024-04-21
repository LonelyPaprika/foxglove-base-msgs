import os
from setuptools import setup, find_packages

setup(
    name='foxglove-base-msgs',
    version='0.1',
    packages=find_packages(),
    package_data={
    'foxglove_base_msgs': ['msgs/*.proto', 
                           'msgs/*.bin', 
                           'msgs/*.py']
    },
    install_requires=[
        'protobuf'
    ]
)