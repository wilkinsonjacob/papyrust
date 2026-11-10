from typing import Literal, assert_type

from papyrust import Err, Ok, Result


def check_isinstance_narrowing(result: Result[int, str]) -> None:
    if isinstance(result, Err):
        assert_type(result, Err[str])
        return
    assert_type(result, Ok[int])


def test_ok_predicates() -> None:
    result = Ok(1)

    assert result.is_ok() is True
    assert result.is_err() is False


def test_err_predicates() -> None:
    result = Err("bad")

    assert result.is_ok() is False
    assert result.is_err() is True


def test_predicates_have_literal_types() -> None:
    assert_type(Ok(1).is_ok(), Literal[True])
    assert_type(Ok(1).is_err(), Literal[False])
    assert_type(Err("bad").is_ok(), Literal[False])
    assert_type(Err("bad").is_err(), Literal[True])


def test_predicates_on_a_result_union() -> None:
    results: list[Result[int, str]] = [Ok(1), Err("bad"), Ok(2)]

    assert [r.is_ok() for r in results] == [True, False, True]
    assert sum(r.is_err() for r in results) == 1


def test_isinstance_narrowing_runs() -> None:
    check_isinstance_narrowing(Ok(1))
    check_isinstance_narrowing(Err("bad"))
