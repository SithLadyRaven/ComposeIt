from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ComposeIt',
    version='1.0.0',
    author='Kelsey Price',
    author_email='kelsey@raven.ws',
    description='Generate docker-compose file from existing containers',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sithladyraven/ComposeIt',
    packages=['ComposeIt'],
    install_requires=['docker>=3.3.0', 'pyyaml>=3.12'],
    entry_points={
        'console_scripts': ['ComposeIt = ComposeIt:main']
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
