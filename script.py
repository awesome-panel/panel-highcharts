import panel_highcharts as ph

ph.config.theme("auto")
ph.config.js_files(highcharts_venn=True)

import panel as pn

pn.extension("highchart", template="fast")

configuration = {
    "series": [
        {
            "type": "venn",
            "name": "The Unattainable Triangle",
            "data": [
                {"sets": ["Good"], "value": 2},
                {"sets": ["Fast"], "value": 2},
                {"sets": ["Cheap"], "value": 2},
                {"sets": ["Good", "Fast"], "value": 1, "name": "More expensive"},
                {"sets": ["Good", "Cheap"], "value": 1, "name": "Will take time to deliver"},
                {"sets": ["Fast", "Cheap"], "value": 1, "name": "Not the best quality"},
                {"sets": ["Fast", "Cheap", "Good"], "value": 1, "name": "They're dreaming"},
            ],
        }
    ],
    "title": {"text": "The Unattainable Triangle"},
}
plot_pane = ph.HighChart(
    object=configuration, sizing_mode="stretch_both", min_height=600
).servable()
