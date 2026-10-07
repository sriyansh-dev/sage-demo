from shell_utils import list_dir


def test_list_dir_handles_spaces_in_path(tmp_path):
    d = tmp_path / "my files"
    d.mkdir()
    (d / "a.txt").write_text("1")
    (d / "b.txt").write_text("2")
    assert list_dir(str(d)) == ["a.txt", "b.txt"]
