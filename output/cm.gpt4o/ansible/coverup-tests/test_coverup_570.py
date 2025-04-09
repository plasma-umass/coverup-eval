# file lib/ansible/utils/helpers.py:37-43
# lines [37, 41, 42, 43]
# branches ['41->42', '41->43']

import pytest
from unittest.mock import Mock

# Assuming the function is imported from ansible.utils.helpers
from ansible.utils.helpers import object_to_dict

class TestObjectToDict:
    def test_object_to_dict_with_exclude(self):
        class TestObject:
            def __init__(self):
                self.a = 1
                self.b = 2
                self._c = 3

        obj = TestObject()
        result = object_to_dict(obj, exclude=['b'])
        assert result == {'a': 1}

    def test_object_to_dict_without_exclude(self):
        class TestObject:
            def __init__(self):
                self.a = 1
                self.b = 2
                self._c = 3

        obj = TestObject()
        result = object_to_dict(obj)
        assert result == {'a': 1, 'b': 2}

    def test_object_to_dict_with_invalid_exclude(self):
        class TestObject:
            def __init__(self):
                self.a = 1
                self.b = 2
                self._c = 3

        obj = TestObject()
        result = object_to_dict(obj, exclude='invalid')
        assert result == {'a': 1, 'b': 2}

    def test_object_to_dict_with_empty_exclude(self, mocker):
        class TestObject:
            def __init__(self):
                self.a = 1
                self.b = 2
                self._c = 3

        obj = TestObject()
        result = object_to_dict(obj, exclude=[])
        assert result == {'a': 1, 'b': 2}
