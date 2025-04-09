# file: lib/ansible/utils/collection_loader/_collection_finder.py:336-355
# asked: {"lines": [], "branches": [[352, 355], [353, 355]]}
# gained: {"lines": [], "branches": [[352, 355]]}

import pytest
import sys
from types import ModuleType
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_new_or_existing_module_creates_and_cleans_up_module():
    module_name = "test_module"
    module_attr = "test_attr"
    module_value = "test_value"

    with pytest.raises(Exception):
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, **{module_attr: module_value}):
            raise Exception("Triggering exception to test cleanup")

    assert module_name not in sys.modules

def test_new_or_existing_module_uses_existing_module(monkeypatch):
    module_name = "existing_module"
    existing_module = ModuleType(module_name)
    monkeypatch.setitem(sys.modules, module_name, existing_module)

    with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name) as mod:
        assert mod is existing_module

    assert sys.modules[module_name] is existing_module

def test_new_or_existing_module_sets_attributes():
    module_name = "attr_module"
    module_attr = "attr"
    module_value = "value"

    with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, **{module_attr: module_value}) as mod:
        assert getattr(mod, module_attr) == module_value

    assert module_name in sys.modules
    del sys.modules[module_name]

def test_new_or_existing_module_cleanup_on_exception():
    module_name = "cleanup_module"
    module_attr = "attr"
    module_value = "value"

    with pytest.raises(Exception):
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, **{module_attr: module_value}):
            raise Exception("Triggering exception to test cleanup")

    assert module_name not in sys.modules

def test_new_or_existing_module_no_cleanup_if_not_created(monkeypatch):
    module_name = "no_cleanup_module"
    existing_module = ModuleType(module_name)
    monkeypatch.setitem(sys.modules, module_name, existing_module)

    with pytest.raises(Exception):
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name):
            raise Exception("Triggering exception to test no cleanup")

    assert sys.modules[module_name] is existing_module
