# file: lib/ansible/utils/collection_loader/_collection_finder.py:336-355
# asked: {"lines": [336, 337, 338, 340, 341, 342, 343, 344, 345, 346, 348, 349, 350, 351, 352, 353, 354, 355], "branches": [[343, 344], [343, 348], [348, 349], [348, 350], [352, 353], [352, 355], [353, 354], [353, 355]]}
# gained: {"lines": [336, 337, 338, 340, 341, 342, 343, 344, 345, 346, 348, 349, 350, 351, 352, 353, 354, 355], "branches": [[343, 344], [343, 348], [348, 349], [348, 350], [352, 353], [353, 354]]}

import pytest
import sys
from types import ModuleType
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_new_or_existing_module_create():
    module_name = 'test_module'
    assert module_name not in sys.modules

    with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, attr1='value1') as module:
        assert module_name in sys.modules
        assert isinstance(module, ModuleType)
        assert module.attr1 == 'value1'

    assert module_name in sys.modules
    del sys.modules[module_name]

def test_new_or_existing_module_existing(monkeypatch):
    module_name = 'test_module'
    existing_module = ModuleType(module_name)
    existing_module.existing_attr = 'existing_value'
    monkeypatch.setitem(sys.modules, module_name, existing_module)

    with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, attr1='value1') as module:
        assert module_name in sys.modules
        assert module is existing_module
        assert module.existing_attr == 'existing_value'
        assert module.attr1 == 'value1'

    assert module_name in sys.modules
    del sys.modules[module_name]

def test_new_or_existing_module_exception():
    module_name = 'test_module'
    assert module_name not in sys.modules

    with pytest.raises(ValueError):
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, attr1='value1') as module:
            assert module_name in sys.modules
            raise ValueError("Test exception")

    assert module_name not in sys.modules
