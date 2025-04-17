from setuptools import setup, find_packages

setup(
    name="e164-python-sk",
    version="0.1.0",
    description="A Python SDK package for accessing the  e164.com phone number validation API.",
    author="Catalin Dragos",
    author_email="catalin.dragos@e164.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
