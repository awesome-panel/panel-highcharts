import json

import requests

import panel_highcharts as ph

ph.config.theme("auto")

import panel as pn

pn.extension("highstock")

data = requests.get(
    "https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/new-intraday.json"
).json()
configuration = {
    "title": {"text": "AAPL stock price by minute"},
    "series": [
        {
            "name": "AAPL",
            "type": "candlestick",
            "data": data,
            "tooltip": {"valueDecimals": 2},
            "allowPointSelect": "true",
            "point": {
                "events": {
                    "mouseOver": "@mouseOverFun",
                }
            },
        }
    ],
}
plot_pane = ph.HighStock(object=configuration, sizing_mode="stretch_both", min_height=600)
pn.Column(plot_pane, plot_pane.param.event).servable()
