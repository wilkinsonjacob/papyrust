from .err import Err
from .ok import Ok

type Result[T, E] = Ok[T] | Err[E]
"""A value that is either ``Ok`` (success) or ``Err`` (failure).

``Result[T, E]`` is the type of functions that can fail: ``Ok[T]`` carries the
success value and ``Err[E]`` carries the error. Use ``match`` or ``isinstance``
to handle both cases.
"""
