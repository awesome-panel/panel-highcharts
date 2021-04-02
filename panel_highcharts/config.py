"""Use

- panel_highcharts.config.js_files to define which Highcharts js files to include
"""
from panel import extension

# Enables using pn.extension("highchart")
# pylint: disable=protected-access
extension._imports["highchart"] = "panel_highcharts.models.highchart"
# pylint: enable=protected-access


def js_files(  # pylint: disable=too-many-locals, too-many-arguments
    highcharts_accessibility: bool = False,
    highcharts_annotations: bool = False,
    highcharts_boost: bool = False,
    highcharts_broken_axis: bool = False,
    highcharts_canvas_tools: bool = False,
    highcharts_data: bool = False,
    highcharts_drilldown: bool = False,
    highcharts_export_data: bool = True,
    highcharts_exporting: bool = True,
    highcharts_funnel: bool = False,
    highcharts_heatmap: bool = False,
    highcharts_more: bool = False,
    highcharts_network: bool = False,
    highcharts_no_data: bool = False,
    highcharts_offline_exporting: bool = False,
    highcharts_solid_gauge: bool = False,
    highcharts_3d: bool = False,
    highcharts_treemap: bool = False,
):
    """Configures the js files to include from https://code.highcharts.com

    Use this before using `panel.extension("highchart")`

    Args:
        highcharts_accessibility (bool, optional): Defaults to False.
        highcharts_annotations (bool, optional): Defaults to False.
        highcharts_boost (bool, optional): Defaults to False.
        highcharts_broken_axis (bool, optional): Defaults to False.
        highcharts_canvas_tools (bool, optional): Defaults to False.
        highcharts_data (bool, optional): Defaults to False.
        highcharts_drilldown (bool, optional): Defaults to False.
        highcharts_export_data (bool, optional): Defaults to True.
        highcharts_exporting (bool, optional): Defaults to True.
        highcharts_funnel (bool, optional): Defaults to False.
        highcharts_heatmap (bool, optional): Defaults to False.
        highcharts_more (bool, optional): Defaults to False.
        highcharts_network (bool, optional): Defaults to False.
        highcharts_no_data (bool, optional): Defaults to False.
        highcharts_offline_exporting (bool, optional): Defaults to False.
        highcharts_solid_gauge (bool, optional): Defaults to False.
        highcharts_3d (bool, optional): Defaults to False.
        highcharts_treemap (bool, optional): Defaults to False.
    """
    # pylint: disable=import-outside-toplevel
    from .models.highchart import HighChart

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
        highcharts_network=highcharts_network,
        highcharts_no_data=highcharts_no_data,
        highcharts_offline_exporting=highcharts_offline_exporting,
        highcharts_solid_gauge=highcharts_solid_gauge,
        highcharts_3d=highcharts_3d,
        highcharts_treemap=highcharts_treemap,
    )
