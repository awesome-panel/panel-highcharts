"""Contains the Bokeh Model for the HighStock pane"""
from collections import OrderedDict

from .highbase import PATH_HIGH_CHARTS, PATH_REQUIRE_HIGH_CHARTS, PATHS, HighBase


class HighStock(HighBase):
    """The Bokeh Model for the HighStock pane"""

    __javascript__ = [
        "https://code.highcharts.com/highcharts.js",
        "https://code.highcharts.com/modules/stock.js",
        "https://code.highcharts.com/modules/export-data.js",
        "https://code.highcharts.com/modules/exporting.js",
    ]

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
            "highcharts/modules/stock": "https://code.highcharts.com/modules/stock",
            "highcharts/modules/exporting": "https://code.highcharts.com/modules/exporting",
            "highcharts/modules/export-data": "https://code.highcharts.com/modules/export-data",
        },
        "exports": {
            "highcharts": "Highcharts",
            "highcharts/modules/stock": "highchartsmodulesstock",
            "highcharts/modules/exporting": "highchartsmodulesexporting",
            "highcharts/modules/export-data": "highchartsmodulesexportdata",
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
        highcharts_more: bool = False,
        highcharts_no_data: bool = False,
        highcharts_offline_exporting: bool = False,
        highcharts_solid_gauge: bool = False,
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
            highcharts_more (bool, optional): Defaults to False.
            highcharts_networkgraph (bool, optional): Defaults to False.
            highcharts_no_data (bool, optional): Defaults to False.
            highcharts_offline_exporting (bool, optional): Defaults to False.
            highcharts_solid_gauge (bool, optional): Defaults to False.
        """
        paths = OrderedDict()
        include = {
            "highcharts/modules/stock": True,
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
            "highcharts/modules/no-data": highcharts_no_data,
            "highcharts/modules/offline-exporting": highcharts_offline_exporting,
            "highcharts/modules/solid-gauge": highcharts_solid_gauge,
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
            **{k: k.replace("/", "").replace("-", "") for k in paths},  # type: ignore
        }
