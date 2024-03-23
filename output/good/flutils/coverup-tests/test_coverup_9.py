# file flutils/objutils.py:36-58
# lines [36, 55, 56, 57, 58]
# branches ['55->56', '55->58', '56->55', '56->57']

import pytest
from flutils.objutils import has_any_attrs

@pytest.fixture
def mock_obj(mocker):
    class MockObj:
        pass
    mock_obj = MockObj()
    setattr(mock_obj, 'existing_attr', None)
    return mock_obj

def test_has_any_attrs_with_existing_attribute(mock_obj):
    assert has_any_attrs(mock_obj, 'existing_attr', 'non_existing_attr') is True

def test_has_any_attrs_without_existing_attribute(mock_obj):
    assert has_any_attrs(mock_obj, 'non_existing_attr1', 'non_existing_attr2') is False
