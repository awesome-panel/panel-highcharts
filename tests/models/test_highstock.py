# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from panel_highcharts.models.highstock import HighStock


@pytest.fixture
def backup_js_files():
    javascript = HighStock.__javascript__
    js_require = HighStock.__js_require__
    yield
    HighStock.__javascript__ = javascript
    HighStock.__js_require__ = js_require


def test_class():
    # pylint: disable=unsubscriptable-object
    assert "https://code.highcharts.com/highcharts.js" in HighStock.__javascript__
    assert "https://code.highcharts.com/modules/stock.js" in HighStock.__javascript__

    assert "https://code.highcharts.com/highcharts.js" in HighStock.__js_skip__["highcharts"]
    assert "https://code.highcharts.com/modules/stock.js" in HighStock.__js_skip__["highcharts"]

    assert HighStock.__js_require__["packages"] == [{"name": "highcharts", "main": "highcharts"}]
    assert HighStock.__js_require__["paths"]["highcharts"] == "https://code.highcharts.com"
    assert (
        HighStock.__js_require__["paths"]["highcharts/modules/stock"]
        == "https://code.highcharts.com/modules/stock"
    )

    assert HighStock.__js_require__["exports"]["highcharts"] == "Highcharts"
    assert HighStock.__js_require__["exports"]["highcharts/modules/stock"] is None


def test_js_files(backup_js_files):  # pylint: disable=unused-argument
    # Given
    javascript = HighStock.__javascript__
    js_skip = HighStock.__js_skip__
    js_require = HighStock.__js_require__
    # When
    HighStock.js_files()
    # Then
    assert HighStock.__javascript__ == javascript
    assert HighStock.__js_skip__ == js_skip
    assert HighStock.__js_require__ == js_require


def test_js_files_data(backup_js_files):  # pylint: disable=unused-argument
    # When
    HighStock.js_files(highcharts_data=True)
    # Then
    assert "https://code.highcharts.com/modules/data.js" in HighStock.__javascript__
    # pylint: disable=unsubscriptable-object
    assert "https://code.highcharts.com/modules/data.js" in HighStock.__js_skip__["highcharts"]
    assert (
        HighStock.__js_require__["paths"]["highcharts/modules/data"]
        == "https://code.highcharts.com/modules/data"
    )
