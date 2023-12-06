from setuptools import find_packages, setup

setup(
    name='imageocrlib',
    packages=find_packages(include=['imageocrlib']),
    version='0.1.0',
    description='Library for image OCR ',
    author='Brillina Wang',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)