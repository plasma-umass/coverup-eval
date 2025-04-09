# file: lib/ansible/utils/collection_loader/_collection_finder.py:336-355
# asked: {"lines": [351, 352, 353, 354, 355], "branches": [[352, 353], [352, 355], [353, 354], [353, 355]]}
# gained: {"lines": [351, 352, 353, 354, 355], "branches": [[352, 353], [352, 355], [353, 354]]}

import pytest
import sys
from types import ModuleType
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_new_or_existing_module_creates_new_module():
    module_name = 'test_module'
    assert module_name not in sys.modules

    with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, test_attr='test_value') as module:
        assert module_name in sys.modules
        assert module.test_attr == 'test_value'

    assert module_name in sys.modules
    del sys.modules[module_name]

def test_new_or_existing_module_uses_existing_module():
    module_name = 'test_module'
    existing_module = ModuleType(module_name)
    existing_module.existing_attr = 'existing_value'
    sys.modules[module_name] = existing_module

    with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, new_attr='new_value') as module:
        assert module is existing_module
        assert module.existing_attr == 'existing_value'
        assert module.new_attr == 'new_value'

    assert module_name in sys.modules
    del sys.modules[module_name]

def test_new_or_existing_module_exception_cleanup():
    module_name = 'test_module'
    assert module_name not in sys.modules

    with pytest.raises(ValueError):
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, test_attr='test_value') as module:
            assert module_name in sys.modules
            raise ValueError("Test exception")

    assert module_name not in sys.modules

def test_new_or_existing_module_exception_no_cleanup():
    module_name = 'test_module'
    existing_module = ModuleType(module_name)
    sys.modules[module_name] = existing_module

    with pytest.raises(ValueError):
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, test_attr='test_value') as module:
            assert module is existing_module
            raise ValueError("Test exception")

    assert module_name in sys.modules
    del sys.modules[module_name]
