import sys
sys.path.pop(0)
from setuptools import setup
from codecs import open
from os import path

cwd = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="micropython-sgp40",
    py_modules=["sgp40"],
    version="0.1.0",
    description="MicroPython I2C driver for Sensirion SGP40 VOC sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="sgp40, voc, micropython, i2c",
    url="https://github.com/agners/micropython-sgp40",
    author="Stefan Agner",
    author_email="stefan@agner.ch",
    maintainer="Stefan Agner",
    maintainer_email="stefan@agner.ch",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
