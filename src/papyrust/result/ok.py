from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, Never

from .err import Err


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

    def and_then[U, F](self, f: Callable[[T], "Ok[U] | Err[F]"]) -> "Ok[U] | Err[F]":
        return f(self.value)

    def expect(self, msg: str) -> T:
        return self.value

    def unwrap(self) -> T:
        return self.value

    def unwrap_or(self, default: object) -> T:
        return self.value

    def unwrap_or_else(self, f: Callable[[Never], object]) -> T:
        return self.value
