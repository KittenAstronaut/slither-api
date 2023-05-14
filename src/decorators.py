import typing as t
from functools import partial

from src import methods


def route(methods: t.Sequence[str], path: str = ""):
    def _factory(func: t.Callable):
        func.__nest_view__ = True
        func.__nest_methods__ = methods
        func.__nest_path__ = path
        return func

    return _factory


get = partial(route, methods=(methods.GET,))
post = partial(route, methods=(methods.POST,))
put = partial(route, methods=(methods.PUT,))
patch = partial(route, methods=(methods.PATCH,))
delete = partial(route, methods=(methods.DELETE,))
head = partial(route, methods=(methods.HEAD,))
