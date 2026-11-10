from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, Never


@dataclass(frozen=True, slots=True)
class Ok[T]:
    value: T

    def is_ok(self) -> Literal[True]:
        return True

    def is_err(self) -> Literal[False]:
        return False

    def map[U](self, f: Callable[[T], U]) -> "Ok[U]":
        return Ok(f(self.value))

    def map_err(self, f: Callable[[Never], object]) -> "Ok[T]":
        return self
