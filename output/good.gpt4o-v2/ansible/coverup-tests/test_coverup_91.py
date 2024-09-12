# file: lib/ansible/utils/collection_loader/_collection_finder.py:336-355
# asked: {"lines": [336, 337, 338, 340, 341, 342, 343, 344, 345, 346, 348, 349, 350, 351, 352, 353, 354, 355], "branches": [[343, 344], [343, 348], [348, 349], [348, 350], [352, 353], [352, 355], [353, 354], [353, 355]]}
# gained: {"lines": [336, 337, 338, 340, 341, 342, 343, 344, 345, 346, 348, 349, 350, 351, 352, 353, 354, 355], "branches": [[343, 344], [343, 348], [348, 349], [348, 350], [352, 353], [353, 354]]}

import pytest
import sys
from types import ModuleType
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_new_or_existing_module_create_new():
    module_name = 'test_module'
    module_attr = 'test_attr'
    module_value = 'test_value'

    with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, **{module_attr: module_value}) as module:
        assert module.__name__ == module_name
        assert getattr(module, module_attr) == module_value
        assert sys.modules[module_name] is module

    # Clean up after the test
    if module_name in sys.modules:
        del sys.modules[module_name]

    assert module_name not in sys.modules

def test_new_or_existing_module_existing():
    module_name = 'test_module'
    existing_module = ModuleType(module_name)
    sys.modules[module_name] = existing_module
    module_attr = 'test_attr'
    module_value = 'test_value'

    try:
        with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, **{module_attr: module_value}) as module:
            assert module is existing_module
            assert getattr(module, module_attr) == module_value
    finally:
        del sys.modules[module_name]

def test_new_or_existing_module_exception():
    module_name = 'test_module'
    module_attr = 'test_attr'
    module_value = 'test_value'

    class CustomException(Exception):
        pass

    try:
        with pytest.raises(CustomException):
            with _AnsibleCollectionPkgLoaderBase._new_or_existing_module(module_name, **{module_attr: module_value}):
                raise CustomException()
        assert module_name not in sys.modules
    finally:
        if module_name in sys.modules:
            del sys.modules[module_name]
