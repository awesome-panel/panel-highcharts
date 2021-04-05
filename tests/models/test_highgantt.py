# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from panel_highcharts.models.highgantt import HighGantt


@pytest.fixture
def backup_js_files():
    javascript = HighGantt.__javascript__
    js_require = HighGantt.__js_require__
    yield
    HighGantt.__javascript__ = javascript
    HighGantt.__js_require__ = js_require


def test_class():
    # pylint: disable=unsubscriptable-object
    assert "https://code.highcharts.com/highcharts.js" in HighGantt.__javascript__
    assert "https://code.highcharts.com/modules/gantt.js" in HighGantt.__javascript__

    assert "https://code.highcharts.com/highcharts.js" in HighGantt.__js_skip__["highcharts"]
    assert "https://code.highcharts.com/modules/gantt.js" in HighGantt.__js_skip__["highcharts"]

    assert HighGantt.__js_require__["packages"] == [{"name": "highcharts", "main": "highcharts"}]
    assert HighGantt.__js_require__["paths"]["highcharts"] == "https://code.highcharts.com"
    assert (
        HighGantt.__js_require__["paths"]["highcharts/modules/gantt"]
        == "https://code.highcharts.com/modules/gantt"
    )

    assert HighGantt.__js_require__["exports"]["highcharts"] == "Highcharts"
    assert HighGantt.__js_require__["exports"]["highcharts/modules/gantt"] is None


def test_js_files(backup_js_files):  # pylint: disable=unused-argument
    # Given
    javascript = HighGantt.__javascript__
    js_skip = HighGantt.__js_skip__
    js_require = HighGantt.__js_require__
    # When
    HighGantt.js_files()
    # Then
    assert HighGantt.__javascript__ == javascript
    assert HighGantt.__js_skip__ == js_skip
    assert HighGantt.__js_require__ == js_require


def test_js_files_data(backup_js_files):  # pylint: disable=unused-argument
    # When
    HighGantt.js_files(highcharts_data=True)
    # Then
    assert "https://code.highcharts.com/modules/data.js" in HighGantt.__javascript__
    # pylint: disable=unsubscriptable-object
    assert "https://code.highcharts.com/modules/data.js" in HighGantt.__js_skip__["highcharts"]
    assert (
        HighGantt.__js_require__["paths"]["highcharts/modules/data"]
        == "https://code.highcharts.com/modules/data"
    )
