# papyrust

Rust-style Python, built for static type checkers.

> **Status: alpha.** The API is incomplete and will change between releases.

## Installation

```sh
pip install papyrust
# or
uv add papyrust
```

Requires Python 3.12 or newer. No runtime dependencies.

## Development

This project uses [uv](https://docs.astral.sh/uv/).

```sh
uv sync                                   # install dependencies
uv run pre-commit install                 # install git hooks
uv run pytest                             # run tests
uv run ty check                           # type check
uv run ruff check && uv run ruff format   # lint and format
```

Commits follow [Conventional Commits](https://www.conventionalcommits.org/).
Use `uv run cz commit` for an interactive prompt, and `uv run cz bump` to cut a
release.

## License

[MIT](LICENSE)
