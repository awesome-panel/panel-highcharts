from glob import glob
import pathlib

CWD = pathlib.Path.cwd()
EXAMPLES = CWD / "examples"


def panel_serve_examples():
  result =  {
        'command': ["panel", "serve", *glob('examples/*.ipynb'), "--allow-websocket-origin=*", "--port", "{port}", "--prefix", "{base_url}panel"],
        'absolute_url': True,
        'timeout': 360,
  }
  print(result)
  return result