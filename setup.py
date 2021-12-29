from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests"]
packages = ["pycoinmc", "pycoinmc/key", "pycoinmc/cryptocurrency", "pycoinmc/exchange"]

setup(
    name="pycoinmc",
    version="6.0.0",
    author="Pablo Valverde",
    author_email="pabludo8cho@gmail.com",
    description="Coinmarketcap unofficial API wrapper, it can be used to easly create python applications that needs to contact with the API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Pablo-Valverde/pycoinmc",
    packages=packages,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9.5",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
