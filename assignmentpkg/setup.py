from setuptools import setup, find_packages

setup(
    name="assignmentpkg",
    version="0.1.0",
    author="Kevin, Rahul, S, Ashish",
    description="A package for analyzing data from the NYT API",
    packages=find_packages(),
    install_requires=[
        "requests",
        "PyYAML",
        "numpy",
        "scipy",
        "matplotlib"
    ],
    python_requires='>=3.6',
)
