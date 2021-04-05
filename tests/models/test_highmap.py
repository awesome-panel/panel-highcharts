# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from panel_highcharts.models.highmap import HighMap


@pytest.fixture
def backup_js_files():
    javascript = HighMap.__javascript__
    js_require = HighMap.__js_require__
    yield
    HighMap.__javascript__ = javascript
    HighMap.__js_require__ = js_require


def test_class():
    # pylint: disable=unsubscriptable-object
    assert "https://code.highcharts.com/highcharts.js" in HighMap.__javascript__
    assert "https://code.highcharts.com/maps/modules/map.js" in HighMap.__javascript__

    assert "https://code.highcharts.com/highcharts.js" in HighMap.__js_skip__["highcharts"]
    assert "https://code.highcharts.com/maps/modules/map.js" in HighMap.__js_skip__["highcharts"]

    assert HighMap.__js_require__["packages"] == [{"name": "highcharts", "main": "highcharts"}]
    assert HighMap.__js_require__["paths"]["highcharts"] == "https://code.highcharts.com"
    assert (
        HighMap.__js_require__["paths"]["highcharts/modules/map"]
        == "https://code.highcharts.com/maps/modules/map"
    )

    assert HighMap.__js_require__["exports"]["highcharts"] == "Highcharts"
    assert HighMap.__js_require__["exports"]["highcharts/modules/map"] is None


def test_js_files(backup_js_files):  # pylint: disable=unused-argument
    # Given
    javascript = HighMap.__javascript__
    js_skip = HighMap.__js_skip__
    js_require = HighMap.__js_require__
    # When
    HighMap.js_files()
    # Then
    assert HighMap.__javascript__ == javascript
    assert HighMap.__js_skip__ == js_skip
    assert HighMap.__js_require__ == js_require


def test_js_files_data(backup_js_files):  # pylint: disable=unused-argument
    # When
    HighMap.js_files(highcharts_data=True)
    # Then
    assert "https://code.highcharts.com/modules/data.js" in HighMap.__javascript__
    # pylint: disable=unsubscriptable-object
    assert "https://code.highcharts.com/modules/data.js" in HighMap.__js_skip__["highcharts"]
    assert (
        HighMap.__js_require__["paths"]["highcharts/modules/data"]
        == "https://code.highcharts.com/modules/data"
    )


def test_mapdata(backup_js_files):  # pylint: disable=unused-argument
    # When
    HighMap.js_files(mapdata=["historical/countries/no-2019/no-aa-all-2019"])
    # Then
    assert (
        "https://code.highcharts.com/mapdata/historical/countries/no-2019/no-aa-all-2019.js"
        in HighMap.__javascript__
    )
    # pylint: disable=unsubscriptable-object
    assert (
        "https://code.highcharts.com/mapdata/historical/countries/no-2019/no-aa-all-2019.js"
        in HighMap.__js_skip__["highcharts"]
    )
    assert (
        HighMap.__js_require__["paths"]["mapdata/historical/countries/no-2019/no-aa-all-2019"]
        == "https://code.highcharts.com/mapdata/historical/countries/no-2019/no-aa-all-2019"
    )
