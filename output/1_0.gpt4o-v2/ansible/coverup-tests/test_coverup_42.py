# file: lib/ansible/module_utils/common/warnings.py:21-30
# asked: {"lines": [21, 22, 25, 26, 28, 30], "branches": [[22, 25], [22, 30], [25, 26], [25, 28]]}
# gained: {"lines": [21, 22, 25, 26, 28, 30], "branches": [[22, 25], [22, 30], [25, 26], [25, 28]]}

import pytest
from ansible.module_utils.common.warnings import deprecate, _global_deprecations

@pytest.fixture
def clear_global_deprecations():
    _global_deprecations.clear()
    yield
    _global_deprecations.clear()

def test_deprecate_with_date(clear_global_deprecations):
    msg = "This is a deprecation warning"
    date = "2023-12-31"
    deprecate(msg, date=date)
    assert len(_global_deprecations) == 1
    assert _global_deprecations[0] == {'msg': msg, 'date': date, 'collection_name': None}

def test_deprecate_with_version(clear_global_deprecations):
    msg = "This is a deprecation warning"
    version = "2.0"
    deprecate(msg, version=version)
    assert len(_global_deprecations) == 1
    assert _global_deprecations[0] == {'msg': msg, 'version': version, 'collection_name': None}

def test_deprecate_raises_type_error(clear_global_deprecations):
    with pytest.raises(TypeError, match="deprecate requires a string not a <class 'int'>"):
        deprecate(123)
