# file flutils/pathutils.py:219-333
# lines [274, 276, 277, 278, 279, 281, 282, 283, 286, 290, 292, 293, 294, 295, 296, 297, 298, 301, 302, 306, 307, 308, 309, 310, 311, 312, 313, 315, 316, 318, 321, 322, 324, 325, 326, 327, 330, 331, 333]
# branches ['276->277', '276->281', '281->282', '281->290', '293->294', '293->295', '295->296', '295->301', '306->307', '306->321', '308->309', '308->312', '312->313', '312->315', '321->322', '321->324', '324->325', '324->330', '325->326', '325->333']

import pytest
import os
from pathlib import Path
from flutils.pathutils import directory_present

def test_directory_present(tmp_path, mocker):
    # Mock normalize_path to return the path as is
    mocker.patch('flutils.pathutils.normalize_path', side_effect=lambda x: Path(x))
    # Mock exists_as to simulate different scenarios
    def mock_exists_as(path):
        if path == tmp_path:
            return 'directory'
        elif path in [tmp_path / 'subdir', tmp_path / 'subdir' / 'nested_dir', tmp_path / 'new_dir']:
            return ''
        elif path == tmp_path / 'existing_dir':
            return 'directory'
        elif path == tmp_path / 'file':
            return 'file'
        elif path == tmp_path / 'parent_file':
            return 'file'
        return ''
    mocker.patch('flutils.pathutils.exists_as', side_effect=mock_exists_as)
    # Mock chown and chmod to avoid actual file system changes
    mocker.patch('flutils.pathutils.chown')
    mocker.patch('flutils.pathutils.chmod')

    # Test creating a new directory
    new_dir = tmp_path / 'new_dir'
    result = directory_present(new_dir)
    assert result == new_dir
    assert new_dir.is_dir()

    # Test creating nested directories
    nested_dir = tmp_path / 'subdir' / 'nested_dir'
    result = directory_present(nested_dir)
    assert result == nested_dir
    assert nested_dir.is_dir()

    # Test existing directory
    existing_dir = tmp_path / 'existing_dir'
    existing_dir.mkdir()
    result = directory_present(existing_dir)
    assert result == existing_dir
    assert existing_dir.is_dir()

    # Test path with glob pattern
    with pytest.raises(ValueError, match="must NOT contain any glob patterns"):
        directory_present(tmp_path / 'glob*pattern')

    # Test non-absolute path
    with pytest.raises(ValueError, match="must be an absolute path"):
        directory_present('relative/path')

    # Test path that exists as a file
    file_path = tmp_path / 'file'
    file_path.touch()
    with pytest.raises(FileExistsError, match="already exists as a file"):
        directory_present(file_path)

    # Test parent path that exists as a file
    parent_file_path = tmp_path / 'parent_file' / 'child_dir'
    parent_file_path.parent.touch()
    with pytest.raises(FileExistsError, match="parent path: .* exists as a file"):
        directory_present(parent_file_path)
