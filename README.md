# Projects

Python projects using NumPy, Matplotlib, and PyTorch.

## Environment

Developed and tested on:

| | |
|---|---|
| OS | macOS 27.0.1 (Apple Silicon, arm64) |
| Python | 3.14.5 |
| PyTorch | 2.14.1 |
| Device | Apple M4 Pro GPU via MPS |

## Setup

Requires Python 3.12 or newer (check with `python3 --version`).

### With uv (recommended)

```sh
uv sync
```

Run scripts inside the environment with `uv run python your_script.py`.

### With pip

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If `python3` is older than 3.12, use a newer one by name (e.g. `python3.12 -m venv .venv`) or use uv, which downloads a suitable Python for you.

To run the notebooks, also `pip install ipykernel` (uv installs it automatically).

### Updating dependencies

Add packages with `uv add <package>`, then regenerate `requirements.txt`:

```sh
uv export --format requirements-txt --no-hashes --no-dev -o requirements.txt
```
