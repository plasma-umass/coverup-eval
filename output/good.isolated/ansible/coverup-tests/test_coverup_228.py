# file lib/ansible/utils/collection_loader/_collection_finder.py:465-483
# lines [465, 466, 467, 470, 471, 472, 474, 478, 479, 481, 483]
# branches ['466->467', '466->470', '471->472', '471->474', '478->479', '478->481']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockLoader(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, source_code, filename=None):
        self._source_code = source_code
        self._filename = filename
        self._compiled_code = None

    def get_filename(self, fullname):
        return self._filename

    def get_source(self, fullname):
        return self._source_code

@pytest.fixture
def mock_loader_no_source():
    return MockLoader(source_code=None)

@pytest.fixture
def mock_loader_empty_source():
    return MockLoader(source_code='')

@pytest.fixture
def mock_loader_valid_source():
    return MockLoader(source_code='print("Hello, world!")', filename='example.py')

def test_get_code_no_source(mock_loader_no_source):
    assert mock_loader_no_source.get_code('test_module') is None

def test_get_code_empty_source(mock_loader_empty_source):
    assert mock_loader_empty_source.get_code('test_module') is not None

def test_get_code_valid_source(mock_loader_valid_source):
    code = mock_loader_valid_source.get_code('test_module')
    assert code is not None
    assert code.co_filename == 'example.py'
