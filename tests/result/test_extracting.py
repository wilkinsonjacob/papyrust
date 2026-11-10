from typing import assert_type

import pytest

from papyrust import Err, Ok, Result
from papyrust.errors import PapyrustError, UnwrapError

# expect


def test_ok_expect_returns_value() -> None:
    assert Ok(1).expect("should not fail") == 1


def test_err_expect_raises_with_message_and_error() -> None:
    with pytest.raises(UnwrapError) as exc_info:
        Err("bad").expect("config must load")

    assert str(exc_info.value) == "config must load: 'bad'"


# unwrap


def test_ok_unwrap_returns_value() -> None:
    assert Ok(1).unwrap() == 1


def test_err_unwrap_raises_unwrap_error() -> None:
    with pytest.raises(UnwrapError) as exc_info:
        Err("bad").unwrap()

    message = str(exc_info.value)
    assert "unwrap()" in message
    assert "Err" in message
    assert "'bad'" in message


def test_unwrap_error_is_a_papyrust_error() -> None:
    with pytest.raises(PapyrustError):
        Err("bad").unwrap()


# unwrap_or


def test_ok_unwrap_or_returns_value() -> None:
    assert Ok(1).unwrap_or(0) == 1


def test_err_unwrap_or_returns_default() -> None:
    assert Err("bad").unwrap_or(0) == 0


def test_unwrap_or_accepts_default_as_keyword() -> None:
    assert Ok(1).unwrap_or(default=0) == 1
    assert Err("bad").unwrap_or(default=0) == 0


# unwrap_or_else


def test_ok_unwrap_or_else_returns_value_without_calling_f() -> None:
    def boom(_: object) -> object:
        raise AssertionError("must not be called")

    assert Ok(1).unwrap_or_else(boom) == 1


def test_err_unwrap_or_else_calls_f_with_error() -> None:
    assert Err("bad").unwrap_or_else(len) == 3


# types


def check_extracting_types(r: Result[int, str], fallback: str) -> None:
    assert_type(r.expect("msg"), int)
    assert_type(r.unwrap(), int)
    assert_type(r.unwrap_or(0), int)
    assert_type(r.unwrap_or(fallback), int | str)
    assert_type(r.unwrap_or_else(len), int)


def test_type_checks_run() -> None:
    check_extracting_types(Ok(1), "x")
    with pytest.raises(UnwrapError):
        check_extracting_types(Err("bad"), "x")
