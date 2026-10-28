import os


def list_dir(path):
    """Return the sorted file names inside a directory."""
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        return []
    return sorted(entries)
