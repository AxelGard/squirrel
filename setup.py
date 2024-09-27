from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="squirrel",
    version="0.1.0",
    description="",
    url="https://github.com/AxelGard/squirrel",
    author="Axel Gard",
    author_email="axel.gard@tutanota.com",
    license="MIT",
    packages=["squirrel"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
    ],
    extras_requires={"dev": ["pytest", "black"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Office/Business :: Financial",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
