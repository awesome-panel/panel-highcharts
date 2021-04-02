# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from panel_highcharts import HighChart


def test_constructor():
    config = {"series": [{"data": [1, 2, 3, 4, 5]}]}
    return HighChart(object=config)


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


def test_highchart_app():
    config = {
        "title": {"text": "Panel HighChart Pane"},
        "xAxis": {
            "title": {"enabled": True, "text": "Altitude"},
            "labels": {"formatter": """function(){return this.value + "km";}"""},
        },
        "series": [
            {
                "name": "series1",
                "data": [1, 2, 3, 4, 5],
                "allowPointSelect": "true",
                "point": {
                    "events": {
                        "click": "function(){console.log('click');}",
                        "mouseOver": "@2",
                        "select": "@select",
                        "unselect": "@unselect",
                    }
                },
                "events": {
                    "mouseOut": "@",
                },
            }
        ],
    }
    chart = HighChart(object=config, background="salmon", margin=10)
    return _chart_app(chart)


def test_network_app():
    config = {
        "chart": {
            "type": "networkgraph",
            "plotBorderWidth": 1,
        },
        "title": {"text": "Networkgraph with random initial positions"},
        "plotOptions": {"networkgraph": {"keys": ["from", "to"]}},
        "series": [
            {
                "layoutAlgorithm": {
                    "enableSimulation": True,
                    "initialPositions": """function () {
                    var chart = this.series[0].chart,
                        width = chart.plotWidth,
                        height = chart.plotHeight;

                    this.nodes.forEach(function (node) {
                        // If initial positions were set previously, use that
                        // positions. Otherwise use random position:
                        node.plotX = node.plotX === undefined ?
                            Math.random() * width : node.plotX;
                        node.plotY = node.plotY === undefined ?
                            Math.random() * height : node.plotY;
                    });
                }""",
                },
                "name": "K8",
                "data": [
                    ["A", "B"],
                    ["A", "C"],
                    ["A", "D"],
                    ["A", "E"],
                    ["A", "F"],
                    ["A", "G"],
                    ["B", "C"],
                    ["B", "D"],
                    ["B", "E"],
                    ["B", "F"],
                    ["B", "G"],
                    ["C", "D"],
                    ["C", "E"],
                    ["C", "F"],
                    ["C", "G"],
                    ["D", "E"],
                    ["D", "F"],
                    ["D", "G"],
                    ["E", "F"],
                    ["E", "G"],
                    ["F", "G"],
                ],
            }
        ],
    }
    chart = HighChart(object=config, margin=10)
    return _chart_app(chart)


if __name__.startswith("bokeh"):
    pn.extension("highchart")
    test_highchart_app().servable()
    # test_network_app().servable()
