"""Tests the .add_series method of HighChart"""
import panel as pn

import panel_highcharts as ph

pn.extension("highchart", sizing_mode="stretch_width")

CONFIGURATION = {
    "xAxis": {
        "categories": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
    },
    "series": [
        {
            "data": [
                29.9,
                71.5,
                106.4,
                129.2,
                144.0,
                176.0,
                135.6,
                148.5,
                216.4,
                194.1,
                95.6,
                54.4,
            ]
        }
    ],
}

OPTIONS = {
    "data": [
        194.1,
        95.6,
        54.4,
        29.9,
        71.5,
        106.4,
        129.2,
        144.0,
        176.0,
        135.6,
        148.5,
        216.4,
    ]
}


def test_add_series():
    """Tests the .add_series method"""
    chart = ph.HighChart(object=CONFIGURATION, sizing_mode="stretch_both", height=400)
    chart.add_series(options=OPTIONS, redraw=False, animation=False)


def test_get_add_series_app():
    """Tests the .add_series method of HighChart"""
    chart = ph.HighChart(object=CONFIGURATION, sizing_mode="stretch_both", height=800)

    button = pn.widgets.Button(name="Add Series")

    def handle_click(_):
        if button.clicks == 1:

            chart.add_series(options=OPTIONS, redraw=True, animation=True)
            button.disabled = True

    button.on_click(handle_click)

    return pn.template.FastListTemplate(
        site="Panel-HighCharts",
        title="Add Series",
        sidebar=[button],
        main=[chart],
    )


if __name__.startswith("bokeh"):
    test_get_add_series_app().servable()
