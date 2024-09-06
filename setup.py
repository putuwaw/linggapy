from setuptools import setup, find_packages

setup(
    name="linggapy",
    url="https://github.com/putuwaw/linggapy",
    author="Putu Widyantara Artanta Wibawa",
    author_email="putuwaw973@gmail.com",
    packages=find_packages(),
    package_data={
        "linggapy": ["data/*.txt"],
    },
    version="0.1.1",
    license="MIT",
    keywords=["stemming", "stem", "balinese", "language"],
    description="Library for Stemming Balinese Text Language",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6, <4",
)
