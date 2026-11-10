from typing import assert_type

from papyrust import Err, Ok, Result


def boom(_: object) -> object:
    raise AssertionError("must not be called")


def half(n: int) -> Result[int, str]:
    if n % 2 == 0:
        return Ok(n // 2)
    return Err("odd")


# map


def test_ok_map_applies_function() -> None:
    assert Ok(2).map(str) == Ok("2")


def test_err_map_is_passthrough() -> None:
    assert Err("bad").map(boom) == Err("bad")


def test_map_returns_new_ok_and_leaves_original_unchanged() -> None:
    original = Ok(2)

    mapped = original.map(lambda n: n + 1)

    assert mapped == Ok(3)
    assert original == Ok(2)


def check_map_types(r: Result[int, str]) -> None:
    assert_type(r.map(str), Ok[str] | Err[str])


# map_err


def test_err_map_err_transforms_error() -> None:
    assert Err("bad").map_err(len) == Err(3)


def test_ok_map_err_is_passthrough() -> None:
    assert Ok(1).map_err(boom) == Ok(1)


def check_map_err_types(r: Result[int, str]) -> None:
    assert_type(r.map_err(len), Ok[int] | Err[int])


# and_then


def test_ok_and_then_returns_ok_from_function() -> None:
    assert Ok(4).and_then(half) == Ok(2)


def test_ok_and_then_returns_err_from_function() -> None:
    assert Ok(3).and_then(half) == Err("odd")


def test_err_and_then_short_circuits() -> None:
    assert Err("bad").and_then(boom) == Err("bad")


def test_and_then_chains_and_stops_at_first_error() -> None:
    assert Ok(8).and_then(half).and_then(half).and_then(half) == Ok(1)
    assert Ok(12).and_then(half).and_then(half).and_then(half) == Err("odd")


def check_and_then_types(r: Result[int, str]) -> None:
    assert_type(r.and_then(half), Ok[int] | Err[str])


def test_type_checks_run() -> None:
    for r in (Ok(1), Err("bad")):
        check_map_types(r)
        check_map_err_types(r)
        check_and_then_types(r)
