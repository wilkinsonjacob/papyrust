from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, Never, NoReturn

from ..errors import UnwrapError


@dataclass(frozen=True, slots=True)
class Err[E]:
    """Contains the error value of a ``Result``.

    Attributes:
        error: The error value.
    """

    error: E

    def is_ok(self) -> Literal[False]:
        """Return ``True`` if the result is ``Ok``."""
        return False

    def is_err(self) -> Literal[True]:
        """Return ``True`` if the result is ``Err``."""
        return True

    def map(self, f: Callable[[Never], object]) -> "Err[E]":
        """Map a ``Result[T, E]`` to a ``Result[U, E]`` by applying ``f``.

        ``f`` is applied to the contained ``Ok`` value. An ``Err`` value is left
        untouched. This can be used to compose the results of two functions.

        Args:
            f: Function to apply to the ``Ok`` value.
        """
        return self

    def map_err[F](self, f: Callable[[E], F]) -> "Err[F]":
        """Map a ``Result[T, E]`` to a ``Result[T, F]`` by applying ``f``.

        ``f`` is applied to the contained ``Err`` value. An ``Ok`` value is left
        untouched. This can be used to pass through a successful result while
        handling an error.

        Args:
            f: Function to apply to the ``Err`` value.
        """
        return Err(f(self.error))

    def and_then(self, f: Callable[[Never], object]) -> "Err[E]":
        """Call ``f`` if the result is ``Ok``, otherwise return the ``Err``.

        This can be used for control flow based on ``Result`` values.

        Args:
            f: Function to apply to the ``Ok`` value. It must itself return a
                ``Result``.
        """
        return self

    def expect(self, msg: str) -> NoReturn:
        """Return the contained ``Ok`` value.

        Because this method may raise, its use is generally discouraged. Instead,
        prefer pattern matching to handle the ``Err`` case explicitly, or call
        ``unwrap_or`` or ``unwrap_or_else``.

        Args:
            msg: Message to include in the error if the result is ``Err``.

        Raises:
            UnwrapError: If the value is an ``Err``, with a message including
                ``msg`` and the content of the ``Err``.
        """
        raise UnwrapError(f"{msg}: {self.error!r}")

    def unwrap(self) -> NoReturn:
        """Return the contained ``Ok`` value.

        Because this method may raise, its use is generally discouraged. Instead,
        prefer pattern matching to handle the ``Err`` case explicitly, or call
        ``unwrap_or`` or ``unwrap_or_else``.

        Raises:
            UnwrapError: If the value is an ``Err``, with a message including the
                content of the ``Err``.
        """
        raise UnwrapError(f"called `Result.unwrap()` on an `Err` value: {self.error!r}")

    def unwrap_or[U](self, default: U) -> U:
        """Return the contained ``Ok`` value or a provided default.

        Arguments passed to ``unwrap_or`` are eagerly evaluated; if you are
        passing the result of a function call, it is recommended to use
        ``unwrap_or_else``, which is lazily evaluated.

        Args:
            default: Value to return if the result is ``Err``.
        """
        return default

    def unwrap_or_else[U](self, f: Callable[[E], U]) -> U:
        """Return the contained ``Ok`` value or compute it from a function.

        Args:
            f: Function called with the ``Err`` value to compute the fallback. It
                is only called if the result is ``Err``.
        """
        return f(self.error)
