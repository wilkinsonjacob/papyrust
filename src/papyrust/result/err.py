from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, Never


@dataclass(frozen=True, slots=True)
class Err[E]:
    error: E

    def map(self, f: Callable[[Never], object]) -> "Err[E]":
        return self

    def is_ok(self) -> Literal[False]:
        return False

    def is_err(self) -> Literal[True]:
        return True
