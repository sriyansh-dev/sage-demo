import subprocess


def list_dir(path):
    """Return the sorted file names inside a directory."""
    # Use a list argument to avoid shell injection and handle paths with spaces
    out = subprocess.run(["ls", path], capture_output=True, text=True)
    # Split on newlines to get file names, filter out empty strings
    files = [name for name in out.stdout.splitlines() if name]
    return sorted(files)
