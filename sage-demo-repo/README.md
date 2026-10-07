# sage-demo-repo

A deliberately buggy mini project used to demo **S.A.G.E.** (Secure Agentic Git Engine).

Known problems S.A.G.E. should find and fix, verified by `pytest`:

| File | Problem |
|---|---|
| `inventory.py` | ignores quantity, wrong discount maths, crashes on empty list |
| `shell_utils.py` | command injection via `shell=True` and breaks on paths with spaces |
| `config.py` | `yaml.load` without a Loader (unsafe, and a TypeError on PyYAML 6) |

Run it: `python main.py`   Test it: `python -m pytest -q`
