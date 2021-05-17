![Panel HighCharts Logo](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/images/panel-highcharts-logo.png)

# &#128200; Panel HighCharts

The `panel-highcharts` package makes it easy to use [Highcharts](https://www.highcharts.com/) from Python for exploratory analysis in a Jupyter Notebook or as a [Panel](https://panel.holoviz.org) Web App.

Check out the `panel-highcharts` examples on **Binder**

| Jupyter Notebook | Jupyter Labs | Panel Apps |
| - | - | - |
| [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel) |

[![Panel HighChart Reference Example](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/assets/images/panel-highcharts-binder.gif?raw=true)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighChart.ipynb)

THIS IS APLHA SOFTWARE. I BELIEVE THINGS WORK, BUT THE PACKAGE NEEDS TO BE USED TO TELL. AND USAGE MIGHT ALSO CHANGE THE API.

## License

The `panel-highcharts` python package and repository is open source and free to use (MIT License), however **Highcharts itself requires a license for commercial use**. For more info see the Highcharts license [FAQs](https://shop.highsoft.com/faq).

## Installation

With `pip`

```bash
pip install panel-highcharts
```

## Usage

From with a Jupyter Notebook

```python
import panel_highcharts as ph

import panel as pn
pn.extension('highchart')
```

```python
configuration = {
    "title": {"text": "HighChart Pane"},
    "series": [
        {
            "name": "series1",
            "data": [1, 2, 3, 4, 5],
        }
    ]
}
```

```python
ph.HighChart(object=configuration, sizing_mode="stretch_width")
```

![Basic Example](assets/images/panel-highcharts-basic-example.png)

## Reference Guides

- [HighChart](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighChart.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighChart.ipynb)

- [HighStock](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighStock.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighStock.ipynb)

- [HighMap](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighMap.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighMap.ipynb)

- [HighGantt](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighGantt.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighGantt.ipynb)

## Examples

- [Networkgraph](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/Network.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/Network.ipynb)

- [PackedBubble](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/PackedBubble.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/PackedBubble.ipynb)

## Additional Resources

You can find more inspiration via the links below.

- [Highcharts](https://www.highcharts.com)
  - [Demos](https://www.highcharts.com/demo)
- [Panel](https://panel.holoviz.org)
- [Awesome Panel](https://awesome-panel.org)

## Roadmap

When I get the time I would like to

- Support pandas `.plot` api via method as `.highplot` on dataframes
- Add more examples
- Add badges for 100% test coverage etc.
- Distribute as conda package

## Change Log

- 20210405: Add HighStock, HighMap, HighGantt
- 20210404: Can now display in Classic Notebook
- 20210403: First Release to PyPi. Works in Jupyter Lab and Panel App.
