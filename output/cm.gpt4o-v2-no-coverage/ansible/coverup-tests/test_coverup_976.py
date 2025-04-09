# file: lib/ansible/utils/collection_loader/_collection_finder.py:288-290
# asked: {"lines": [288, 290], "branches": []}
# gained: {"lines": [288, 290], "branches": []}

import pytest
import os
from unittest.mock import patch, MagicMock

from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

# Mocking _iter_modules_impl to avoid dependency on actual file system
def mock_iter_modules_impl(paths, prefix=''):
    if not prefix:
        prefix = ''
    else:
        prefix = prefix
    for b_path in paths:
        if not os.path.isdir(b_path):
            continue
        for b_basename in sorted(os.listdir(b_path)):
            b_candidate_module_path = os.path.join(b_path, b_basename)
            if os.path.isdir(b_candidate_module_path):
                if '.' in b_basename or b_basename == '__pycache__':
                    continue
                yield (prefix + b_basename, True)
            elif b_basename.endswith('.py') and b_basename != '__init__.py':
                yield (prefix + os.path.splitext(b_basename)[0]), False

@pytest.fixture
def mock_pathctx(tmp_path):
    # Create a temporary directory structure
    d = tmp_path / "mock_path"
    d.mkdir()
    (d / "module1.py").write_text("# module1")
    (d / "module2.py").write_text("# module2")
    (d / "subdir").mkdir()
    (d / "subdir" / "module3.py").write_text("# module3")
    (d / "__pycache__").mkdir()
    return str(d)

@pytest.fixture
def mock_collection_finder():
    return MagicMock()

def test_iter_modules_no_prefix(mock_pathctx, mock_collection_finder, monkeypatch):
    finder = _AnsiblePathHookFinder(mock_collection_finder, mock_pathctx)

    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._iter_modules_impl', mock_iter_modules_impl)

    modules = list(finder.iter_modules(''))
    assert ('module1', False) in modules
    assert ('module2', False) in modules
    assert ('subdir', True) in modules
    assert ('__pycache__', True) not in modules

def test_iter_modules_with_prefix(mock_pathctx, mock_collection_finder, monkeypatch):
    finder = _AnsiblePathHookFinder(mock_collection_finder, mock_pathctx)

    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._iter_modules_impl', mock_iter_modules_impl)

    modules = list(finder.iter_modules('prefix_'))
    assert ('prefix_module1', False) in modules
    assert ('prefix_module2', False) in modules
    assert ('prefix_subdir', True) in modules
    assert ('prefix___pycache__', True) not in modules
