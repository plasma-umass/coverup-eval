# file lib/ansible/module_utils/common/warnings.py:21-30
# lines [22, 25, 26, 28, 30]
# branches ['22->25', '22->30', '25->26', '25->28']

import pytest
from ansible.module_utils.common.warnings import deprecate

# Assuming _global_deprecations is a list that is defined in the module to store deprecation warnings
# If it's not accessible directly, you might need to mock or patch it using pytest-mock or unittest.mock

@pytest.fixture
def clean_global_deprecations(mocker):
    # Mock the _global_deprecations list
    mocker.patch('ansible.module_utils.common.warnings._global_deprecations', new=[])
    yield

def test_deprecate_with_date(clean_global_deprecations):
    from ansible.module_utils.common.warnings import _global_deprecations
    msg = "This is a deprecation message"
    date = "2023-12-31"
    collection_name = "test_collection"
    deprecate(msg, date=date, collection_name=collection_name)
    assert {'msg': msg, 'date': date, 'collection_name': collection_name} in _global_deprecations

def test_deprecate_with_version(clean_global_deprecations):
    from ansible.module_utils.common.warnings import _global_deprecations
    msg = "Another deprecation message"
    version = "2.10"
    collection_name = "test_collection"
    deprecate(msg, version=version, collection_name=collection_name)
    assert {'msg': msg, 'version': version, 'collection_name': collection_name} in _global_deprecations

def test_deprecate_with_non_string_raises_type_error(clean_global_deprecations):
    with pytest.raises(TypeError):
        deprecate(123, version="2.10")
