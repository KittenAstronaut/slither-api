from __future__ import annotations

import typing as t

from fastapi import FastAPI


class SlitherApp(FastAPI):
    @classmethod
    def from_module(cls, module: t.Type) -> SlitherApp:
        app = cls()
        app.include_router(module()._router)
        return app
