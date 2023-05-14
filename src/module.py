import typing as t

from src.controller import ControllerProtocol
from src.router import SlitherRouter
from src.utils import wraps_class


class ModuleProtocol(t.Protocol):
    pass


def module(
    *,
    controllers: list,
    providers: list,
    exports: list,
) -> t.Callable[[t.Type[ModuleProtocol]], ModuleProtocol]:
    def decorator(cls: t.Type[object]) -> ModuleProtocol:
        @wraps_class(cls)
        class _ModuleWrapper:
            __nest_controllers__: list[t.Type[ControllerProtocol]]
            __nest_providers__: list
            __nest_exports__: list

            def __init__(self) -> None:
                self.__nest_controllers__ = controllers
                self.__nest_providers__ = providers
                self.__nest_exports__ = exports
                self._router = SlitherRouter()
                self._register_controllers()

            def _register_controllers(self):
                for controller in self.__nest_controllers__:
                    self._router.include_router(controller()._router)

        return _ModuleWrapper

    return decorator
