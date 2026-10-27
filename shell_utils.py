import subprocess


def list_dir(path):
    """Return the sorted file names inside a directory."""
    # Use a list argument to avoid shell injection and handle spaces in paths safely
    out = subprocess.run(["ls", path], capture_output=True, text=True)
    # Split on whitespace and filter out empty strings
    files = [name for name in out.stdout.split() if name]
    return sorted(files)
