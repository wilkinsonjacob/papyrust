from .err import Err
from .ok import Ok

type Result[T, E] = Ok[T] | Err[E]
