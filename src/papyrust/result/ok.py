from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, Never

from .err import Err


@dataclass(frozen=True, slots=True)
class Ok[T]:
    """Contains the success value of a ``Result``.

    Attributes:
        value: The success value.
    """

    value: T

    def is_ok(self) -> Literal[True]:
        """Return ``True`` if the result is ``Ok``."""
        return True

    def is_err(self) -> Literal[False]:
        """Return ``True`` if the result is ``Err``."""
        return False

    def map[U](self, f: Callable[[T], U]) -> "Ok[U]":
        """Map a ``Result[T, E]`` to a ``Result[U, E]`` by applying ``f``.

        ``f`` is applied to the contained ``Ok`` value. An ``Err`` value is left
        untouched. This can be used to compose the results of two functions.

        Args:
            f: Function to apply to the ``Ok`` value.
        """
        return Ok(f(self.value))

    def map_err(self, f: Callable[[Never], object]) -> "Ok[T]":
        """Map a ``Result[T, E]`` to a ``Result[T, F]`` by applying ``f``.

        ``f`` is applied to the contained ``Err`` value. An ``Ok`` value is left
        untouched. This can be used to pass through a successful result while
        handling an error.

        Args:
            f: Function to apply to the ``Err`` value.
        """
        return self

    def and_then[U, F](self, f: Callable[[T], "Ok[U] | Err[F]"]) -> "Ok[U] | Err[F]":
        """Call ``f`` if the result is ``Ok``, otherwise return the ``Err``.

        This can be used for control flow based on ``Result`` values.

        Args:
            f: Function to apply to the ``Ok`` value. It must itself return a
                ``Result``.
        """
        return f(self.value)

    def expect(self, msg: str) -> T:
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
        return self.value

    def unwrap(self) -> T:
        """Return the contained ``Ok`` value.

        Because this method may raise, its use is generally discouraged. Instead,
        prefer pattern matching to handle the ``Err`` case explicitly, or call
        ``unwrap_or`` or ``unwrap_or_else``.

        Raises:
            UnwrapError: If the value is an ``Err``, with a message including the
                content of the ``Err``.
        """
        return self.value

    def unwrap_or(self, default: object) -> T:
        """Return the contained ``Ok`` value or a provided default.

        Arguments passed to ``unwrap_or`` are eagerly evaluated; if you are
        passing the result of a function call, it is recommended to use
        ``unwrap_or_else``, which is lazily evaluated.

        Args:
            default: Value to return if the result is ``Err``.
        """
        return self.value

    def unwrap_or_else(self, f: Callable[[Never], object]) -> T:
        """Return the contained ``Ok`` value or compute it from a function.

        Args:
            f: Function called with the ``Err`` value to compute the fallback. It
                is only called if the result is ``Err``.
        """
        return self.value
