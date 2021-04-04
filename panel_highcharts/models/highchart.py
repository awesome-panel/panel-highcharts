"""Contains the Bokeh Model for the HighChart pane"""
from collections import OrderedDict

from bokeh.core.properties import Any, Dict, Nullable, String
from bokeh.models import LayoutDOM
from panel.util import classproperty

PATH_HIGH_CHARTS = "https://code.highcharts.com/highcharts.js"
PATH_REQUIRE_HIGH_CHARTS = "https://code.highcharts.com"

PATHS = OrderedDict(
    [
        ("highcharts-3d", "https://code.highcharts.com/highcharts-3d.js"),
        ("highcharts-more", "https://code.highcharts.com/highcharts-more.js"),
        ("highcharts/modules/exporting", "https://code.highcharts.com/modules/exporting.js"),
        ("highcharts/modules/export-data", "https://code.highcharts.com/modules/export-data.js"),
        ("highcharts/modules/networkgraph", "https://code.highcharts.com/modules/networkgraph.js"),
        ("highcharts/modules/annotations", "https://code.highcharts.com/modules/annotations.js"),
        ("highcharts/modules/boost", "https://code.highcharts.com/modules/boost.js"),
        ("highcharts/modules/broken-axis", "https://code.highcharts.com/modules/broken-axis.js"),
        ("highcharts/modules/canvas-tools", "https://code.highcharts.com/modules/canvas-tools.js"),
        ("highcharts/modules/data", "https://code.highcharts.com/modules/data.js"),
        ("highcharts/modules/drilldown", "https://code.highcharts.com/modules/drilldown.js"),
        ("highcharts/modules/funnel", "https://code.highcharts.com/modules/funnel.js"),
        ("highcharts/modules/heatmap", "https://code.highcharts.com/modules/heatmap.js"),
        (
            "highcharts/modules/no-data-to-display",
            "https://code.highcharts.com/modules/no-data-to-display.js",
        ),
        (
            "highcharts/modules/offline-exporting",
            "https://code.highcharts.com/modules/offline-exporting.js",
        ),
        ("highcharts/modules/solid-gauge", "https://code.highcharts.com/modules/solid-gauge.js"),
        ("highcharts/modules/treemap", "https://code.highcharts.com/modules/treemap.js"),
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
            "highcharts": cls.__javascript__,
        }

    # https://api.highcharts.com/class-reference/#toc5
    __js_require__ = {
        "packages": [
            {
                "name": "highcharts",
                "main": "highcharts",
            },
        ],
        "paths": {
            "highcharts": "https://code.highcharts.com",
            "highcharts/modules/exporting": "https://code.highcharts.com/modules/exporting",
            "highcharts/modules/export-data": "https://code.highcharts.com/modules/export-data",
        },
        "exports": {
            "highcharts": "Highcharts",
            "highcharts/modules/exporting": None,
            "highcharts/modules/export-data": None,
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
        highcharts_networkgraph: bool = False,
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
            highcharts_networkgraph (bool, optional): Defaults to False.
            highcharts_no_data (bool, optional): Defaults to False.
            highcharts_offline_exporting (bool, optional): Defaults to False.
            highcharts_solid_gauge (bool, optional): Defaults to False.
            highcharts_3d (bool, optional): Defaults to False.
            highcharts_treemap (bool, optional): Defaults to False.
        """
        paths = OrderedDict()
        include = {
            "highcharts-3d": highcharts_3d,
            "highcharts-more": highcharts_more,
            "highcharts/modules/accessibility": highcharts_accessibility,
            "highcharts/modules/annotations": highcharts_annotations,
            "highcharts/modules/boost": highcharts_boost,
            "highcharts/modules/broken-axis": highcharts_broken_axis,
            "highcharts/modules/canvas-tools": highcharts_canvas_tools,
            "highcharts/modules/data": highcharts_data,
            "highcharts/modules/drilldown": highcharts_drilldown,
            "highcharts/modules/export-data": highcharts_export_data,
            "highcharts/modules/exporting": highcharts_exporting,
            "highcharts/modules/funnel": highcharts_funnel,
            "highcharts/modules/heatmap": highcharts_heatmap,
            "highcharts/modules/networkgraph": highcharts_networkgraph,
            "highcharts/modules/no-data": highcharts_no_data,
            "highcharts/modules/offline-exporting": highcharts_offline_exporting,
            "highcharts/modules/solid-gauge": highcharts_solid_gauge,
            "highcharts/modules/treemap": highcharts_treemap,
        }
        for key, value in include.items():
            if value:
                paths[key] = PATHS[key]

        cls.__javascript__ = [PATH_HIGH_CHARTS] + list(paths.values())
        cls.__js_require__["paths"] = {
            "highcharts": PATH_REQUIRE_HIGH_CHARTS,
            **{k: v[:-3] for k, v in paths.items()},
        }
        cls.__js_require__["exports"] = {
            "highcharts": "Highcharts",
            **{k: None for k in paths},  # type: ignore
        }
