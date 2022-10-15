"""Use

- panel_highcharts.config.js_files to define which Highcharts js files to include
- the HighChart pane to use the Highcharts Chart in Panel.
"""
from . import config
from .charts import HighChart, HighGantt, HighMap, HighStock

VERSION = "20221015.3"
