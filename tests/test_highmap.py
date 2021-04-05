# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

import panel_highcharts as ph

CONFIG = {
    "chart": {"map": "custom/europe", "borderWidth": 1},
    "title": {"text": "Nordic countries"},
    "subtitle": {"text": "Demo of drawing all areas in the map, only highlighting partial data"},
    "legend": {"enabled": False},
    "series": [
        {
            "name": "Country",
            "data": [["is", 1], ["no", 1], ["se", 1], ["dk", 1], ["fi", 1]],
            "dataLabels": {
                "enabled": True,
                "color": "#FFFFFF",
                "formatter": """function () {
                if (this.point.value) {
                    return this.point.name;
                }
            }""",
            },
            "tooltip": {"headerFormat": "", "pointFormat": "{point.name}"},
        }
    ],
}


def test_constructor():
    return ph.HighMap(object=CONFIG)


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
    chart = ph.HighMap(object=CONFIG, margin=10)
    return _chart_app(chart)


if __name__.startswith("bokeh"):
    ph.config.js_files(mapdata=["custom/europe"])
    pn.extension("highmap")
    test_highstock_app().servable()
