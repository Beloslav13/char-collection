import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="char-collection",
    version="1.2.0",
    author="Beloslav",
    author_email="velislav1329@gmail.com",
    description="Building random characters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Beloslav13/char-collection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)