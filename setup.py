# Setup
from setuptools import setup, find_packages

setup(
    name='Hydra API',
    version='0.2',
    description='Command Line Tool to wrap the hydra server API',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
          'hydra-api = hydra_api.cli:run'
        ]
    }
)
