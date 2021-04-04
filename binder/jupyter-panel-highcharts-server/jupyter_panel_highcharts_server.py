"""
Function to configure serving the panel example apps via jupyter-server-proxy.
"""
from glob import glob
import pathlib

ICON_PATH = str((pathlib.Path(__file__).parent / "panel-highcharts-apps-icon.svg").absolute())

def panel_serve_examples():
    """Returns the jupyter-server-proxy configuration for serving the example notebooks as Panel
    apps.

    Returns:
        Dict: The configuration dictionary
    """
    # See:
    # https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
    # https://github.com/holoviz/jupyter-panel-proxy/blob/master/panel_server/__init__.py
    return {
        "command": [
            "panel",
            "serve",
            *glob("examples/*.ipynb"),
            "--allow-websocket-origin=*",
            "--port",
            "{port}",
            "--prefix",
            "{base_url}panel",
        ],
        "absolute_url": True,
        "timeout": 360,
        "launcher_entry": {
            "enabled": True,
            "title": "Panel Highcharts Apps",
            "icon_path": ICON_PATH,
        },
    }
