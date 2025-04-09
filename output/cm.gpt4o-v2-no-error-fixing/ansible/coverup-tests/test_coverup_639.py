# file: lib/ansible/utils/collection_loader/_collection_finder.py:288-290
# asked: {"lines": [288, 290], "branches": []}
# gained: {"lines": [288, 290], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture
def mock_pathctx(tmp_path):
    d = tmp_path / "test_dir"
    d.mkdir()
    (d / "test_module.py").write_text("# test module")
    (d / "test_package").mkdir()
    (d / "test_package" / "__init__.py").write_text("# test package")
    return str(d)

def test_iter_modules(mock_pathctx):
    finder = _AnsiblePathHookFinder(collection_finder=None, pathctx=mock_pathctx)
    
    with patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl') as mock_iter_modules_impl:
        mock_iter_modules_impl.return_value = iter([('test_module', False), ('test_package', True)])
        
        result = list(finder.iter_modules('test_prefix'))
        
        mock_iter_modules_impl.assert_called_once_with([finder._pathctx], 'test_prefix')
        assert result == [('test_module', False), ('test_package', True)]
