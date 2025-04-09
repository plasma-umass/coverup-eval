# file: lib/ansible/utils/collection_loader/_collection_finder.py:605-654
# asked: {"lines": [605, 606, 607, 610, 611, 613, 614, 615, 617, 618, 620, 628, 630, 631, 633, 636, 641, 643, 645, 648, 649, 651, 652, 654], "branches": [[614, 615], [614, 617], [617, 618], [617, 620], [628, 630], [628, 641], [631, 633], [631, 636], [641, 643], [641, 645], [648, 649], [648, 651], [651, 652], [651, 654]]}
# gained: {"lines": [605, 606, 607, 610, 611, 613, 614, 615, 617, 618, 620, 628, 630, 631, 633, 636, 641, 643, 645, 648, 649, 651, 652, 654], "branches": [[614, 615], [614, 617], [617, 618], [617, 620], [628, 630], [628, 641], [631, 633], [631, 636], [641, 643], [641, 645], [648, 649], [648, 651], [651, 652], [651, 654]]}

import pytest
from unittest.mock import patch, MagicMock

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionLoader, _get_collection_metadata, _nested_dict_get, _get_ancestor_redirect

class TestAnsibleCollectionLoader:

    @patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata')
    @patch('ansible.utils.collection_loader._collection_finder._nested_dict_get')
    @patch('ansible.utils.collection_loader._collection_finder._get_ancestor_redirect')
    @patch('ansible.utils.collection_loader._collection_finder.import_module')
    def test_get_subpackage_search_paths(self, mock_import_module, mock_get_ancestor_redirect, mock_nested_dict_get, mock_get_collection_metadata):
        # Setup
        loader = _AnsibleCollectionLoader('ansible_collections.namespace.collection.module', path_list=['/fake/path'])
        candidate_paths = ['/fake/path']

        # Mocking
        mock_get_collection_metadata.return_value = {'import_redirection': {'ansible_collections.namespace.collection.module': {'redirect': 'redirected.module'}}}
        mock_nested_dict_get.return_value = {'redirect': 'redirected.module'}
        mock_get_ancestor_redirect.return_value = None
        mock_import_module.return_value = MagicMock(__path__=['/fake/redirected/path'])

        # Test explicit redirect
        result = loader._get_subpackage_search_paths(candidate_paths)
        assert result is None
        assert loader._redirect_module.__path__ == ['/fake/redirected/path']
        assert loader._redirected_package_map['ansible_collections.namespace.collection.module'] == 'redirected.module'

        # Test ancestor redirect
        mock_nested_dict_get.return_value = None
        mock_get_ancestor_redirect.return_value = 'redirected.ancestor.module'
        result = loader._get_subpackage_search_paths(candidate_paths)
        assert result is None
        assert loader._redirect_module.__path__ == ['/fake/redirected/path']

        # Test no redirect and valid candidate paths
        mock_get_ancestor_redirect.return_value = None
        mock_import_module.side_effect = ImportError
        with patch.object(loader, '_module_file_from_path', return_value=('/found/path', True, '/package/path')) as mock_module_file_from_path:
            result = loader._get_subpackage_search_paths(candidate_paths)
            assert result == ['/package/path']
            assert loader._source_code_path == '/found/path'

        # Test no redirect and no candidate paths
        with pytest.raises(ImportError, match='package has no paths'):
            loader._get_subpackage_search_paths([])

        # Test no redirect and no valid module found
        with patch.object(loader, '_module_file_from_path', return_value=('/found/path', False, None)) as mock_module_file_from_path:
            result = loader._get_subpackage_search_paths(candidate_paths)
            assert result is None

        # Cleanup
        del loader
