"""Use

- panel_highcharts.config.js_files to define which Highcharts js files to include
"""
from typing import List, Optional

from panel import extension
from panel.io import notebook

# Enables using pn.extension("highchart", ...)
# pylint: disable=protected-access
extension._imports["highchart"] = "panel_highcharts.models.highchart"
extension._imports["highstock"] = "panel_highcharts.models.highstock"
extension._imports["highmap"] = "panel_highcharts.models.highmap"
extension._imports["highgantt"] = "panel_highcharts.models.highgantt"
# pylint: enable=protected-access


# pylint: disable=too-many-arguments, invalid-name
def _mock():
    """Temporary fix #2571 https://github.com/holoviz/panel/issues/2571"""

    def _autoload_js(
        bundle, configs, requirements, exports, skip_imports, ipywidget, load_timeout=5000
    ):
        config = {"packages": {}, "paths": {}, "shim": {}}
        for conf in configs:
            for key, c in conf.items():
                config[key].update(c)
        return notebook.AUTOLOAD_NB_JS.render(
            bundle=bundle,
            force=True,
            timeout=load_timeout,
            config=config,
            requirements=requirements,
            exports=exports,
            skip_imports=skip_imports,
            ipywidget=ipywidget,
        )

    notebook._autoload_js = _autoload_js  # pylint: disable=protected-access


# pylint: enable=too-many-arguments, invalid-name

_mock()


def js_files(  # pylint: disable=too-many-locals, too-many-arguments
    highcharts_accessibility: bool = False,
    highcharts_annotations: bool = False,
    highcharts_boost: bool = False,
    highcharts_broken_axis: bool = False,
    highcharts_canvas_tools: bool = False,
    highcharts_coloraxis: bool = False,
    highcharts_data: bool = False,
    highcharts_drilldown: bool = False,
    highcharts_export_data: bool = True,
    highcharts_exporting: bool = True,
    highcharts_funnel: bool = False,
    highcharts_heatmap: bool = False,
    highcharts_marker_clusters: bool = False,
    highcharts_more: bool = False,
    highcharts_networkgraph: bool = False,
    highcharts_no_data: bool = False,
    highcharts_offline_exporting: bool = False,
    highcharts_solid_gauge: bool = False,
    highcharts_3d: bool = False,
    highcharts_treemap: bool = False,
    highcharts_variwide: bool = False,
    mapdata: Optional[List[str]] = None,
):
    """Configures the js files to include from https://code.highcharts.com

    Use this before using `panel.extension("highchart")`

    Args:
        highcharts_accessibility (bool, optional): Defaults to False.
        highcharts_annotations (bool, optional): Defaults to False.
        highcharts_boost (bool, optional): Defaults to False.
        highcharts_broken_axis (bool, optional): Defaults to False.
        highcharts_coloraxis (bool, optional): Defaults to False.
        highcharts_canvas_tools (bool, optional): Defaults to False.
        highcharts_data (bool, optional): Defaults to False.
        highcharts_drilldown (bool, optional): Defaults to False.
        highcharts_export_data (bool, optional): Defaults to True.
        highcharts_exporting (bool, optional): Defaults to True.
        highcharts_funnel (bool, optional): Defaults to False.
        highcharts_heatmap (bool, optional): Defaults to False.
        highcharts_marker_clusters (bool, optional): Defaults to False.
        highcharts_more (bool, optional): Defaults to False.
        highcharts_networkgraph (bool, optional): Defaults to False.
        highcharts_no_data (bool, optional): Defaults to False.
        highcharts_offline_exporting (bool, optional): Defaults to False.
        highcharts_solid_gauge (bool, optional): Defaults to False.
        highcharts_3d (bool, optional): Defaults to False.
        highcharts_treemap (bool, optional): Defaults to False.
        highcharts_variwide (bool, optional): Defaults to False.
    """
    # pylint: disable=import-outside-toplevel
    from .models.highchart import HighChart
    from .models.highgantt import HighGantt
    from .models.highmap import HighMap
    from .models.highstock import HighStock

    HighChart.js_files(
        highcharts_accessibility=highcharts_accessibility,
        highcharts_annotations=highcharts_annotations,
        highcharts_boost=highcharts_boost,
        highcharts_broken_axis=highcharts_broken_axis,
        highcharts_canvas_tools=highcharts_canvas_tools,
        highcharts_data=highcharts_data,
        highcharts_drilldown=highcharts_drilldown,
        highcharts_export_data=highcharts_export_data,
        highcharts_exporting=highcharts_exporting,
        highcharts_funnel=highcharts_funnel,
        highcharts_heatmap=highcharts_heatmap,
        highcharts_more=highcharts_more,
        highcharts_networkgraph=highcharts_networkgraph,
        highcharts_no_data=highcharts_no_data,
        highcharts_offline_exporting=highcharts_offline_exporting,
        highcharts_solid_gauge=highcharts_solid_gauge,
        highcharts_3d=highcharts_3d,
        highcharts_treemap=highcharts_treemap,
        highcharts_variwide=highcharts_variwide,
    )

    HighStock.js_files(
        highcharts_accessibility=highcharts_accessibility,
        highcharts_annotations=highcharts_annotations,
        highcharts_boost=highcharts_boost,
        highcharts_broken_axis=highcharts_broken_axis,
        highcharts_canvas_tools=highcharts_canvas_tools,
        highcharts_data=highcharts_data,
        highcharts_drilldown=highcharts_drilldown,
        highcharts_export_data=highcharts_export_data,
        highcharts_exporting=highcharts_exporting,
        highcharts_more=highcharts_more,
        highcharts_no_data=highcharts_no_data,
        highcharts_offline_exporting=highcharts_offline_exporting,
        highcharts_solid_gauge=highcharts_solid_gauge,
    )

    HighMap.js_files(
        highcharts_accessibility=highcharts_accessibility,
        highcharts_annotations=highcharts_annotations,
        highcharts_boost=highcharts_boost,
        highcharts_broken_axis=highcharts_broken_axis,
        highcharts_canvas_tools=highcharts_canvas_tools,
        highcharts_coloraxis=highcharts_coloraxis,
        highcharts_data=highcharts_data,
        highcharts_drilldown=highcharts_drilldown,
        highcharts_export_data=highcharts_export_data,
        highcharts_exporting=highcharts_exporting,
        highcharts_marker_clusters=highcharts_marker_clusters,
        highcharts_more=highcharts_more,
        highcharts_no_data=highcharts_no_data,
        highcharts_offline_exporting=highcharts_offline_exporting,
        mapdata=mapdata,
    )

    HighGantt.js_files(
        highcharts_accessibility=highcharts_accessibility,
        highcharts_annotations=highcharts_annotations,
        highcharts_boost=highcharts_boost,
        highcharts_broken_axis=highcharts_broken_axis,
        highcharts_canvas_tools=highcharts_canvas_tools,
        highcharts_data=highcharts_data,
        highcharts_drilldown=highcharts_drilldown,
        highcharts_export_data=highcharts_export_data,
        highcharts_exporting=highcharts_exporting,
        highcharts_more=highcharts_more,
        highcharts_no_data=highcharts_no_data,
        highcharts_offline_exporting=highcharts_offline_exporting,
    )
