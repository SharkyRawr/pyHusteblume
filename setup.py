import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="husteblume",
    version="0.0.1",
    author="Sophie Luna Schumann",
    author_email="pypi@sophie.lgbt",
    description="Library to access the TK.de Husteblume API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SharkyRawr/pyHusteblume",
    project_urls={
        "Bug Tracker": "https://github.com/SharkyRawr/pyHusteblume/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="husteblume"),
    python_requires=">=3.6",
    install_requires=[
          'requests',
      ],
)