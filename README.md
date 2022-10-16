![Panel HighCharts Logo](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/images/panel-highcharts-logo.png)

# 📈 Panel Highcharts

We want to

- make it super simple to do **exploratory data analysis** and develop high-quality
[Panel](https://awesome-panel.org) **data apps** using the [HighCharts](https://www.highcharts.com/) plotting library.

We provide

- the [`panel-highcharts`](https://pypi.org/project/panel-highcharts/) python package for Panel.
- example notebooks and data apps.

You can install and use the package as simple as.

![Panel HighCharts Intro](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/videos/panel-highcharts-intro.gif)

## Monitor

[![PyPI version](https://badge.fury.io/py/panel-highcharts.svg)](https://pypi.org/project/panel-highcharts/)
[![Downloads](https://pepy.tech/badge/panel-highcharts/month)](https://pepy.tech/project/panel-highcharts)
![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIT)
![Test Results](https://github.com/awesome-panel/panel-highcharts/actions/workflows/tests.yaml/badge.svg?branch=main)

[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)
[![Follow on LinkedIn](https://img.shields.io/badge/linked-in-blue)](https://www.linkedin.com/in/marcskovmadsen)

## ⭐ Support

Please support [Panel](https://panel.holoviz.org) and
[awesome-panel](https://awesome-panel.org) by giving the projects a star on Github:

- [holoviz/panel](https://github.com/holoviz/panel).
- [awesome-panel/awesome-panel](https://github.com/awesome-panel/awesome-panel).

Thanks

## ❤️ Contribute

If you are looking to contribute to this project you can find ideas in the [issue tracker](https://github.com/awesome-panel/panel-highcharts/issues). To get started check out the [DEVELOPER_GUIDE](DEVELOPER_GUIDE.md).

I would love to support and receive your contributions. Thanks.

[![Hacktober Fest](https://github.blog/wp-content/uploads/2022/10/hacktoberfestbanner.jpeg?fit=1200%2C630)](https://github.com/awesome-panel/awesome-panel-cli/issues).

## ⚖️ License

The `panel-highcharts` python package and repository is open source and free to use (MIT License), however **Highcharts itself requires a license for commercial use**. For more info see the Highcharts license [FAQs](https://shop.highsoft.com/faq).

## 📙 How to

Below we describe how to get started.

### 🚀 Get started in under a minute

Install `panel-highcharts` including the *`examples` dependencies*.

```bash
pip install panel-highcharts[examples]
```

Download the examples

```bash
pn examples panel-highcharts
```

Explore the sample notebooks in the folder `examples/awesome-panel/panel-highcharts`

```bash
jupyter lab
```

![Panel HighCharts Intro](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/videos/pn-examples-panel-highcharts.gif)

Explore the sample apps

```bash
pn hello panel-highcharts
```

![Panel HighCharts Intro](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/videos/pn-hello-panel-highcharts.gif)

### 📒 Get started on Binder

Click the button

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/awesome-panel/panel-highcharts/HEAD)

### Create a hello world example

```python
import panel_highcharts as ph

import panel as pn
pn.extension('highchart')

configuration = {
    "title": {"text": "HighChart Pane"},
    "series": [
        {
            "name": "series1",
            "data": [1, 2, 3, 4, 5],
        }
    ]
}

ph.HighChart(object=configuration, sizing_mode="stretch_width").servable()
```

### Checkout Highcharts examples

Follow the [link](https://www.highcharts.com/demo)

![Highcharts Gallery](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/images/highcharts-gallery.gif)
