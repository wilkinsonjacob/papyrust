from papyrust import Err, Ok, Result


def test_public_imports() -> None:
    success: Result[int, str] = Ok(1)
    failure: Result[int, str] = Err("bad")

    assert isinstance(success, Ok)
    assert isinstance(failure, Err)
