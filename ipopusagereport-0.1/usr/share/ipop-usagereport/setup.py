from setuptools import *

setup(
    name="ipop-stats",
    version="0.0.1",
    install_requires=[
        "flask>=0.10.1,<0.11",
        "pymongo>=3.6,<4",
        "PyYAML>=3.10,<4.0",
    ],
    description="Gathers anonymous usage statistics of IPOP users",
    packages=find_packages(),
    scripts=["bin/ipop-stats"],
)
