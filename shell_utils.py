import subprocess


def list_dir(path):
    """Return the sorted file names inside a directory."""
    out = subprocess.run(f"ls {path}", shell=True, capture_output=True, text=True)
    return sorted(out.stdout.split())
