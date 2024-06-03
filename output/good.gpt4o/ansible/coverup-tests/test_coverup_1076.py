# file lib/ansible/utils/collection_loader/_collection_finder.py:422-446
# lines [423, 424, 429, 432, 434, 436, 437, 438, 439, 440, 443, 444, 446]
# branches ['423->424', '423->429', '429->432', '429->434', '436->437', '436->446', '438->439', '438->443', '443->436', '443->444']

import os
import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockLoader(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        pass

@pytest.fixture
def mock_file(tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("test content")
    return str(test_file)

@pytest.fixture
def mock_init_file(tmp_path):
    init_file = tmp_path / "__init__.py"
    init_file.write_text("")
    return str(init_file)

def test_get_data_no_path():
    loader = MockLoader()
    with pytest.raises(ValueError, match='a path must be specified'):
        loader.get_data('')

def test_get_data_relative_path():
    loader = MockLoader()
    with pytest.raises(ValueError, match='relative resource paths not supported'):
        loader.get_data('relative/path')

def test_get_data_absolute_path(mock_file):
    loader = MockLoader()
    result = loader.get_data(mock_file)
    assert result == b"test content"

def test_get_data_init_file(mock_init_file):
    loader = MockLoader()
    result = loader.get_data(mock_init_file)
    assert result == b""

def test_get_data_non_existent_file():
    loader = MockLoader()
    result = loader.get_data('/non/existent/file')
    assert result is None
