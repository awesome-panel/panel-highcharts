"""The HighChart pane enables you to use the Highchart chart in Panel """
from typing import Dict

import param
from panel.pane.base import PaneBase
from panel.util import lazy_load
from pyviz_comms import JupyterComm

from . import config  # pylint: disable=unused-import


class HighChartBase(PaneBase):  # pylint: disable=too-many-ancestors
    """A Base Panel HighChart pane"""

    # Events: https://api.highcharts.com/highcharts/plotOptions.series.point.events
    object = param.Dict(
        default=None,
        doc="""
        The initial user configuration of the chart. Will reset the chart when ever a
        configuration is provided.""",
    )
    object_update = param.Dict(doc="""Incremental change to the initial user configuration.""")

    event = param.Dict(doc="""Events raised by the chart""")

    _add_series = param.Dict(doc="""Transfer the arguments of the add_series method""")

    priority = 0.0

    _rename = {"object": "config", "object_update": "config_update"}

    _updates = True

    _model_module = "panel_highcharts.models.highchart"
    _model = "HighChart"

    @classmethod
    def applies(cls, obj):
        if isinstance(obj, (dict, str)):
            return 0
        return False

    def _get_model(self, doc, root=None, parent=None, comm=None):
        _BkHighChart = lazy_load(  # pylint: disable=invalid-name
            self._model_module, self._model, isinstance(comm, JupyterComm)
        )
        props = self._process_param_change(self._init_params())
        if not "config_update" in props:
            props["config_update"] = self.object_update
        model = _BkHighChart(config=self.object, **props)
        root = root or model
        self._link_props(
            model,
            [
                "event",
            ],
            doc,
            root,
            comm,
        )
        self._models[root.ref["id"]] = (model, parent)
        return model

    def _update(self, ref=None, model=None):
        model.update(config=self.object, config_update=self.object_update)

    def add_series(self, options: Dict, redraw: bool = True, animation: bool = True):
        """Adds the seried specified by the options

        C.f. https://api.highcharts.com/class-reference/Highcharts.Chart#addSeries

        Args:
            options (Dict): The config options for the series.
            redraw (bool, optional): Whether to redraw the chart after adding. Defaults to True.
            animation (bool, optional): Whether to apply animation. Defaults to True.
        """
        self._add_series = {}  # hack to be able to add series multiple times
        self._add_series = {
            "options": options,
            "redraw": redraw,
            "animation": animation,
        }


class HighChart(HighChartBase):  # pylint: disable=too-many-ancestors
    """A Panel HighChart pane"""

    _model_module = "panel_highcharts.models.highchart"
    _model = "HighChart"


class HighStock(HighChartBase):  # pylint: disable=too-many-ancestors
    """A Panel HighStock pane"""

    _model_module = "panel_highcharts.models.highstock"
    _model = "HighStock"


class HighMap(HighChartBase):  # pylint: disable=too-many-ancestors
    """A Panel HighMap pane"""

    _model_module = "panel_highcharts.models.highmap"
    _model = "HighMap"


class HighGantt(HighChartBase):  # pylint: disable=too-many-ancestors
    """A Panel HighGantt pane"""

    _model_module = "panel_highcharts.models.highgantt"
    _model = "HighGantt"
