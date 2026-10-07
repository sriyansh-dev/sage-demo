import yaml


def load_config(path):
    """Load a YAML settings file into a dict."""
    with open(path) as f:
        return yaml.safe_load(f)
