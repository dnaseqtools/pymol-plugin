from setuptools import setup, find_packages

def parse_requirements(file):
    with open(file) as f:
        return [line.strip() for line in f if line and not line.startswith("#")]

setup(
    name="DNASeq Kinase Analyzer",
    version="1.0",
    author="Alexander Melton",
    description="A PyMOL-compatible module for analyzing the human kinome using DNASeq's proprietary tools and algorithms",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
)
