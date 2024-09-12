# file: flutils/pathutils.py:219-333
# asked: {"lines": [219, 221, 222, 223, 274, 276, 277, 278, 279, 281, 282, 283, 286, 290, 292, 293, 294, 295, 296, 297, 298, 301, 302, 306, 307, 308, 309, 310, 311, 312, 313, 315, 316, 318, 321, 322, 324, 325, 326, 327, 330, 331, 333], "branches": [[276, 277], [276, 281], [281, 282], [281, 290], [293, 294], [293, 295], [295, 296], [295, 301], [306, 307], [306, 321], [308, 309], [308, 312], [312, 313], [312, 315], [321, 322], [321, 324], [324, 325], [324, 330], [325, 326], [325, 333]]}
# gained: {"lines": [219, 221, 222, 223, 274, 276, 277, 278, 279, 281, 282, 283, 286, 290, 292, 293, 294, 295, 296, 297, 298, 301, 302, 306, 307, 308, 309, 310, 311, 312, 313, 315, 316, 318, 321, 322, 324, 325, 326, 327, 330, 331, 333], "branches": [[276, 277], [276, 281], [281, 282], [281, 290], [293, 294], [293, 295], [295, 296], [295, 301], [306, 307], [308, 309], [308, 312], [312, 313], [312, 315], [321, 322], [321, 324], [324, 325], [324, 330], [325, 326], [325, 333]]}

import os
import pytest
from pathlib import Path
from flutils.pathutils import directory_present

def test_directory_present_creates_directory(tmp_path):
    test_path = tmp_path / "new_dir"
    result = directory_present(test_path)
    assert result == test_path
    assert test_path.is_dir()

def test_directory_present_existing_directory(tmp_path):
    test_path = tmp_path / "existing_dir"
    test_path.mkdir()
    result = directory_present(test_path)
    assert result == test_path
    assert test_path.is_dir()

def test_directory_present_raises_value_error_on_glob_pattern(tmp_path):
    test_path = tmp_path / "new_dir*"
    with pytest.raises(ValueError, match="must NOT contain any glob patterns"):
        directory_present(test_path)

def test_directory_present_raises_value_error_on_non_absolute_path(mocker):
    mock_normalize_path = mocker.patch("flutils.pathutils.normalize_path", return_value=Path("relative_dir"))
    test_path = Path("relative_dir")
    with pytest.raises(ValueError, match="must be an absolute path"):
        directory_present(test_path)

def test_directory_present_raises_file_exists_error_on_existing_file(tmp_path):
    test_path = tmp_path / "existing_file"
    test_path.touch()
    with pytest.raises(FileExistsError, match="already exists as a file"):
        directory_present(test_path)

def test_directory_present_creates_parent_directories(tmp_path):
    test_path = tmp_path / "parent_dir" / "child_dir"
    result = directory_present(test_path)
    assert result == test_path
    assert test_path.is_dir()
    assert (tmp_path / "parent_dir").is_dir()

def test_directory_present_applies_mode(tmp_path):
    test_path = tmp_path / "new_dir"
    mode = 0o755
    result = directory_present(test_path, mode=mode)
    assert result == test_path
    assert test_path.is_dir()
    assert oct(test_path.stat().st_mode & 0o777) == oct(mode)

def test_directory_present_applies_user_group(mocker, tmp_path):
    test_path = tmp_path / "new_dir"
    mock_chown = mocker.patch("flutils.pathutils.chown")
    user = "testuser"
    group = "testgroup"
    result = directory_present(test_path, user=user, group=group)
    assert result == test_path
    assert test_path.is_dir()
    mock_chown.assert_called_with(test_path, user=user, group=group)

def test_directory_present_existing_parent_non_directory(tmp_path):
    parent_path = tmp_path / "parent_file"
    parent_path.touch()
    child_path = parent_path / "child_dir"
    with pytest.raises(FileExistsError, match="parent path: .* exists as a file"):
        directory_present(child_path)
