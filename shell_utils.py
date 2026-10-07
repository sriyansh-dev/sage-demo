import os


def list_dir(path):
    """Return the sorted file names inside a directory."""
    try:
        return sorted(os.listdir(path))
    except FileNotFoundError:
        return []
