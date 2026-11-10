from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, Never, NoReturn

from ..errors import UnwrapError


@dataclass(frozen=True, slots=True)
class Err[E]:
    error: E

    def is_ok(self) -> Literal[False]:
        return False

    def is_err(self) -> Literal[True]:
        return True

    def map(self, f: Callable[[Never], object]) -> "Err[E]":
        return self

    def map_err[F](self, f: Callable[[E], F]) -> "Err[F]":
        return Err(f(self.error))

    def unwrap(self) -> NoReturn:
        raise UnwrapError(f"called `result.unwrap()` on an `Err` value: {self.error!r}")

    def unwrap_or[U](self, default: U) -> U:
        return default
