from setuptools import setup, find_packages


packages = find_packages()
description = 'cli tool to perform logistic regression on a dataset'
author = 'Serhii Ladonia'
author_email = 'ladonya.s@gmail.com'
url = 'https://github.com/MedievalSerj/logistic_regression'


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='dslr',
    version='0.1',
    description=description,
    long_description=description,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    install_requires=requirements,
    url=url,
    license='GPL',
    packages=packages,
    entry_points={
        'console_scripts': ['dslr=dslr.main:main'],
    }
)
