# file lib/ansible/utils/collection_loader/_collection_finder.py:465-483
# lines [465, 466, 467, 470, 471, 472, 474, 478, 479, 481, 483]
# branches ['466->467', '466->470', '471->472', '471->474', '478->479', '478->481']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the class is imported from the module where it is defined
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    @pytest.fixture
    def loader(self, mocker):
        loader = mocker.create_autospec(_AnsibleCollectionPkgLoaderBase, instance=True)
        loader._compiled_code = None
        loader.get_code.side_effect = lambda fullname: _AnsibleCollectionPkgLoaderBase.get_code(loader, fullname)
        return loader

    def test_get_code_with_compiled_code(self, loader):
        loader._compiled_code = 'compiled_code'
        assert loader.get_code('some_fullname') == 'compiled_code'

    def test_get_code_with_no_filename(self, loader, mocker):
        mocker.patch.object(loader, 'get_filename', return_value=None)
        mocker.patch.object(loader, 'get_source', return_value='source_code')
        mocker.patch('builtins.compile', return_value='compiled_code')

        assert loader.get_code('some_fullname') == 'compiled_code'
        assert loader._compiled_code == 'compiled_code'

    def test_get_code_with_no_source_code(self, loader, mocker):
        mocker.patch.object(loader, 'get_filename', return_value='some_filename')
        mocker.patch.object(loader, 'get_source', return_value=None)

        assert loader.get_code('some_fullname') is None
        assert loader._compiled_code is None

    def test_get_code_with_source_code(self, loader, mocker):
        mocker.patch.object(loader, 'get_filename', return_value='some_filename')
        mocker.patch.object(loader, 'get_source', return_value='source_code')
        mocker.patch('builtins.compile', return_value='compiled_code')

        assert loader.get_code('some_fullname') == 'compiled_code'
        assert loader._compiled_code == 'compiled_code'
