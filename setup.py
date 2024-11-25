import os

from setuptools import setup

VERSION = "0.0.1"


def get_version():
    if "RELEASE_VERSION" in os.environ:
        version = os.environ["RELEASE_VERSION"]
        if not version.startswith(VERSION):
            raise ValueError(
                "Release version does not match version: {} and {}".format(
                    version, VERSION
                )
            )
        return version

    return VERSION


with open("README.md") as fh:
    long_description = fh.read()


setup(
    name="fiftyone-addons",
    version=get_version(),
    description="FiftyOne Addons",
    author="imyhxy",
    author_email="imyhxy@gmail.com",
    url="https://github.com/imyhxy/fiftyone-addons",
    license="Apache",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["fiftyone.addons"],
    include_package_data=True,
    install_requires=["fiftyone"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    scripts=[],
    python_requires=">=3.9",
)
