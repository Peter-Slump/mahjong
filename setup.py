import os

from setuptools import setup, find_packages

VERSION = '0.1.0'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mahjong',
    version=VERSION,
    long_description=README,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    extras_require={
        'dev': [
            'bumpversion',
            'flake8'
        ],
    },
    setup_requires=[
        'pytest-runner',
        'bumpversion',
    ],
    install_requires=[],
    tests_require=[
        'pytest',
        'factory_boy',
        'mock',
    ],
    url='https://github.com/Peter-Slump/mahjong',
    license='MIT',
    author='Peter Slump',
    author_email='peter@yarf.nl',
    description='A Mahjong game library'
)
