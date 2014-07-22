from setuptools import setup

setup(
    name='icdb',
    description='The Internet Car DataBase',
    version='0.0.1',
    packages=['icdb', 'cars'],
    install_requires=[
        'django',
        'nose',
        'mock',
    ]
)
