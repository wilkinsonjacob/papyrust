from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Ok[T]:
    value: T

    def map[U](self, f: Callable[[T], U]) -> "Ok[U]":
        return Ok(f(self.value))

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False
