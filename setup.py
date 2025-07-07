"""setup.py file."""
from setuptools import setup

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

with open("README.md", "r") as fs:
    long_description = fs.read()


__author__ = "Roman Dodin <dodin.roman@gmail.com>"

setup(
    name="srlinux-ndk",
    version="0.5.0",
    packages=["ndk"],
    author="Nokia",
    author_email="roman.dodin@nokia.com",
    description="Nokia SR Linux NetOps Development Kit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    url="https://github.com/nokia/srlinux-ndk-py",
    include_package_data=True,
    install_requires=reqs,
)
