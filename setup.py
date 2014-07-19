from setuptools import setup

setup(
    name='stockmarket',
    description='The Stocks DataBase',
    version='0.1.0',
    packages=['stockmarket', 'stocks', 'companies'],
    install_requires=[
        'django',
    ]
)
