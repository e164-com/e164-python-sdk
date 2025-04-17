import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="e164_python",
    version="1.0",
    author="Catalin Dragos",
    author_email="catalin.dragos@e164.com",
    description="E164 Python SDK is a python package for interacting with the e164.com API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/e164-com/e164-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
