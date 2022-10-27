from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

print(required)

setup(
    name='backend',
    description='Backend for the Data Solutions',
    packages=find_packages(),
    install_requires=required
)