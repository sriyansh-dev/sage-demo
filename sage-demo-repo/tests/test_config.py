from config import load_config


def test_load_config(tmp_path):
    f = tmp_path / "settings.yaml"
    f.write_text("name: demo\nretries: 3\n")
    assert load_config(str(f)) == {"name": "demo", "retries": 3}
