# file: lib/ansible/utils/collection_loader/_collection_finder.py:288-290
# asked: {"lines": [288, 290], "branches": []}
# gained: {"lines": [288, 290], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture
def mock_pathctx(tmp_path):
    d = tmp_path / "mock_dir"
    d.mkdir()
    (d / "module1.py").write_text("# test module")
    (d / "module2.py").write_text("# test module")
    (d / "subdir").mkdir()
    (d / "subdir" / "__init__.py").write_text("# test module")
    return str(d)

def test_iter_modules(mock_pathctx):
    finder = _AnsiblePathHookFinder(collection_finder=None, pathctx=mock_pathctx)
    
    with patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl') as mock_iter_modules_impl:
        mock_iter_modules_impl.return_value = iter([('module1', False), ('module2', False), ('subdir', True)])
        
        modules = list(finder.iter_modules(prefix=''))
        
        assert ('module1', False) in modules
        assert ('module2', False) in modules
        assert ('subdir', True) in modules
        mock_iter_modules_impl.assert_called_once_with([finder._pathctx], '')

