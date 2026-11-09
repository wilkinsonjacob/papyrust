from dataclasses import FrozenInstanceError

import pytest

from papyrust.result.err import Err
from papyrust.result.ok import Ok


def test_ok_stores_value() -> None:
    result = Ok(42)

    assert result.value == 42


def test_err_stores_error() -> None:
    result = Err("something went wrong")

    assert result.error == "something went wrong"


def test_ok_is_immutable() -> None:
    result = Ok(42)

    with pytest.raises(FrozenInstanceError):
        result.value = 100  # ty: ignore[invalid-assignment]


def test_err_is_immutable() -> None:
    result = Err("bad")

    with pytest.raises(FrozenInstanceError):
        result.error = "different error"  # ty: ignore[invalid-assignment]


def test_ok_supports_pattern_matching() -> None:
    result = Ok(42)

    match result:
        case Ok(value):
            assert value == 42
        case Err(_):
            pytest.fail("Expected Ok to match the Ok pattern")


def test_err_supports_pattern_matching() -> None:
    result = Err("bad")

    match result:
        case Ok(_):
            pytest.fail("Expected Err to match the Err pattern")
        case Err(error):
            assert error == "bad"


def test_err_is_err_and_is_ok() -> None:
    result = Err("bad")

    assert (result.is_ok(), result.is_err()) == (False, True)


def test_ok_is_err_and_is_ok() -> None:
    result = Ok(1)

    assert (result.is_ok(), result.is_err()) == (True, False)
