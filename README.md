# sage-demo

A deliberately buggy mini project used to demo **S.A.G.E.** (Secure Agentic Git Engine), including its **native OS credential prompt** (`kdialog` / `zenity` / terminal fallback) for `GROQ_API_KEY`.

Known problems S.A.G.E. should find and fix, verified by `pytest`:

| File | Problem |
|---|---|
| `inventory.py` | ignores quantity, wrong discount maths, crashes on empty list |
| `shell_utils.py` | command injection via `shell=True` and breaks on paths with spaces |
| `config.py` | `yaml.load` without a Loader (unsafe, and a `TypeError` on PyYAML 6) |
| `ai_summary.py` | requires `GROQ_API_KEY` from env (triggers S.A.G.E. credential dialog) and misses the `Bearer ` prefix in `Authorization` header |

## Run & Test

```fish
# Set your Groq API key in Fish (or let S.A.G.E. prompt you via kdialog)
set -x GROQ_API_KEY <your_groq_api_key>

python main.py
python -m pytest -q
```
