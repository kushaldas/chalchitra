import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chalchitra",
    version="0.2.0",
    author="Kushal Das",
    author_email="mail@kushaldas.in",
    description="Python module to do GUI testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://chalchitra.readthedocs.io/en/latest",
    packages=["chalchitra"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
