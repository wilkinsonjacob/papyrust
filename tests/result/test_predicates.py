from typing import Literal, assert_type

from papyrust import Err, Ok, Result, is_err, is_ok


def check_is_ok_narrowing(result: Result[int, str]) -> None:
    if is_ok(result):
        assert_type(result, Ok[int])
    else:
        assert_type(result, Err[str])


def check_is_err_narrowing(result: Result[int, str]) -> None:
    if is_err(result):
        assert_type(result, Err[str])
    else:
        assert_type(result, Ok[int])


def test_is_ok_function() -> None:
    assert is_ok(Ok(1)) is True
    assert is_ok(Err("bad")) is False


def test_is_err_function() -> None:
    assert is_err(Err("bad")) is True
    assert is_err(Ok(1)) is False


def test_narrowing_helpers_run() -> None:
    check_is_ok_narrowing(Ok(1))
    check_is_ok_narrowing(Err("bad"))
    check_is_err_narrowing(Ok(1))
    check_is_err_narrowing(Err("bad"))


def test_variant_methods_have_literal_types() -> None:
    assert_type(Ok(1).is_ok(), Literal[True])
    assert_type(Ok(1).is_err(), Literal[False])
    assert_type(Err("bad").is_ok(), Literal[False])
    assert_type(Err("bad").is_err(), Literal[True])

    assert Ok(1).is_ok() is True
    assert Ok(1).is_err() is False
    assert Err("bad").is_ok() is False
    assert Err("bad").is_err() is True
