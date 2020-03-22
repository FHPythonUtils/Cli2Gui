"""Do setup for uploading to pypi
"""
import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="cli2gui",
	version="2020.5",
	author="FredHappyface",
	description="Use this module to convert a cli program to a gui",
	long_description=long_description,
    long_description_content_type="text/markdown",
	url="https://github.com/FHPythonUtils/Cli2Gui",
	packages=setuptools.find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
	python_requires='>=3.0',
)
