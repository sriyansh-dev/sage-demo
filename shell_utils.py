import subprocess


def list_dir(path):
    """Return the sorted file names inside a directory."""
    import os
    try:
        return sorted(os.listdir(path))
    except FileNotFoundError:
        return []
