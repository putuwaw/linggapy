from setuptools import setup, find_packages
import os
import re


def get_version() -> str:
    version_file = os.path.join("linggapy", "__init__.py")
    with open(version_file) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")


setup(
    name="linggapy",
    version=get_version(),
    description="Library for Stemming Balinese Text Language",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Putu Widyantara Artanta Wibawa",
    author_email="putuwaw973@gmail.com",
    url="https://github.com/putuwaw/linggapy",
    packages=find_packages(),
    license="MIT",
    keywords=["stemming", "stem", "balinese", "language"],
    package_data={
        "linggapy": ["data/*.txt"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10, <4",
    extras_require={
        "dev": [
            "pytest>=8.3.2, <9",
        ],
        "docs": [
            "sphinx>=8.0.2, <9",
            "furo",
        ],
    },
    project_urls={
        "Documentation": "https://linggapy.readthedocs.io/en/latest",
        "Source": "https://github.com/putuwaw/linggapy",
        "Issue": "https://github.com/putuwaw/linggapy/issues",
    },
)
