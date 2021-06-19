# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from datetime import datetime as dt

import panel as pn

import panel_highcharts as ph

# Source: https://jsfiddle.net/bxd210w4/26/
CONFIG = {
    "title": {"text": "Simple Gantt Chart"},
    "series": [
        {
            "name": "Project 1",
            "data": [
                {
                    "id": "s",
                    "name": "Start prototype",
                    "start": "2014/10/18",
                    "end": "2014/10/20",
                },
                {
                    "id": "b",
                    "name": "Develop",
                    "start": "2014/10/20",
                    "end": "2014/10/25",
                    "dependency": "s",
                },
                {
                    "id": "a",
                    "name": "Run acceptance tests",
                    "start": "2014/10/23",
                    "end": "2014/10/26",
                },
                {
                    "name": "Test prototype",
                    "start": "2014/10/27",
                    "end": "2014/10/29",
                    "dependency": ["a", "b"],
                },
            ],
        }
    ],
}

EPOCH = dt.utcfromtimestamp(0)


def convert_to_miliseconds(value):
    s_dt = dt.strptime(value, "%Y/%m/%d")
    return int((s_dt - EPOCH).total_seconds() * 1000)


for point in CONFIG["series"][0]["data"]:  # type: ignore
    point["start"] = convert_to_miliseconds(point["start"])
    point["end"] = convert_to_miliseconds(point["end"])


def test_constructor():
    return ph.HighGantt(object=CONFIG)


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
    # Source: https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/maps/demo/all-areas-as-null # pylint: disable=line-too-long
    chart = ph.HighGantt(object=CONFIG, margin=10)
    return _chart_app(chart)


if __name__.startswith("bokeh"):
    ph.config.js_files()
    pn.extension("highgantt")
    test_highstock_app().servable()
