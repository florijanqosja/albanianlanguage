from setuptools import setup, find_packages
import os

# Read version from __version__.py
version_contents = {}
with open(os.path.join("albanianlanguage", "__version__.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="albanianlanguage",
    version=version_contents["__version__"],
    packages=find_packages(include=["albanianlanguage", "albanianlanguage.*"]),
    install_requires=[],
    author="Florijan Qosja",
    author_email="florijanqosja@gmail.com",
    description="A comprehensive package for the Albanian language processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/florijanqosja/albanianlanguage",
    project_urls={
        "Bug Tracker": "https://github.com/florijanqosja/albanianlanguage/issues",
        "Documentation": "https://github.com/florijanqosja/albanianlanguage",
        "Source Code": "https://github.com/florijanqosja/albanianlanguage",
    },
    package_data={"albanianlanguage": ["data/*.csv"]},
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Albanian",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords="albanian, nlp, language-processing, linguistics",
)
