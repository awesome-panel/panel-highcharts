"""This setup.py will install a package that configures the jupyter-server-proxy to
panel serve the example notebooks."""
import setuptools

setuptools.setup(
    name="jupyter-panel-highcharts-server",
    # py_modules rather than packages, since we only have 1 file
    py_modules=["jupyter_panel_highcharts_server"],
    entry_points={
        "jupyter_serverproxy_servers": [
            # name = packagename:function_name
            "panel = jupyter_panel_highcharts_server:panel_serve_examples",
        ]
    },
    install_requires=["jupyter-server-proxy"],
)
