from typing_extensions import TypeIs

from .err import Err
from .ok import Ok

type Result[T, E] = Ok[T] | Err[E]


def is_ok[T, E](result: Result[T, E]) -> TypeIs[Ok[T]]:
    """Return ``True`` if ``result`` is ``Ok``, narrowing its type for checkers."""
    return isinstance(result, Ok)


def is_err[T, E](result: Result[T, E]) -> TypeIs[Err[E]]:
    """Return ``True`` if ``result`` is ``Err``, narrowing its type for checkers."""
    return isinstance(result, Err)
