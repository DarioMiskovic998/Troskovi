import io

from setuptools import find_packages
from setuptools import setup

setup(
    name="Praćenje troškova",
    version="1.0.0",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"])