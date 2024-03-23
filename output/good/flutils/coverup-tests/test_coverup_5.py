# file flutils/objutils.py:61-85
# lines [61, 81, 82, 83, 84, 85]
# branches ['81->82', '81->85', '82->83', '82->85', '83->82', '83->84']

import pytest
from flutils.objutils import has_any_callables

@pytest.fixture
def mock_object(mocker):
    class MockObject:
        def method(self):
            pass
    mock_obj = MockObject()
    mocker.spy(mock_obj, 'method')
    return mock_obj

def test_has_any_callables_with_callable(mock_object):
    assert has_any_callables(mock_object, 'method') is True

def test_has_any_callables_without_callable(mock_object):
    mock_object.attribute = 42
    assert has_any_callables(mock_object, 'attribute') is False

def test_has_any_callables_with_nonexistent_attribute(mock_object):
    assert has_any_callables(mock_object, 'nonexistent_method') is False

def test_has_any_callables_with_mixed_attributes(mock_object):
    mock_object.attribute = 42
    assert has_any_callables(mock_object, 'method', 'attribute', 'nonexistent_method') is True
