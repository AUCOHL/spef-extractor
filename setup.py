import os
import sys
import subprocess
from setuptools import setup, find_packages

try:
    version = (
        subprocess.check_output(["git", "describe", "--tags"]).decode("utf8").strip()
    )
except subprocess.CalledProcessError:
    print("spef-extractor must be built with a full Git clone.", file=sys.stderr)
    exit(os.EX_DATAERR)

requirements = open("requirements.txt").read().strip().split("\n")

setup(
    name="spef-extractor",
    packages=find_packages(),
    version=version,
    description="A parasitics estimator based on layout and technology files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mohamed Gaber",
    author_email="mohamed.gaber@aucegypt.edu",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["spef_extractor = spef_extractor.__main__:main"]},
    python_requires=">3.6",
)
