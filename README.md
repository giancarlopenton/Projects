# First Light

Python project using NumPy, Matplotlib, and PyTorch.

## Setup

Requires Python 3.14+.

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

### Updating dependencies

Add packages with `uv add <package>`, then regenerate `requirements.txt`:

```sh
uv export --format requirements-txt --no-hashes -o requirements.txt
```
