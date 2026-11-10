from collections.abc import Callable
from dataclasses import dataclass
from typing import Never


@dataclass(frozen=True, slots=True)
class Err[E]:
    error: E

    def map(self, f: Callable[[Never], object]) -> "Err[E]":
        return self

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True
