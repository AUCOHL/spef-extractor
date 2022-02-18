from setuptools import setup, find_packages
from spef_extractor.__init__ import __version__

requirements = open("requirements.txt").read().strip().split("\n")

setup(
    name="spef_extractor",
    packages=find_packages(),
    version=__version__,
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
