# file: lib/ansible/utils/collection_loader/_collection_finder.py:336-355
# asked: {"lines": [], "branches": [[352, 355], [353, 355]]}
# gained: {"lines": [], "branches": [[352, 355]]}

import pytest
import sys
from types import ModuleType
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_new_or_existing_module_creates_and_removes_module_on_exception():
    module_name = "test_module"
    assert module_name not in sys.modules

    with pytest.raises(RuntimeError):
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, test_attr="test_value"):
            raise RuntimeError("Triggering exception to test cleanup")

    assert module_name not in sys.modules

def test_new_or_existing_module_uses_existing_module():
    module_name = "test_module"
    existing_module = ModuleType(module_name)
    sys.modules[module_name] = existing_module

    with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, test_attr="test_value") as mod:
        assert mod is existing_module
        assert mod.test_attr == "test_value"

    assert sys.modules[module_name] is existing_module
    del sys.modules[module_name]

def test_new_or_existing_module_cleanup_on_exception_with_existing_module():
    module_name = "test_module"
    existing_module = ModuleType(module_name)
    sys.modules[module_name] = existing_module

    with pytest.raises(RuntimeError):
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, test_attr="test_value"):
            raise RuntimeError("Triggering exception to test cleanup")

    assert sys.modules[module_name] is existing_module
    # Ensure that the attribute set during the context manager is still present
    assert hasattr(existing_module, "test_attr")
    assert existing_module.test_attr == "test_value"
    del sys.modules[module_name]
