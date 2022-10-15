# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel_highcharts as ph


def test_variwide():
    ph.config.js_files(highcharts_variwide=True)
    ph.config.js_files(highcharts_variwide=False)


def test_venn():
    ph.config.js_files(highcharts_venn=True)
    ph.config.js_files(highcharts_venn=False)
