"""Setup file for the Awesome Panel Extensions"""
import pathlib
from typing import List

import setuptools

# I only want to include a short README with a focus on the package
with open("README.md", "r") as fh:
    long_description = fh.read()

ROOT = pathlib.Path.cwd()
VERSION = (ROOT / "VERSION").read_text().strip()

install_requires = [
    "panel>=0.11.1",
    "bokeh==2.3",
]

_recommended: List[str] = []

_tests = [
    "autoflake",
    "invoke",
    "isort",
    "jupyter-repo2docker",
    "mypy",
    "pylint>=2.6.0",
    "pytest",
    "pytest-cov",
    "rope",
    "twine",
    "wheel",
]

_examples = [
    "notebook",
    "jupyterlab",
]

_doc: List[str] = []

extras_require = {
    "examples": _recommended + _examples,
    "tests": _tests,
    "recommended": _recommended,
    "doc": _recommended + _doc,
}

extras_require["all"] = sorted(set(sum(extras_require.values(), [])))

setuptools.setup(
    name="panel-highcharts",
    version=VERSION,
    description="""A python package enabling you to use HighCharts with Jupyter, HoloViz Panel and
    the rest of the tools you know and love""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marc Skov Madsen",
    author_email="marc.skov.madsen@gmail.com",
    platforms=["Windows", "Mac OS X", "Linux"],
    license="MIT",
    url="https://github.com/MarcSkovMadsen/panel-highcharts",
    # My Project contains more folders/ packages but they should not be included
    packages=setuptools.find_packages(include=["panel_highcharts", "panel_highcharts.*"]),
    include_package_data=True,
    classifiers=[
        # I would like to indicate that this package is a package for the Panel framework
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=extras_require["tests"],
)
