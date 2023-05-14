import typing as t

from src.interfaces.controller import ControllerProtocol
from src.router import SlitherRouter
from src.utils import wraps_class


def controller(
    path: str,
) -> t.Callable[[t.Type[ControllerProtocol]], ControllerProtocol]:
    def decorator(cls: t.Type[ControllerProtocol]) -> ControllerProtocol:
        @wraps_class(cls)
        class _ControllerWrapper:
            __nest_path__: str
            __controller_class__: t.Type[ControllerProtocol]

            def __init__(self):
                self.__nest_path__ = path
                self.__controller_class__ = cls
                self._router = SlitherRouter(
                    prefix=self.__nest_path__,
                )
                self._router.register_controller(self.__controller_class__)

        return _ControllerWrapper

    return decorator
