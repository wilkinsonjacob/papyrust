from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, Never


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
