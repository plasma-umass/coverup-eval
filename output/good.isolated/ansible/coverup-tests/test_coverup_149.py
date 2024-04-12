# file lib/ansible/utils/collection_loader/_collection_finder.py:422-446
# lines [422, 423, 424, 429, 432, 434, 436, 437, 438, 439, 440, 443, 444, 446]
# branches ['423->424', '423->429', '429->432', '429->434', '436->437', '436->446', '438->439', '438->443', '443->436', '443->444']

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase
from ansible.module_utils._text import to_bytes

class TestAnsibleCollectionPkgLoaderBase:
    @pytest.fixture
    def loader(self, mocker):
        # Mocking the _AnsibleCollectionPkgLoaderBase to not require the 'fullname' argument
        mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '__init__', return_value=None)
        return _AnsibleCollectionPkgLoaderBase()

    @pytest.fixture
    def temp_file(self, tmp_path):
        file = tmp_path / "test_file.txt"
        file.write_text("test content")
        return str(file)

    def test_get_data_with_empty_path(self, loader):
        with pytest.raises(ValueError) as excinfo:
            loader.get_data('')
        assert str(excinfo.value) == 'a path must be specified'

    def test_get_data_with_relative_path(self, loader):
        with pytest.raises(ValueError) as excinfo:
            loader.get_data('relative/path')
        assert str(excinfo.value) == 'relative resource paths not supported'

    def test_get_data_with_absolute_path_to_file(self, loader, temp_file):
        content = loader.get_data(temp_file)
        assert content == b'test content'

    def test_get_data_with_absolute_path_to_nonexistent_file(self, loader):
        assert loader.get_data('/nonexistent/path') is None

    def test_get_data_with_absolute_path_to_directory(self, loader, tmp_path):
        dir_path = tmp_path / "test_dir"
        dir_path.mkdir()
        init_file = dir_path / "__init__.py"
        init_file.touch()
        content = loader.get_data(str(init_file))
        assert content == b''

    def test_get_data_with_absolute_path_to_directory_without_init(self, loader, tmp_path):
        dir_path = tmp_path / "test_dir"
        dir_path.mkdir()
        content = loader.get_data(str(dir_path / "__init__.py"))
        assert content == ''

# Note: The actual test running should be done by pytest and not called directly in this script.
