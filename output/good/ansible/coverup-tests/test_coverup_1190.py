# file lib/ansible/parsing/dataloader.py:454-468
# lines [455, 456, 457, 459, 460, 462, 463, 464, 466, 468]
# branches ['456->457', '456->468', '457->456', '457->459', '462->463', '462->464', '464->456', '464->466']

import os
import pytest
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

@pytest.fixture
def temp_dir(tmp_path):
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    (dir_path / ".hidden").touch()
    (dir_path / "file1.txt").touch()
    (dir_path / "file2.yml").touch()
    (dir_path / "file3~").touch()
    subdir_path = dir_path / "subdir"
    subdir_path.mkdir()
    (subdir_path / "file4.yml").touch()
    return dir_path

def test_get_dir_vars_files(dataloader, temp_dir, mocker):
    mocker.patch.object(dataloader, 'list_directory', side_effect=lambda x: os.listdir(x))
    mocker.patch.object(dataloader, 'is_directory', side_effect=lambda x: os.path.isdir(x))
    mocker.patch.object(dataloader, 'is_file', side_effect=lambda x: os.path.isfile(x))

    extensions = ['.yml', '.yaml']
    found_files = dataloader._get_dir_vars_files(str(temp_dir), extensions)

    assert str(temp_dir / "file2.yml") in found_files
    assert str(temp_dir / "subdir" / "file4.yml") in found_files
    assert str(temp_dir / "file1.txt") not in found_files
    assert str(temp_dir / ".hidden") not in found_files
    assert str(temp_dir / "file3~") not in found_files
