import inspect
import typing as t

from fastapi import APIRouter

from src.interfaces.controller import ControllerProtocol


class SlitherRouter(APIRouter):
    def register_controller(self, controller: t.Type[ControllerProtocol]):
        instance = controller()
        for key, value in controller.__dict__.items():
            if getattr(value, "__nest_view__", False):
                view = getattr(instance, key)
                self.api_route(
                    path=value.__nest_path__,
                    methods=value.__nest_methods__,
                    response_model=self._get_response_model(view=value),
                )(view)

    def _get_response_model(self, view):
        annotations = inspect.signature(view)
        return annotations.return_annotation
