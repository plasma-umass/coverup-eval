# file: lib/ansible/utils/collection_loader/_collection_finder.py:485-486
# asked: {"lines": [486], "branches": []}
# gained: {"lines": [486], "branches": []}

import os
import pytest
from unittest.mock import patch

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Mock _iter_modules_impl to avoid dependency on actual file system
def mock_iter_modules_impl(paths, prefix=''):
    if not prefix:
        prefix = ''
    else:
        prefix = prefix
    for path in paths:
        if path == "valid_path":
            yield (prefix + "module1", True)
            yield (prefix + "module2", False)

@pytest.fixture
def collection_pkg_loader():
    class TestCollectionPkgLoader(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, paths):
            self._subpackage_search_paths = paths

    return TestCollectionPkgLoader

def test_iter_modules_executes_all_branches(collection_pkg_loader):
    loader = collection_pkg_loader(["valid_path", "invalid_path"])

    with patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl', side_effect=mock_iter_modules_impl):
        modules = list(loader.iter_modules("test_prefix"))

    assert modules == [("test_prefixmodule1", True), ("test_prefixmodule2", False)]
