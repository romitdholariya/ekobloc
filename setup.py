from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mehta/__init__.py
from mehta import __version__ as version

setup(
	name="mehta",
	version=version,
	description="Mehta Group Customisation(EXPAI & CADCAM)",
	author="Prashant Kamble",
	author_email="kambleprashant@outlook.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
