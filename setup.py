from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="higgs-audio",
    version="0.1.0",
    description="Text-audio foundation model from Boson AI",
    author="Boson AI",
    author_email="your@email.com",
    url="https://github.com/rsxdalv/higgs-audio",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)