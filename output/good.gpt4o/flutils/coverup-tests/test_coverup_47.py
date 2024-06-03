# file flutils/objutils.py:61-85
# lines [61, 81, 82, 83, 84, 85]
# branches ['81->82', '81->85', '82->83', '82->85', '83->82', '83->84']

import pytest
from flutils.objutils import has_any_callables
from unittest.mock import Mock

def test_has_any_callables_with_callable_attrs():
    class TestClass:
        def method1(self):
            pass

        def method2(self):
            pass

    obj = TestClass()
    assert has_any_callables(obj, 'method1', 'method2', 'non_existent') is True

def test_has_any_callables_without_callable_attrs():
    class TestClass:
        attr1 = "value1"
        attr2 = "value2"

    obj = TestClass()
    assert has_any_callables(obj, 'attr1', 'attr2') is False

def test_has_any_callables_with_mixed_attrs():
    class TestClass:
        def method1(self):
            pass

        attr1 = "value1"

    obj = TestClass()
    assert has_any_callables(obj, 'method1', 'attr1') is True

def test_has_any_callables_with_no_attrs():
    class TestClass:
        def method1(self):
            pass

    obj = TestClass()
    assert has_any_callables(obj, 'non_existent1', 'non_existent2') is False

def test_has_any_callables_with_mock(mocker):
    mock_obj = Mock()
    mock_obj.method1 = Mock()
    mock_obj.method2 = Mock()
    mock_obj.attr1 = "value1"

    assert has_any_callables(mock_obj, 'method1', 'method2', 'attr1') is True
    assert has_any_callables(mock_obj, 'attr1') is False
