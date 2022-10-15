![Panel HighCharts Logo](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/images/panel-highcharts-logo.png)

[![PyPI version](https://badge.fury.io/py/panel-highcharts.svg)](https://pypi.org/project/panel-highcharts/)
[![Downloads](https://pepy.tech/badge/panel-highcharts/month)](https://pepy.tech/project/panel-highcharts)
![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIT)
![Test Results](https://github.com/awesome-panel/panel-highcharts/actions/workflows/tests.yaml/badge.svg?branch=main)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/awesome-panel/panel-highcharts/HEAD)
[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcskovmadsen)

# 📈 Panel Highcharts

We want to

- make it super simple to do **exploratory data analysis** and develop high-quality
[Panel](https://awesome-panel.org) **data apps** using the [HighCharts](https://www.highcharts.com/) plotting library.

We provide

- the [`panel-highcharts`](https://pypi.org/project/panel-highcharts/) python package for Panel.
- example notebooks and data apps.

You can install and use the package as simple as.

```bash
pip install panel-highcharts
```

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

![Panel HighCharts Intro](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/videos/panel-highcharts-intro.gif)

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

### 🚀 Install for usage

You can install the package via

```bash
pip install panel-highcharts
```

### 👩‍🏫 Explore the reference examples online

| Guide | Notebook | Jupyter Notebook | Jupyter Labs | Panel App |
| - | - | - | - | - |
| HighChart | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/HighChart) |
| HighStock | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/HighStock) |
| HighMap | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/HighMap) |
| HighGantt | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/HighGantt) |

### 🎨 Explore other examples online

| Guide | Notebook | Jupyter Notebook | Jupyter Labs | App | App
| - | - | - | - |- | - |
| AddSeriesDynamically | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/AddSeriesDynamically.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/AddSeriesDynamically.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/AddSeriesDynamically.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/AddSeriesDynamically) | |
| LinkedCharts | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/LinkedCharts.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/LinkedCharts.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/LinkedCharts.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/LinkedCharts) | |
| Network | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/Network) | [Awesome Panel](https://awesome-panel.org/highcharts-network) |
| PackedBubble | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/PackedBubble) | |
| Themes | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/Themes.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/Themes.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/Themes.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/Themes) | |
| Variwide | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/Variwide.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/Variwide.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/Variwide.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/Variwide) | |

### 👩‍🏫 Explore the examples locally

Run

```bash
pip install pip -U
pip install panel-highcharts[all]
git clone https://github.com/awesome-panel/panel-highcharts.git
cd panel-highcharts/examples
```

Then run

```bash
jupyter lab
```

or

```bash
panel serve *.ipynb
```
