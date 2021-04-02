"""Contains the Bokeh Model for the HighChart pane"""
from collections import OrderedDict

from bokeh.core.properties import Any, Dict, Nullable, String
from bokeh.models import LayoutDOM
from panel.util import classproperty

PATHS = OrderedDict(
    [
        ("highcharts", "https://code.highcharts.com/highcharts.js"),
        ("highcharts-3d", "https://code.highcharts.com/highcharts-3d.js"),
        ("highcharts-more", "https://code.highcharts.com/highcharts-more.js"),
        ("highcharts-exporting", "https://code.highcharts.com/modules/exporting.js"),
        ("highcharts-export-data", "https://code.highcharts.com/modules/export-data.js"),
        ("highcharts-network", "https://code.highcharts.com/modules/networkgraph.js"),
        ("highcharts-annotations", "https://code.highcharts.com/modules/annotations.js"),
        ("highcharts-boost", "https://code.highcharts.com/modules/boost.js"),
        ("highcharts-broken-axis", "https://code.highcharts.com/modules/broken-axis.js"),
        ("highcharts-canvas-tools", "https://code.highcharts.com/modules/canvas-tools.js"),
        ("highcharts-data", "https://code.highcharts.com/modules/data.js"),
        ("highcharts-drilldown", "https://code.highcharts.com/modules/drilldown.js"),
        ("highcharts-funnel", "https://code.highcharts.com/modules/funnel.js"),
        ("highcharts-heatmap", "https://code.highcharts.com/modules/heatmap.js"),
        (
            "highcharts-no-data-to-display",
            "https://code.highcharts.com/modules/no-data-to-display.js",
        ),
        (
            "highcharts-offline-exporting",
            "https://code.highcharts.com/modules/offline-exporting.js",
        ),
        ("highcharts-solid-gauge", "https://code.highcharts.com/modules/solid-gauge.js"),
        ("highcharts-treemap", "https://code.highcharts.com/modules/treemap.js"),
    ]
)


class HighChart(LayoutDOM):
    """The Bokeh Model for the HighChart pane"""

    config = Nullable(Dict(String, Any))
    config_update = Nullable(Dict(String, Any))

    # Events
    event = Nullable(Dict(String, Any))

    __javascript__ = [
        "https://code.highcharts.com/highcharts.js",
        "https://code.highcharts.com/modules/export-data.js",
        "https://code.highcharts.com/modules/exporting.js",
    ]

    @classproperty
    def __js_skip__(cls) -> Dict:  # pylint: disable=no-self-argument
        return {
            "highchart": cls.__javascript__,
        }

    # https://api.highcharts.com/class-reference/#toc5
    __js_require__ = {
        "paths": OrderedDict(
            [
                ("highcharts", "https://code.highcharts.com/highcharts"),
                ("highcharts-export-data", "https://code.highcharts.com/modules/export-data.js"),
                ("highcharts-exporting", "https://code.highcharts.com/modules/exporting.js"),
            ]
        ),
        "exports": {
            "highcharts": "Highcharts",
        },
    }

    @classmethod
    def js_files(  # pylint: disable=too-many-locals, too-many-arguments
        cls,
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
        paths = OrderedDict()
        paths["highcharts"] = PATHS["highcharts"]

        include = {
            "highcharts-accessibility": highcharts_accessibility,
            "highcharts-annotations": highcharts_annotations,
            "highcharts-boost": highcharts_boost,
            "highcharts-broken-axis": highcharts_broken_axis,
            "highcharts-canvas-tools": highcharts_canvas_tools,
            "highcharts-data": highcharts_data,
            "highcharts-drilldown": highcharts_drilldown,
            "highcharts-export-data": highcharts_export_data,
            "highcharts-exporting": highcharts_exporting,
            "highcharts-funnel": highcharts_funnel,
            "highcharts-heatmap": highcharts_heatmap,
            "highcharts-more": highcharts_more,
            "highcharts-network": highcharts_network,
            "highcharts-no-data": highcharts_no_data,
            "highcharts-offline-exporting": highcharts_offline_exporting,
            "highcharts-solid-gauge": highcharts_solid_gauge,
            "highcharts-threed": highcharts_3d,
            "highcharts-treemap": highcharts_treemap,
        }
        for key, value in include.items():
            if value:
                paths[key] = PATHS[key]

        cls.__js_require__["paths"] = paths
        cls.__javascript__ = list(paths.values())
