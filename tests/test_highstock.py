# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import json
import pathlib

import panel as pn

from panel_highcharts import HighStock

FILE = pathlib.Path(__file__).parent
# Source: https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/new-intraday.json
DATA = FILE.parent / "assets" / "data" / "new-intraday.json"


def test_constructor():
    config = {"series": [{"data": [1, 2, 3, 4, 5]}]}
    return HighStock(object=config)


def _chart_app(chart):
    return pn.Row(
        pn.WidgetBox(
            pn.Param(
                chart,
                parameters=[
                    "height",
                    "width",
                    "sizing_mode",
                    "margin",
                    "object",
                    "object_update",
                    "event",
                ],
                widgets={
                    "object": pn.widgets.LiteralInput,
                    "object_update": pn.widgets.LiteralInput,
                    "event": pn.widgets.StaticText,
                },
            ),
            sizing_mode="fixed",
        ),
        chart,
        sizing_mode="stretch_both",
    )


def test_highstock_app():
    data = json.loads(DATA.read_text())
    config = {
        "title": {"text": "AAPL stock price by minute"},
        "rangeSelector": {
            "buttons": [
                {"type": "hour", "count": 1, "text": "1h"},
                {"type": "day", "count": 1, "text": "1D"},
                {"type": "all", "count": 1, "text": "All"},
            ],
            "selected": 1,
            "inputEnabled": False,
        },
        "series": [
            {"name": "AAPL", "type": "candlestick", "data": data, "tooltip": {"valueDecimals": 2}}
        ],
    }
    chart = HighStock(object=config, margin=10)
    return _chart_app(chart)


if __name__.startswith("bokeh"):
    pn.extension("highstock")
    test_highstock_app().servable()
