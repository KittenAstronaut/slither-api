import inspect
import typing as t

WRAPPER_UPDATE_FIELDS = (
    "__module__",
    "__qualname__",
    "__name__",
    "__doc__",
    "__annotations__",
)


async def await_maybe(awaitable: t.Union[t.Any, t.Awaitable]):
    if inspect.isawaitable(awaitable):
        return await awaitable
    return awaitable


def wraps_class(base_class: t.Type, update_fields: list[str] = WRAPPER_UPDATE_FIELDS):
    def _update(cls: t.Type):
        for field in update_fields:
            setattr(cls, field, getattr(base_class, field))
        return cls

    return _update
