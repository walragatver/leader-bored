import logging

import click
from fastapi import FastAPI

try:
    from importlib.metadata import entry_points
except ImportError:  # pragma: no cover
    from importlib_metadata import entry_points

logger = logging.getLogger(__name__)

def get_app():
    app = FastAPI(title="LeaderBored API",openapi_url="/api/openapi.json",docs_url="/api/docs")
    load_modules(app)
    return app

def load_modules(app=None):
    for ep in entry_points()["leader_bored.modules"]:
        logger.info(
            "Loading module: %s",
            ep.name,
            extra={
                "color_message": "Loading module: "
                + click.style("%s", fg="cyan")
            },
        )
        mod = ep.load()
        if app:
            init_app = getattr(mod, "init_app", None)
            if init_app:
                init_app(app)