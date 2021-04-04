# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from panel_highcharts.models.highchart import HighChart


@pytest.fixture
def backup_js_files():
    javascript = HighChart.__javascript__
    js_require = HighChart.__js_require__
    yield
    HighChart.__javascript__ = javascript
    HighChart.__js_require__ = js_require


def test_js_files(backup_js_files):  # pylint: disable=unused-argument
    # Given
    javascript = HighChart.__javascript__
    js_skip = HighChart.__js_skip__
    js_require = HighChart.__js_require__
    # When
    HighChart.js_files()
    # Then
    assert HighChart.__javascript__ == javascript
    assert HighChart.__js_skip__ == js_skip
    assert HighChart.__js_require__ == js_require


def test_js_files_network(backup_js_files):  # pylint: disable=unused-argument
    # When
    HighChart.js_files(highcharts_networkgraph=True)
    # Then
    assert "https://code.highcharts.com/modules/networkgraph.js" in HighChart.__javascript__
    # pylint: disable=unsubscriptable-object
    assert (
        "https://code.highcharts.com/modules/networkgraph.js" in HighChart.__js_skip__["highcharts"]
    )
    assert (
        HighChart.__js_require__["paths"]["highcharts/modules/networkgraph"]
        == "https://code.highcharts.com/modules/networkgraph"
    )
