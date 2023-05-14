from pydantic import BaseModel

from src.app import SlitherApp
from src.controller import controller
from src.decorators import post
from src.module import module


class Result(BaseModel):
    result: str


@controller("/api")
class Controller:
    @post()
    def post(self) -> Result:
        return {
            "result": "a",
        }


@module(controllers=[Controller], providers=[], exports=[])
class Module:
    pass


app = SlitherApp.from_module(Module)
print(app.routes)
