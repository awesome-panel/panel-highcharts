# For Contributers

## 📙 How to

## Git Clone

```bash
git clone https://github.com/marcskovmadsen/panel-highcharts
cd panel-highcharts
```

### Create an environment with `pip`

**Please note getting node.js might be easier with `conda`. See below for instructions.**

You can create and activate a virtual environment with `pip` by running.

```bash
python -m venv .venv
source .venv/bin/activate # works on linux. Other command is nescessary for windows.
```

You will also need to install [nodejs](https://nodejs.org/en/) and make it available on your `PATH`.

### Create an environment with `conda`

You can create and activate a virtual environment with conda by running.

```bash
conda create --name panel-highcharts python=3.9 nodejs
conda activate panel-highcharts
```

### Install for development

Install the `panel-highcharts` package for editing

```bash
pip install pip -U
pip install -e .[all]
```

This will also install the [`awesome-panel-cli`](https://github.com/awesome-panel/awesome-panel-cli) tool.

You can see the available commands via

```bash
pn --help
```

You can run all tests via

```bash
pn test all
```

Please always run this command and fix any failing tests if possible before you `git push`.

### Update Bokeh JS

Make sure Bokeh is up to date

```bash
cd src/panel_highcharts
npm update @bokeh/bokehjs --save
npm audit fix
cd ../..
```

### Build the Package

Update the version number in the [__init__.py](src/panel_highcharts/__init__.py) and
[package.json](src/panel_highcharts/package.json) files.

Then build the Bokeh models

```bash
panel build src/panel_highcharts
```

Finally you can build the package

```bash
pn build package
```

### 🚢 Release a new package on Pypi

Start by running all tests successfully

```bash
pn test all
```

The [Build the package](#build-the-Package) and run

```bash
pn release package <VERSION>
```

to release the package 📦. To upload to *Test Pypi* first, you can add the `--test` flag.
