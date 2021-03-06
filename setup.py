import setuptools
from pathlib import Path

setuptools.setup(
    name="HypixelIO",
    version="1.0.0",

    author="Sunrit Jana",
    author_email="warriordefenderz@gmail.com",

    description="A modern async way of interacting with the Hypixel API!",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT",

    url="https://github.com/janaSunrise/",
    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "tools", "tools.*"]
    ),

    install_requires=[
        'aiohttp'
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)